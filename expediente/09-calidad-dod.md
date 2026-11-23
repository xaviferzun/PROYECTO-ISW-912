# Sección 09 — Calidad y Definition of Done

> **Semana:** 10 · **Responsable:** Maria Paz Ugalde Araya· **Estado:** Borrador . **Jira:** API-29


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

Lista de condiciones que **cualquier** elemento del Sprint debe cumplir para pasar a *Listo* en Jira. Desarrolla la regla de «Listo» de la [Sección 05](05-backlog-sprint-backlog.md) y la regla de la columna final del tablero de la [Sección 10](10-comunicacion-responsabilidades.md), donde la misma columna aparece con el nombre *Hecho*.

Si una sola condición no se cumple, la tarjeta no pasa a *Listo*: vuelve a *En progreso* y el motivo se anota en un comentario del ticket.

### A. Toda historia (producto, habilitadora o tarea del Expediente)

- [ ] **Criterios de aceptación cumplidos:** cada criterio del ticket se comprobó uno por uno (los de las historias de usuario están en la [Sección 06](06-alcance-product-backlog.md)). _Evidencia: comentario en Jira indicando cómo se comprobó cada uno._
- [ ] **Caso de prueba aprobado:** la historia tiene al menos un caso de prueba en la tabla de esta sección y su resultado quedó como *Aprobado*. _Evidencia: fila de la historia en el registro de ejecución._
- [ ] **Revisión por pares:** el otro integrante revisó el trabajo (lee el documento o prueba el código) mientras la tarjeta estaba en *En revisión*. _Evidencia: comentario de revisión en Jira._
- [ ] **Subido al repositorio:** el resultado está en `main` con un commit que incluye la clave del ticket en el mensaje. _Evidencia: commit visible en GitHub._
- [ ] **Sin errores abiertos que bloqueen:** no hay tickets de tipo *Error* abiertos asociados a la historia que afecten la integridad o la pérdida de datos. Un error menor puede quedar abierto solo si el Product Owner lo acepta y queda registrado en Jira. _Evidencia: filtro de errores de la historia en Jira._
- [ ] **Sección del Expediente actualizada:** si la historia cambió el alcance, un criterio de aceptación o un resultado de prueba, la sección correspondiente del Expediente se actualizó en el mismo Sprint. _Evidencia: commit de la sección._

### B. Además, si la historia incluye código

- [ ] **Probado en ambas máquinas:** el caso de prueba se ejecutó y pasó en la máquina de cada integrante. _Evidencia: columnas de ambas máquinas del registro de ejecución._
- [ ] **Probado con carpetas de ejemplo:** se usaron las carpetas de ejemplo definidas en esta sección, nunca datos reales. _Evidencia: el caso de prueba nombra la carpeta usada._
- [ ] **Log funcionando:** la operación escribe su entrada en el log con fecha, hora y resultado, también cuando falla. _Evidencia: línea del log en la captura de la prueba._
- [ ] **Mensajes claros:** los errores indican la causa y qué puede hacer el usuario. _Evidencia: captura del mensaje._
- [ ] **Se puede ejecutar desde cero:** las instrucciones del repositorio permiten que el otro integrante ejecute la historia sin ayuda. _Evidencia: la ejecución en la segunda máquina se hizo siguiendo esas instrucciones._
- [ ] **Sin datos sensibles en el repositorio:** no hay credenciales, rutas personales ni información real en el código, el log de ejemplo o las carpetas de ejemplo. _Evidencia: revisión del commit por el otro integrante._

### C. Además, si es una tarea del Expediente

- [ ] **Sin pendientes visibles:** la sección no contiene marcas de «_Pendiente_» ni comentarios `PENDIENTE` en el apartado que se entrega.
- [ ] **Coherente con el resto del Expediente:** los identificadores (HU, HB, API, R) y los enlaces entre secciones coinciden con los de las demás secciones.

## Estrategia de validación

Validar es comprobar que lo construido cumple los criterios de aceptación de la [Sección 06](06-alcance-product-backlog.md) y las metas de calidad de esta sección. Se usan tres niveles. Cada uno cubre algo que el anterior no alcanza.

