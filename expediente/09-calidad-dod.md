# Sección 09 — Calidad y Definition of Done

> **Semana:** 10 · **Responsable:** Maria Paz Ugalde Araya· **Estado:** Borrador

## Criterios de calidad

El producto protege información valiosa de personas y organizaciones que no cuentan con un área de TI. 
Un respaldo que falla o que no se puede restaurar es peor que no tener respaldo porque da una falsa sensación de seguridad. Los criterios priorizan la **confiabilidad** y la **Integridad** por encima de cualquier otra cosa.

Las metas son valores iniciales del equipo y se revisan en la Retrospectiva de cada Sprint, según lo que se aprenda al probar.

| Criterio | Qué significa en este producto | Cómo se mide (meta) | Historias | Riesgo ([Sección 08](08-riesgos-adquisiciones.md)) |
|---|---|---|---|---|
| **Confiabilidad del respaldo** | Cada respaldo termina completo o falla de forma visible. Nunca sobrescribe respaldos anteriores, un archivo con problema no detiene a los demás y los respaldos programados se ejecutan sin intervención. | • Con las carpetas de ejemplo, el 100 % de los archivos está en el respaldo cuando el resultado es «éxito».<br>• El 100 % de los fallos (totales o parciales) queda en el log y se muestra al usuario.<br>• Los respaldos programados de las pruebas se ejecutan a la hora configurada. | HU-02, HU-03, HU-06, HU-09 | R-03, R-04 |
| **Integridad** | La copia y la información restaurada son idénticas a la original, y el sistema puede demostrarlo. | • 0 diferencias entre origen y respaldo, y entre respaldo y restauración (comparación de carpetas o de huellas hash).<br>• La verificación detecta el 100 % de los archivos alterados o faltantes en los casos de prueba. | HU-02, HU-04, HU-05, HU-08 | R-03, R-06 |
| **Usabilidad** | Una persona sin conocimientos de TI puede configurar, respaldar y recuperar un archivo sin ayuda. Los mensajes dicen qué pasó y qué hacer. | • En la prueba con usuarios, al menos 3 de 4 tareas se completan sin ayuda.<br>• Puntaje promedio de sencillez de 4 o más sobre 5.<br>• Todo mensaje de error indica la causa y la acción sugerida (ej. «El destino no está disponible: conecte el disco externo»). | HU-01, HU-03, HU-07, HU-09 | R-07 |
| **Compatibilidad** | El producto funciona en las máquinas de ambos integrantes y con distintos nombres, tipos y estructuras de archivos, como exige la restricción de compatibilidad de la [Sección 02](02-contexto-restricciones.md). | • Cada historia con código se prueba y pasa en las dos máquinas.<br>• Las carpetas con tildes, «ñ», espacios y tipos de archivo mixtos (CE-02 y CE-03) se respaldan y restauran sin diferencias. | Todas las historias con código | R-02 |

### Criterios de apoyo

- **Trazabilidad:** Todo respaldo deja una entrada en el log con fecha, hora y resultado incluso cuando falla, es la base para consultar el historial (HU-07) y para depurar errores.
- **Privacidad en las pruebas:** Las pruebas usan solo datos ficticios y el log no guarda el contenido de los archivos, el cifrado de los respaldos está fuera de alcance ([Sección 06](06-alcance-product-backlog.md)); por eso este criterio cubre solo lo que el equipo sí controla (riesgo R-08).


## Definition of Done

_Pendiente._

## Estrategia de validación

_Pendiente._

