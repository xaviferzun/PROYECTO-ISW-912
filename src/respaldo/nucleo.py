"""Lógica del sistema de respaldo: configuración, respaldo, listado y restauración.

No depende de la interfaz gráfica, así se puede probar con las pruebas de tests/.
"""

from __future__ import annotations

import json
import os
import shutil
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

PREFIJO = "respaldo_"
FORMATO_FECHA = "%Y-%m-%d_%H-%M-%S"
MANIFIESTO = "manifiesto.json"

CARPETA_APP = Path.home() / ".sistema-respaldo"
ARCHIVO_CONFIG = CARPETA_APP / "config.json"
ARCHIVO_LOG = CARPETA_APP / "respaldos.log"


# ---------------------------------------------------------------- configuración

@dataclass
class Configuracion:
    origen: str = ""
    destino: str = ""


def cargar_config(archivo: Path = ARCHIVO_CONFIG) -> Configuracion:
    if not archivo.exists():
        return Configuracion()
    try:
        datos = json.loads(archivo.read_text(encoding="utf-8"))
        return Configuracion(origen=datos.get("origen", ""), destino=datos.get("destino", ""))
    except (OSError, ValueError):
        return Configuracion()


def guardar_config(config: Configuracion, archivo: Path = ARCHIVO_CONFIG) -> None:
    archivo.parent.mkdir(parents=True, exist_ok=True)
    datos = {"origen": config.origen, "destino": config.destino}
    archivo.write_text(json.dumps(datos, indent=2, ensure_ascii=False), encoding="utf-8")


def validar_rutas(origen: str, destino: str) -> str | None:
    """Devuelve un mensaje de error para el usuario, o None si las rutas sirven (HU-01)."""
    if not origen or not destino:
        return "Elija una carpeta de origen y una carpeta de destino."
    o, d = Path(origen), Path(destino)
    if not o.is_dir():
        return f"La carpeta de origen no existe: {origen}"
    if not d.is_dir():
        return f"La carpeta de destino no está disponible: {destino}. Si es un disco externo, conéctelo."
    o, d = o.resolve(), d.resolve()
    if o == d:
        return "El origen y el destino no pueden ser la misma carpeta."
    if o in d.parents:
        return "El destino no puede estar dentro de la carpeta que se va a respaldar."
    return None


# ---------------------------------------------------------------- resultados y log

@dataclass
class Resultado:
    operacion: str               # RESPALDO o RESTAURACION
    estado: str = "FALLO"        # EXITO, EXITO PARCIAL o FALLO
    archivos: int = 0
    bytes: int = 0
    fallidos: list[tuple[str, str]] = field(default_factory=list)
    mensaje: str = ""
    carpeta: str = ""
    duracion: float = 0.0

    def resumen(self) -> str:
        lineas = [
            f"Resultado: {self.estado}",
            f"Archivos: {self.archivos} ({tamano_legible(self.bytes)})",
            f"Duración: {self.duracion:.1f} s",
        ]
        if self.carpeta:
            lineas.append(f"Carpeta: {self.carpeta}")
        if self.mensaje:
            lineas.append(self.mensaje)
        if self.fallidos:
            lineas.append(f"No se pudieron copiar {len(self.fallidos)} archivo(s):")
            lineas += [f"  - {ruta}: {motivo}" for ruta, motivo in self.fallidos[:10]]
            if len(self.fallidos) > 10:
                lineas.append(f"  ... y {len(self.fallidos) - 10} más (ver el log)")
        return "\n".join(lineas)


def tamano_legible(n: int) -> str:
    valor = float(n)
    for unidad in ("B", "KB", "MB", "GB"):
        if valor < 1024 or unidad == "GB":
            return f"{valor:.0f} {unidad}" if unidad == "B" else f"{valor:.1f} {unidad}"
        valor /= 1024
    return f"{n} B"


def registrar(resultado: Resultado, origen: str, destino: str, log: Path = ARCHIVO_LOG) -> None:
    """Escribe una línea en el log por cada operación, aunque falle (HU-03)."""
    log.parent.mkdir(parents=True, exist_ok=True)
    linea = (
        f"{datetime.now():%Y-%m-%d %H:%M:%S} | {resultado.operacion} | {resultado.estado} | "
        f"origen={origen} | destino={destino} | archivos={resultado.archivos} | "
        f"fallidos={len(resultado.fallidos)} | {tamano_legible(resultado.bytes)} | "
        f"{resultado.duracion:.1f} s"
    )
    if resultado.mensaje and resultado.estado == "FALLO":
        linea += f" | motivo={resultado.mensaje}"
    with log.open("a", encoding="utf-8") as f:
        f.write(linea + "\n")
        for ruta, motivo in resultado.fallidos:
            f.write(f"    no copiado: {ruta} ({motivo})\n")


def _estado(copiados: int, fallidos: int) -> str:
    if fallidos == 0:
        return "EXITO"
    return "EXITO PARCIAL" if copiados > 0 else "FALLO"


# ---------------------------------------------------------------- respaldo (HU-02)

def _nueva_carpeta(destino: Path) -> Path:
    base = destino / f"{PREFIJO}{datetime.now():{FORMATO_FECHA}}"
    carpeta, n = base, 2
    while carpeta.exists():  # dos respaldos en el mismo segundo no se pisan
        carpeta = Path(f"{base}_{n}")
        n += 1
    return carpeta


