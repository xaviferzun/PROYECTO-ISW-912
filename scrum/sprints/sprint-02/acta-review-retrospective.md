# Acta de Sprint Review y Sprint Retrospective · Sprint 2

> **Proyecto:** Sistema de Respaldo y Recuperación de Información · **Jira:** API-26 · **Elaborada por:** Xavier Fernández Zúñiga (Product Owner)

## Parte 1. Sprint Review

### Datos

| Campo | Detalle |
|---|---|
| Sprint | Sprint 2 ("API Sprint 2" en Jira), del 18 al 24 de noviembre de 2026 |
| Fecha de la Review | 24 de noviembre de 2026 |
| Formato | El Product Owner revisó cada elemento contra sus criterios de aceptación y la Definition of Done de la [Sección 09](../../../expediente/09-calidad-dod.md), con la app funcionando en su máquina |
| Participantes | Xavier Fernández Zúñiga (Product Owner y Developer). María Paz Ugalde Araya no estuvo disponible ese día |
| Interesados | La Review con el docente es la exposición del 25 de noviembre. Sus comentarios se registran en la [Sección 12](../../../expediente/12-incremento-final-cierre.md) |

### Sprint Goal

> Entregar un MVP que permita configurar, respaldar y restaurar una carpeta con registro en log (HU-01 a HU-04), y completar el Expediente para la entrega final.

**¿Se cumplió?** Sí.

El MVP funciona: se probaron los 7 pasos de la Demo y las 9 pruebas automáticas pasan ([captura](../../../evidencias/demo-mvp-2026-11-24.png)). Las Secciones 00 a 12 del Expediente están completas.

### Qué se revisó

**Producto**

| Jira | Elemento | Puntos | Resultado | Evidencia |
|---|---|---:|---|---|
| API-8 | HB-01 · Definir la tecnología | 2 | Aceptado | D-03 en la Sección 11 |
| API-9 | HB-02 · Entorno y estructura de `src/` | 2 | Aceptado | Commit `2f4fdbf` |
| API-11 | HB-04 · Prueba técnica de copia y registro | 3 | Aceptado | Commit `6f06c62` |
| API-12 | HU-01 · Configurar origen y destino | 3 | Aceptado | Paso 2 de la Demo y 2 pruebas |
| API-13 | HU-02 · Respaldo manual | 3 | Aceptado | Paso 3 de la Demo y 3 pruebas |
| API-14 | HU-03 · Ver el resultado | 2 | Aceptado | Paso 4 de la Demo y 2 pruebas |
| API-15 | HU-04 · Restaurar un respaldo completo | 5 | Aceptado | Pasos 5 y 6 de la Demo y 2 pruebas |

**Total:** 20 puntos terminados (7 de habilitadoras que venían del Sprint 1 y 13 de historias de usuario). En el Sprint 1 fueron 0.

**Expediente**

| Jira | Elemento | Responsable | Resultado |
|---|---|---|---|
| API-24, API-43 | Secciones 04, 05, 06 y 07 con las fechas reales y el alcance del MVP | Xavier | Aceptado |
| API-26 | Acta del Sprint 1 y esta acta | Xavier | Aceptado |
| API-39, API-31 | Sección 11: cambios, decisiones, evidencias y guion de la Demo | Xavier | Aceptado |
| API-40 | Sección 10: Working Agreements | Xavier | Aceptado |
| API-41 | Historial de cambios | Xavier | Aceptado |
| API-42 | Sección 08: respuestas a los riesgos, mapa de calor y plan de salida | María Paz | Aceptado |
| API-29 | Sección 09: Definition of Done, validación y resultado de la prueba manual | María Paz y Xavier | Aceptado |
| API-45 | Sección 10: matriz RACI | María Paz | Aceptado |
| API-44 | Correcciones en 00 y 01 | María Paz y Xavier | Aceptado. Se quitó el carné de la portada en lugar de completarlo |
| API-32 | Sección 12: incremento final, informe y lecciones aprendidas | Xavier | Aceptado |
| API-33 | Preparar la Demo | Xavier | Aceptado. Ensayo hecho el 24 de noviembre |

