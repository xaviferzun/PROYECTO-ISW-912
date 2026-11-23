"""Ventana principal del Sistema de Respaldo y Recuperación (Tkinter)."""

from __future__ import annotations

import os
import queue
import subprocess
import sys
import threading
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from . import nucleo


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Sistema de Respaldo y Recuperación")
        self.geometry("760x560")
        self.minsize(640, 480)
        self.cola: queue.Queue = queue.Queue()
        self.respaldos: list[nucleo.InfoRespaldo] = []

        config = nucleo.cargar_config()
        self.origen = tk.StringVar(value=config.origen)
        self.destino = tk.StringVar(value=config.destino)
        self.estado = tk.StringVar(value="Listo.")

        self._construir()
        self.actualizar_lista()

    # ------------------------------------------------------------ interfaz

    def _construir(self) -> None:
        marco = ttk.Frame(self, padding=12)
        marco.pack(fill="both", expand=True)

        # HU-01: configuración
        conf = ttk.LabelFrame(marco, text="1. Configuración", padding=10)
        conf.pack(fill="x")
        for fila, (texto, var) in enumerate((("Carpeta a respaldar:", self.origen), ("Guardar respaldos en:", self.destino))):
            ttk.Label(conf, text=texto).grid(row=fila, column=0, sticky="w", pady=3)
            ttk.Entry(conf, textvariable=var).grid(row=fila, column=1, sticky="ew", padx=6)
            ttk.Button(conf, text="Elegir...", command=lambda v=var: self.elegir(v)).grid(row=fila, column=2)
        conf.columnconfigure(1, weight=1)
        ttk.Button(conf, text="Guardar configuración", command=self.guardar).grid(row=2, column=2, sticky="e", pady=(6, 0))

        # HU-02 y HU-03: respaldo y resultado
        resp = ttk.LabelFrame(marco, text="2. Respaldo", padding=10)
        resp.pack(fill="x", pady=8)
        self.btn_respaldar = ttk.Button(resp, text="Respaldar ahora", command=self.respaldar)
        self.btn_respaldar.pack(side="left")
        self.barra = ttk.Progressbar(resp, mode="indeterminate", length=200)
        self.barra.pack(side="left", padx=10)
        ttk.Button(resp, text="Ver log", command=self.ver_log).pack(side="right")

        # HU-04: respaldos disponibles y restauración
        rest = ttk.LabelFrame(marco, text="3. Respaldos disponibles", padding=10)
        rest.pack(fill="both", expand=True)
        self.lista = tk.Listbox(rest, height=8, activestyle="none")
        self.lista.pack(side="left", fill="both", expand=True)
        barra_lista = ttk.Scrollbar(rest, orient="vertical", command=self.lista.yview)
        barra_lista.pack(side="left", fill="y")
        self.lista.configure(yscrollcommand=barra_lista.set)
        botones = ttk.Frame(rest)
        botones.pack(side="left", fill="y", padx=(8, 0))
        ttk.Button(botones, text="Restaurar...", command=self.restaurar).pack(fill="x")
        ttk.Button(botones, text="Abrir carpeta", command=self.abrir_respaldo).pack(fill="x", pady=4)
        ttk.Button(botones, text="Actualizar lista", command=self.actualizar_lista).pack(fill="x")

        ttk.Label(marco, textvariable=self.estado, anchor="w").pack(fill="x", pady=(8, 0))

    # ------------------------------------------------------------ HU-01

    def elegir(self, var: tk.StringVar) -> None:
        carpeta = filedialog.askdirectory(initialdir=var.get() or None)
        if carpeta:
            var.set(carpeta)

    def guardar(self) -> bool:
        error = nucleo.validar_rutas(self.origen.get(), self.destino.get())
        if error:
            messagebox.showerror("Configuración no válida", error)
            return False
        nucleo.guardar_config(nucleo.Configuracion(self.origen.get(), self.destino.get()))
        self.estado.set("Configuración guardada.")
        self.actualizar_lista()
        return True

    # ------------------------------------------------------------ HU-02 y HU-03

    def respaldar(self) -> None:
        if not self.guardar():
            return
        self.btn_respaldar.state(["disabled"])
        self.barra.start(12)
        self.estado.set("Respaldando...")
        origen, destino = self.origen.get(), self.destino.get()

        def trabajo():
            res = nucleo.respaldar(origen, destino, avance=lambda n, ruta: self.cola.put(("avance", n, ruta)))
            self.cola.put(("fin", res))

        threading.Thread(target=trabajo, daemon=True).start()
        self.after(100, self._revisar_cola)

    def _revisar_cola(self) -> None:
        try:
            while True:
                msg = self.cola.get_nowait()
                if msg[0] == "avance":
                    self.estado.set(f"Respaldando... {msg[1]} archivos ({msg[2]})")
                else:
                    self._fin_respaldo(msg[1])
                    return
        except queue.Empty:
            pass
        self.after(100, self._revisar_cola)

    def _fin_respaldo(self, res: nucleo.Resultado) -> None:
        self.barra.stop()
        self.btn_respaldar.state(["!disabled"])
        self.estado.set(f"Último respaldo: {res.estado} · {res.archivos} archivos")
        self.actualizar_lista()
        if res.estado == "EXITO":
            messagebox.showinfo("Respaldo terminado", res.resumen())
        elif res.estado == "EXITO PARCIAL":
            messagebox.showwarning("Respaldo con errores", res.resumen())
        else:
            messagebox.showerror("El respaldo falló", res.resumen())

    def ver_log(self) -> None:
        if not nucleo.ARCHIVO_LOG.exists():
            messagebox.showinfo("Log", "Todavía no hay operaciones registradas.")
            return
        ventana = tk.Toplevel(self)
        ventana.title("Log de operaciones")
        ventana.geometry("820x360")
        texto = tk.Text(ventana, wrap="none")
        texto.pack(fill="both", expand=True)
        texto.insert("1.0", nucleo.ARCHIVO_LOG.read_text(encoding="utf-8"))
        texto.see("end")
        texto.configure(state="disabled")

    # ------------------------------------------------------------ HU-04

    def actualizar_lista(self) -> None:
        self.respaldos = nucleo.listar_respaldos(self.destino.get())
        self.lista.delete(0, "end")
        for r in self.respaldos:
            self.lista.insert("end", r.etiqueta())
        if not self.respaldos:
            self.lista.insert("end", "(No hay respaldos en el destino todavía)")

    def _seleccionado(self) -> nucleo.InfoRespaldo | None:
        sel = self.lista.curselection()
        if not sel or not self.respaldos:
            messagebox.showinfo("Restaurar", "Seleccione un respaldo de la lista.")
            return None
        return self.respaldos[sel[0]]

    def restaurar(self) -> None:
        resp = self._seleccionado()
        if not resp:
            return
        destino = filedialog.askdirectory(title="¿Dónde desea restaurar los archivos?")
        if not destino:
            return
        repetidos = nucleo.conflictos(str(resp.ruta), destino)
        reemplazar = False
        if repetidos:
            muestra = "\n".join(repetidos[:8]) + ("\n..." if len(repetidos) > 8 else "")
            reemplazar = messagebox.askyesno(
                "Archivos existentes",
                f"{len(repetidos)} archivo(s) ya existen en la carpeta y se van a reemplazar:\n\n{muestra}\n\n¿Desea continuar?",
            )
            if not reemplazar:
                self.estado.set("Restauración cancelada.")
                return
        res = nucleo.restaurar(str(resp.ruta), destino, reemplazar=reemplazar)
        self.estado.set(f"Última restauración: {res.estado} · {res.archivos} archivos")
        mostrar = messagebox.showinfo if res.estado == "EXITO" else messagebox.showwarning
        mostrar("Restauración terminada", res.resumen())

    def abrir_respaldo(self) -> None:
        resp = self._seleccionado()
        if not resp:
            return
        if sys.platform == "win32":
            os.startfile(resp.ruta)  # type: ignore[attr-defined]
        else:
            subprocess.Popen(["open" if sys.platform == "darwin" else "xdg-open", str(resp.ruta)])


def main() -> None:
    App().mainloop()
