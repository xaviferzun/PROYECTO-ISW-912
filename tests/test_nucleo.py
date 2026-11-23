"""Pruebas de la lógica de respaldo (HB-04 y criterios de HU-01 a HU-04).

Ejecutar desde la raíz del repositorio:  python -m unittest discover -s tests -v
"""

import shutil
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from respaldo import nucleo  # noqa: E402


class PruebasRespaldo(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.origen = self.tmp / "origen"
        self.destino = self.tmp / "destino"
        self.log = self.tmp / "respaldos.log"
        (self.origen / "sub carpeta" / "año 2026").mkdir(parents=True)
        self.destino.mkdir()
        (self.origen / "factura.txt").write_text("Factura 001", encoding="utf-8")
        (self.origen / "sub carpeta" / "clientes ñandú.csv").write_text("id,nombre\n1,Ana", encoding="utf-8")
        (self.origen / "sub carpeta" / "año 2026" / "foto.bin").write_bytes(bytes(range(256)) * 40)

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def respaldar(self):
        return nucleo.respaldar(str(self.origen), str(self.destino), log=self.log)

    # HU-01 ----------------------------------------------------------------
    def test_valida_rutas(self):
        self.assertIsNone(nucleo.validar_rutas(str(self.origen), str(self.destino)))
        self.assertIn("no existe", nucleo.validar_rutas(str(self.tmp / "nada"), str(self.destino)))
        self.assertIn("no está disponible", nucleo.validar_rutas(str(self.origen), str(self.tmp / "nada")))
        dentro = self.origen / "respaldos"
        dentro.mkdir()
        self.assertIn("dentro", nucleo.validar_rutas(str(self.origen), str(dentro)))

    def test_guarda_y_carga_configuracion(self):
        archivo = self.tmp / "config.json"
        nucleo.guardar_config(nucleo.Configuracion(str(self.origen), str(self.destino)), archivo)
        cargada = nucleo.cargar_config(archivo)
        self.assertEqual(cargada.origen, str(self.origen))
        self.assertEqual(cargada.destino, str(self.destino))

    # HU-02 y HB-04 --------------------------------------------------------
    def test_respaldo_copia_todo_con_subcarpetas(self):
        res = self.respaldar()
        self.assertEqual(res.estado, "EXITO")
        self.assertEqual(res.archivos, 3)
        copia = Path(res.carpeta)
        for archivo in self.origen.rglob("*"):
            if archivo.is_file():
                rel = archivo.relative_to(self.origen)
                self.assertEqual(archivo.read_bytes(), (copia / rel).read_bytes(), rel)

    def test_respaldos_no_se_sobrescriben(self):
        r1, r2 = self.respaldar(), self.respaldar()
        self.assertNotEqual(r1.carpeta, r2.carpeta)
        self.assertEqual(len(nucleo.listar_respaldos(str(self.destino))), 2)

    def test_un_archivo_con_error_no_detiene_el_respaldo(self):
        copia_real = shutil.copy2

        def copia_con_falla(src, dst, *a, **k):
            if Path(src).name == "factura.txt":
                raise PermissionError(13, "Permiso denegado")
            return copia_real(src, dst, *a, **k)

        with mock.patch.object(nucleo.shutil, "copy2", copia_con_falla):
            res = self.respaldar()
        self.assertEqual(res.estado, "EXITO PARCIAL")
        self.assertEqual(res.archivos, 2)
        self.assertEqual(res.fallidos[0][0], "factura.txt")

    # HU-03 ----------------------------------------------------------------
    def test_origen_invalido_falla_sin_excepcion_y_queda_en_log(self):
        res = nucleo.respaldar(str(self.tmp / "no-existe"), str(self.destino), log=self.log)
        self.assertEqual(res.estado, "FALLO")
        self.assertIn("FALLO", self.log.read_text(encoding="utf-8"))

    def test_log_registra_cada_respaldo(self):
        self.respaldar()
        linea = self.log.read_text(encoding="utf-8").splitlines()[0]
        self.assertIn("RESPALDO | EXITO", linea)
        self.assertIn("archivos=3", linea)

    # HU-04 ----------------------------------------------------------------
    def test_restauracion_completa_recupera_lo_borrado(self):
        res = self.respaldar()
        shutil.rmtree(self.origen)
        self.origen.mkdir()
        rest = nucleo.restaurar(res.carpeta, str(self.origen), log=self.log)
        self.assertEqual(rest.estado, "EXITO")
        self.assertEqual(rest.archivos, 3)
        self.assertEqual((self.origen / "factura.txt").read_text(encoding="utf-8"), "Factura 001")
        self.assertFalse((self.origen / nucleo.MANIFIESTO).exists())

    def test_restaurar_pide_confirmacion_si_hay_archivos_iguales(self):
        res = self.respaldar()
        (self.origen / "factura.txt").write_text("cambiado", encoding="utf-8")
        self.assertIn("factura.txt", nucleo.conflictos(res.carpeta, str(self.origen)))
        sin_permiso = nucleo.restaurar(res.carpeta, str(self.origen), log=self.log)
        self.assertEqual(sin_permiso.estado, "FALLO")
        self.assertEqual((self.origen / "factura.txt").read_text(encoding="utf-8"), "cambiado")
        con_permiso = nucleo.restaurar(res.carpeta, str(self.origen), reemplazar=True, log=self.log)
        self.assertEqual(con_permiso.estado, "EXITO")
        self.assertEqual((self.origen / "factura.txt").read_text(encoding="utf-8"), "Factura 001")


if __name__ == "__main__":
    unittest.main()