### Cambios al Product Backlog

No hubo cambios nuevos. HU-05 a HU-09 siguen diferidas por CR-03 y quedan en el Product Backlog para una versión futura, en el orden de la Sección 12.

## Parte 2. Sprint Retrospective

### Datos

| Campo | Detalle |
|---|---|
| Fecha | 24 de noviembre de 2026 |
| Participantes | Xavier Fernández Zúñiga. María Paz no estuvo disponible; puede agregar sus puntos en el ticket API-36 |
| Formato | Start / Stop / Continue, con evidencia del repositorio y de Jira |

### Seguimiento de las acciones del Sprint 1

| Acción | Ticket | ¿Se cumplió? | Evidencia |
|---|---|---|---|
| Toda tarjeta pasa por *En revisión* y el otro integrante la revisa antes de *Hecho* | API-36 | En parte | Las tarjetas de Xavier pasaron por *En revisión* el 22 de noviembre. Las de María Paz pasaron a *Listo* sin comentario de revisión, y las de Xavier no recibieron revisión de María Paz antes de la entrega |
| Sesión técnica para decidir la tecnología y subir el esqueleto a `src/` | API-37 | Sí | Tecnología decidida y esqueleto subido el 22 de noviembre (commit `2f4fdbf`) |
| Cada commit lleva la clave de Jira y se sube el mismo día | API-38 | Sí | Los 17 commits del Sprint 2 empiezan con `API-` |

### Continue: lo que funcionó

| Qué funcionó | Evidencia |
|---|---|
| Reducir el alcance a un MVP permitió entregar un producto que funciona | 20 puntos terminados contra 0 del Sprint 1 |
| Las tareas quedaron bien repartidas por ticket | María Paz: Secciones 08, 09 y RACI. Xavier: código, 04 a 07, 11 y 12 |
| La clave de Jira en los commits | Se puede seguir cada cambio hasta su tarea |
| Los Working Agreements y la RACI dejaron claro quién decide y quién hace cada cosa | Sección 10 |

### Stop: lo que no funcionó

| Qué no funcionó | Evidencia |
|---|---|
| El trabajo se volvió a juntar al final del Sprint | Todo el código se subió el 22 de noviembre. Las secciones de María Paz se subieron esa misma noche, entre las 11:28 y las 11:51 p. m. |
| Hubo tarjetas en *Listo* sin la revisión del compañero | API-29, API-42, API-44 y API-45 pasaron a *Listo* sin comentario "Revisado" |
| El Sprint se creó tarde en Jira | El Sprint 2 empezó el 18 de noviembre, pero se creó en Jira el 22 |
| El producto se probó en una sola máquina | Sección 09: la columna de María Paz quedó como "No se probó" |

### Start: lo que haríamos en un siguiente Sprint

| # | Acción | Dueño | Cómo se verifica |
|---|---|---|---|
| 1 | Configurar Jira para que una tarjeta solo pueda pasar a *Hecho* desde *En revisión* | María Paz (Scrum Master) | El flujo del tablero no permite saltarse *En revisión* |
| 2 | Crear el Sprint en Jira el mismo día del Sprint Planning | María Paz | Fecha de creación del Sprint igual a su fecha de inicio |
| 3 | Probar el producto en las dos máquinas antes de la Review | Xavier y María Paz | Las dos columnas de la prueba manual llenas en la Sección 09 |
| 4 | Subir avances a mitad del Sprint, no solo al final | Ambos | `git log` con commits en al menos tres días distintos del Sprint |

Como este es el último Sprint del curso, estas acciones quedan como recomendación para una versión futura del producto.

## Cierre del Sprint

El Sprint 2 se cerró en Jira el 24 de noviembre de 2026.

| Rol | Nombre | Aprobado |
|---|---|---|
| Product Owner | Xavier Fernández Zúñiga | Sí, 24 de noviembre de 2026 |
| Scrum Master | María Paz Ugalde Araya | Sí, 24 de noviembre de 2026 |