def respaldar(origen: str, destino: str, avance=None, log: Path = ARCHIVO_LOG) -> Resultado:
    """Copia todo el origen a una carpeta nueva con fecha dentro del destino.

    Si un archivo falla, sigue con los demás y lo anota. Nunca lanza excepciones
    hacia la interfaz: todo problema queda en el Resultado y en el log.
    """
    inicio = time.perf_counter()
    res = Resultado(operacion="RESPALDO")
    error = validar_rutas(origen, destino)
    if error:
        res.mensaje = error
        registrar(res, origen, destino, log)
        return res

    carpeta = _nueva_carpeta(Path(destino))
    try:
        carpeta.mkdir(parents=True)
    except OSError as e:
        res.mensaje = f"No se pudo crear la carpeta del respaldo: {e}"
        registrar(res, origen, destino, log)
        return res

    res.carpeta = str(carpeta)
    copiados: list[dict] = []
    for raiz, _dirs, archivos in os.walk(origen):
        for nombre in archivos:
            src = Path(raiz) / nombre
            rel = src.relative_to(origen)
            dst = carpeta / rel
            try:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
                tam = dst.stat().st_size
                res.archivos += 1
                res.bytes += tam
                copiados.append({"ruta": rel.as_posix(), "bytes": tam})
            except OSError as e:
                res.fallidos.append((rel.as_posix(), e.strerror or str(e)))
            if avance:
                avance(res.archivos + len(res.fallidos), rel.as_posix())

    res.estado = _estado(res.archivos, len(res.fallidos))
    if res.archivos == 0 and not res.fallidos:
        res.estado = "EXITO"
        res.mensaje = "La carpeta de origen está vacía."
    res.duracion = time.perf_counter() - inicio

    manifiesto = {
        "fecha": datetime.now().isoformat(timespec="seconds"),
        "origen": str(Path(origen).resolve()),
        "estado": res.estado,
        "archivos": copiados,
        "fallidos": [{"ruta": r, "motivo": m} for r, m in res.fallidos],
    }
    (carpeta / MANIFIESTO).write_text(json.dumps(manifiesto, indent=2, ensure_ascii=False), encoding="utf-8")
    registrar(res, origen, destino, log)
    return res


# ---------------------------------------------------------------- listado (HU-04)

@dataclass
class InfoRespaldo:
    nombre: str
    ruta: Path
    fecha: datetime
    archivos: int
    estado: str

    def etiqueta(self) -> str:
        return f"{self.fecha:%d/%m/%Y %H:%M:%S}  ·  {self.archivos} archivos  ·  {self.estado}"


def listar_respaldos(destino: str) -> list[InfoRespaldo]:
    """Respaldos encontrados en el destino, del más reciente al más antiguo."""
    d = Path(destino)
    if not d.is_dir():
        return []
    lista = []
    for carpeta in d.iterdir():
        if not (carpeta.is_dir() and carpeta.name.startswith(PREFIJO)):
            continue
        texto = carpeta.name[len(PREFIJO):len(PREFIJO) + 19]
        try:
            fecha = datetime.strptime(texto, FORMATO_FECHA)
        except ValueError:
            continue
        archivos, estado = 0, "?"
        try:
            datos = json.loads((carpeta / MANIFIESTO).read_text(encoding="utf-8"))
            archivos, estado = len(datos.get("archivos", [])), datos.get("estado", "?")
        except (OSError, ValueError):
            archivos = sum(1 for p in carpeta.rglob("*") if p.is_file())
        lista.append(InfoRespaldo(carpeta.name, carpeta, fecha, archivos, estado))
    return sorted(lista, key=lambda r: (r.fecha, r.nombre), reverse=True)


# ---------------------------------------------------------------- restauración (HU-04)

def _archivos_del_respaldo(respaldo: Path):
    for p in respaldo.rglob("*"):
        if p.is_file() and p.relative_to(respaldo).as_posix() != MANIFIESTO:
            yield p


def conflictos(respaldo: str, destino: str) -> list[str]:
    """Archivos del respaldo que ya existen en el destino y se reemplazarían."""
    r, d = Path(respaldo), Path(destino)
    return [p.relative_to(r).as_posix() for p in _archivos_del_respaldo(r) if (d / p.relative_to(r)).exists()]


def restaurar(respaldo: str, destino: str, reemplazar: bool = False, log: Path = ARCHIVO_LOG) -> Resultado:
    """Copia el contenido de un respaldo a la carpeta elegida.

    Si reemplazar es False y hay archivos con el mismo nombre, no toca nada:
    la interfaz debe pedir confirmación antes (HU-04).
    """
    inicio = time.perf_counter()
    res = Resultado(operacion="RESTAURACION", carpeta=destino)
    r, d = Path(respaldo), Path(destino)
    if not r.is_dir():
        res.mensaje = "El respaldo seleccionado ya no existe."
    elif not d.is_dir():
        res.mensaje = f"La carpeta donde restaurar no existe: {destino}"
    elif not reemplazar and conflictos(respaldo, destino):
        res.mensaje = "Hay archivos con el mismo nombre en el destino. Confirme si desea reemplazarlos."
    if res.mensaje:
        registrar(res, respaldo, destino, log)
        return res

    for src in _archivos_del_respaldo(r):
        rel = src.relative_to(r)
        try:
            (d / rel).parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, d / rel)
            res.archivos += 1
            res.bytes += src.stat().st_size
        except OSError as e:
            res.fallidos.append((rel.as_posix(), e.strerror or str(e)))

    res.estado = _estado(res.archivos, len(res.fallidos))
    res.duracion = time.perf_counter() - inicio
    registrar(res, respaldo, destino, log)
    return res