| Nivel | Qué comprueba | Cómo | Cuándo | Quién | Evidencia |
|---|---|---|---|---|---|
| **1. Pruebas automáticas** | La lógica de respaldo, registro y restauración (`src/respaldo/nucleo.py`). No prueban la ventana. | `python -m unittest discover -s tests -v` desde la raíz. Son 9 pruebas en `tests/test_nucleo.py`. | Antes de mover la tarjeta a *En revisión*, cuando la revisa el compañero y antes de la Demo. | Quien desarrolla y quien revisa | Salida con `OK` en el ticket |
| **2. Prueba manual con el guion de la Demo** | La ventana de punta a punta: botones, barra de avance, mensajes, aviso de archivos repetidos y log. | Los 7 pasos del guion de la [Sección 11](11-decisiones-cambios-evidencias.md#preparación-de-la-demo), con las carpetas `demo-origen` y `demo-destino`. | Ensayo completo el lunes 23 de noviembre en las dos máquinas, y de nuevo antes de la Demo. | Xavier y María Paz, cada uno en su máquina | Tabla de resultados de abajo y capturas en `evidencias/` |
| **3. Revisión en la Sprint Review** | Que cada historia cumple sus criterios de aceptación con el producto funcionando. | Se muestra HU-01 a HU-04 y se revisa cada criterio de la Sección 06. El Product Owner acepta o devuelve cada historia. | Martes 24 de noviembre de 2026, al cierre del Sprint 2. | Ambos integrantes; decide el Product Owner | Acta del Sprint 2 en `scrum/sprints/sprint-02/` y captura del tablero |

### Qué valida cada historia

| Historia | Pruebas automáticas | Pasos de la Demo | Solo se comprueba a mano |
|---|---|---|---|
| HU-01 · Configurar origen y destino | `test_valida_rutas`, `test_guarda_y_carga_configuracion` | 2 | Elegir las carpetas en la ventana y ver la configuración guardada al volver a abrir el programa |
| HU-02 · Respaldo manual | `test_respaldo_copia_todo_con_subcarpetas`, `test_respaldos_no_se_sobrescriben`, `test_un_archivo_con_error_no_detiene_el_respaldo` | 3 | Que el usuario vea que el proceso está en curso |
| HU-03 · Ver el resultado | `test_log_registra_cada_respaldo`, `test_origen_invalido_falla_sin_excepcion_y_queda_en_log` | 3 y 4 | El resumen en pantalla (archivos, tamaño y duración) |
| HU-04 · Restaurar un respaldo completo | `test_restauracion_completa_recupera_lo_borrado`, `test_restaurar_pide_confirmacion_si_hay_archivos_iguales` | 5 y 6 | La lista de respaldos ordenada por fecha y el aviso en pantalla antes de reemplazar |

### Cómo se valida cada criterio de calidad

| Criterio | Cómo se valida en esta entrega |
|---|---|
| Confiabilidad del respaldo | Pruebas automáticas de respaldo con archivo con error y origen inválido, y revisión del log en el paso 4 de la Demo. |
| Integridad | Las pruebas comparan byte por byte lo copiado con el original y comprueban lo restaurado. La verificación con huellas hash (HU-08) quedó fuera por CR-03. |
| Usabilidad | Prueba con usuarios de la tabla de criterios, hecha en la Sprint Review con una persona que no sea del equipo. [PENDIENTE: persona de prueba.] |
| Compatibilidad | Las pruebas y el guion se ejecutan en la máquina de cada integrante. |

### Resultado de la prueba manual

Se llena durante el ensayo del lunes 23 de noviembre con *Pasó* o *No pasó* y, si no pasó, el número del ticket de Error.

| Paso de la Demo | Historia | Máquina de Xavier | Máquina de María Paz |
|---|---|---|---|
| 1. Abrir la aplicación | — | [PENDIENTE] | [PENDIENTE] |
| 2. Configurar origen y destino | HU-01 | [PENDIENTE] | [PENDIENTE] |
| 3. Respaldar ahora | HU-02 | [PENDIENTE] | [PENDIENTE] |
| 4. Ver log | HU-03 | [PENDIENTE] | [PENDIENTE] |
| 5. Borrar `clientes.txt` | — | [PENDIENTE] | [PENDIENTE] |
| 6. Restaurar el respaldo | HU-04 | [PENDIENTE] | [PENDIENTE] |
| 7. Correr las pruebas automáticas | — | [PENDIENTE] | [PENDIENTE] |

### Si una validación falla

- **Una prueba automática falla:** la tarjeta vuelve a *En progreso*, se registra un Error en Jira, se corrige y se corren de nuevo todas las pruebas, no solo la que falló.
- **Un paso de la prueba manual falla:** se registra un Error con el paso, el sistema operativo y una captura. La historia no pasa a *Hecho* hasta que el paso funcione en las dos máquinas.
- **Una historia no se acepta en la Sprint Review:** el Product Owner la devuelve al backlog y lo anota en el acta, como se hizo en el Sprint 1.
- **Algo falla durante la exposición:** se muestran las pruebas automáticas y el log.
