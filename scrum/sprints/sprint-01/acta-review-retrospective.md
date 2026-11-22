# Acta de Sprint Review y Sprint Retrospective · Sprint 1

> **Proyecto:** Sistema de Respaldo y Recuperación de Información · **Jira:** API-26 · **Elaborada por:** [PENDIENTE]

## Parte 1. Sprint Review

### Datos de la reunión

| Campo | Detalle |
|---|---|
| Sprint | Sprint 1 ("API Sprint 1" en Jira), del 1 al 10 de noviembre de 2026 |
| Fecha de la Review | [PENDIENTE] |
| Duración | [PENDIENTE] |
| Medio | [PENDIENTE] (presencial, Meet, etc.) |
| Equipo | Xavier Fernández Zúñiga (Product Owner y Developer), María Paz Ugalde Araya (Scrum Master y Developer) |
| Interesados invitados | [PENDIENTE] (por ejemplo, el docente del curso) |

### Sprint Goal

> Dejar lista la base técnica del proyecto y comprobar que el sistema puede copiar una carpeta a un destino y registrar el resultado.

**¿Se cumplió?** No.

No se decidió la tecnología del producto (API-8). Sin esa decisión no se pudo preparar el entorno (API-9) ni hacer la prueba de copiar una carpeta (API-11). Al cierre del Sprint la carpeta `src/` del repositorio sigue vacía.

Lo que sí avanzó fue el tablero de Jira y el Expediente del Proyecto.

### Qué se mostró y qué cumple la regla de Hecho

La Definition of Done formal todavía no está escrita (Sección 09, en curso). Para esta revisión se usó la regla para mover una tarjeta a *Hecho* de la Sección 10:

1. Cumple sus criterios de aceptación.
2. Fue revisada por el otro integrante.
3. Está subida al repositorio con un commit.
4. Si es código, se probó en las dos máquinas.

**Historias de usuario del producto (HU-01 a HU-09):** ninguna se trabajó. Todas siguen en *Por hacer*. No hubo un Incremento de producto que mostrar.

**Elementos del Sprint Backlog:**

| Jira | Elemento | Estado en Jira | Evidencia en el repositorio | ¿Cumple la regla? | Decisión del PO |
|---|---|---|---|---|---|
| API-8 | HB-01 · Definir la tecnología | Por hacer | Ninguna | No | Pasa al Sprint 2 (API-37) |
| API-9 | HB-02 · Entorno y estructura en `src/` | Por hacer | `src/` vacío | No | Pasa al Sprint 2 |
| API-10 | HB-03 · Configurar el tablero de Jira | Listo | Tablero con 4 columnas, WIP 2 y Sprint 1 iniciado el 1 de noviembre. Falta la captura en `evidencias/` | En parte | Se acepta la configuración. La captura pasa a API-44 |
| API-11 | HB-04 · Prueba técnica de copia | Listo | No hay código | No | No se acepta. Vuelve a *Por hacer* y se trabaja con API-37 |
| API-21 | Correcciones de las Secciones 00 y 01 | Listo | Roles definidos en la 00 (commit `24430de`). Falta el carné y los errores de la 01 | En parte | Lo pendiente pasa a API-44 |
| API-24 | Sección 05 · Backlog y seguimiento | En curso | Commit `7e0e409`. Falta la captura del tablero | En parte | Se cierra cuando esté la captura |
| API-25 | Sección 06 · Alcance y Product Backlog | Listo | 6 commits del 10 y 11 de noviembre | Sí, aunque no pasó por *En revisión* | Aceptado |
| API-26 | Eventos Scrum del Sprint 1 | Por hacer | Esta acta | — | Se cierra con esta acta |
| API-28 | Sección 08 · Riesgos | Listo | Matriz con 9 riesgos y plan de adquisiciones. El apartado de respuestas a los riesgos está vacío | No | No se acepta. Lo que falta pasa a API-42 |
| API-30 | Sección 10 · Comunicación y tablero | Listo | Commit `6730d9f` | Sí, aunque no pasó por *En revisión* | Aceptado |

**Trabajo terminado fuera del Sprint Backlog:** Sección 07 de planificación y costos (API-27, commit `90e9be0`) y avance de la Sección 09 de calidad (API-29, en curso). Las Secciones 03 y 04 (API-22 y API-23) se terminaron antes de iniciar el Sprint, el 28 de octubre.

**Resumen:** de 10 elementos del Sprint, 2 se aceptan completos, 3 se aceptan en parte y 5 no se aceptan. El trabajo de producto quedó en cero.

### Retroalimentación de los interesados

| Interesado | Comentario | Qué se hace con el comentario |
|---|---|---|
| [PENDIENTE] | [PENDIENTE] | [PENDIENTE] |

### Cambios al Product Backlog acordados

> Decisiones del Product Owner. [PENDIENTE: confirmarlas en la Review y ajustar si se decide algo distinto.]

1. **Reducir el alcance de la entrega (CR-03).** La entrega se enfoca en respaldar y recuperar: HU-01, HU-02, HU-03 y HU-04 (13 de 32 puntos). HU-05 a HU-09 quedan diferidas y solo se trabajan si sobra tiempo. Detalle en la [Sección 11](../../../expediente/11-decisiones-cambios-evidencias.md).
2. **API-11 vuelve a *Por hacer*.** Se marcó como lista sin tener código.
3. **Nuevos elementos:** las tres acciones de mejora de la Retrospective (API-36, API-37 y API-38) y los pendientes del Expediente (API-39 a API-44).
4. **Orden para el Sprint 2:** primero la base técnica (API-37, API-8, API-9, API-11) y luego HU-01 a HU-04. Las secciones del Expediente se trabajan en paralelo.

### Estado del release frente al Cronograma de Entregas

Comparación con el cronograma de la [Sección 07](../../../expediente/07-planificacion-estimaciones-costos.md):

| Sprint | Lo planificado | Lo real al 22 de noviembre |
|---|---|---|
| Sprint 1 | Base técnica y prueba de copia | No se logró |
| Sprint 2 (hasta 10 nov) | HU-01 a HU-03: respaldo manual (8 puntos) | No se empezó |
| Sprint 3 (hasta 17 nov) | HU-04 y HU-05: restauración (8 puntos) | No se empezó |

- **Producto:** según el plan, para el 17 de noviembre debían estar terminados 16 de 32 puntos. Hay 0. El proyecto va unos dos Sprints atrasado.
- **Expediente:** Secciones 00 a 07 y 10 subidas. La 08 y la 09 están incompletas. La 11 y la 12 no se han empezado.
- **Entrega:** Semana 11, el [PENDIENTE: fecha exacta]. Con el cambio CR-03, el objetivo de la entrega es tener HU-01 a HU-04 funcionando y el Expediente completo.

## Parte 2. Sprint Retrospective

### Datos

| Campo | Detalle |
|---|---|
| Fecha y duración | [PENDIENTE] |
| Facilitadora | María Paz Ugalde Araya (Scrum Master) |
| Participantes | Xavier Fernández Zúñiga, María Paz Ugalde Araya |
| Formato | Start / Stop / Continue |

Se revisa cómo trabajamos como equipo, no a las personas. Cada punto tiene su evidencia en Jira o en el repositorio.

### Continue: lo que funcionó

| Qué funcionó | Evidencia |
|---|---|
| El tablero de Jira quedó listo desde el primer día del Sprint | Sprint 1 creado y en curso el 1 de noviembre, con columnas y límite WIP |
| Los tickets tenían descripción y criterios de aceptación, y eso hizo más fácil saber qué entregar | Los 28 tickets de trabajo creados el 28 de octubre tienen criterios de aceptación |
| El Expediente avanzó bastante | Secciones 06, 07, 08 y 09 entre el 10 y el 14 de noviembre. Sección 10 el 6 de noviembre |
| El reparto de secciones por persona estuvo claro | Cada ticket del Expediente tiene un responsable |

### Stop: lo que no funcionó

| Qué no funcionó | Evidencia |
|---|---|
| Se movieron tarjetas a *Listo* sin cumplir sus criterios y sin pasar por *En revisión* | API-11 en *Listo* sin código. API-10 sin captura. API-28 sin plan de mitigación. La columna *En revisión* casi no se usó |
| La decisión técnica se quedó sin tomar todo el Sprint y bloqueó el objetivo | API-8 estuvo en *Por hacer* del 1 al 10 de noviembre |
| El trabajo se juntó al final | Del 1 al 9 de noviembre hubo 1 commit. Los otros 5 commits del Sprint llegaron el 10 de noviembre, último día |
| Los commits no se pueden rastrear hasta su tarea | Desde el 28 de octubre, 13 de 17 commits no llevan la clave de Jira |
| El Sprint no se cerró en su fecha | El Sprint venció el 10 de noviembre y seguía abierto el 22 de noviembre |
| [PENDIENTE: ¿se hizo el Daily? Revisar el chat del equipo] | [PENDIENTE] |

### Start: lo que vamos a empezar a hacer

Las acciones de mejora de la tabla siguiente.

### Seguimiento de las acciones del Sprint anterior

No aplica. Es el primer Sprint del proyecto y no había acciones anteriores. Las acciones de esta Retrospective se revisan en la del Sprint 2.

### Acciones de mejora

| # | Acción | Dueño | Fecha | Cómo se verifica | Ticket |
|---|---|---|---|---|---|
| 1 | Toda tarjeta pasa por *En revisión*. El otro integrante la revisa contra sus criterios y deja el comentario "Revisado" antes de moverla a *Hecho* | María Paz (Scrum Master) | Desde el inicio del Sprint 2 | En la Retrospective del Sprint 2, todas las tarjetas en *Hecho* tienen el comentario "Revisado" | API-36 |
| 2 | Hacer juntos una sesión técnica de 2 horas para decidir la tecnología y subir a `src/` un esqueleto que se pueda ejecutar | Xavier (Product Owner) | 24 de noviembre de 2026 | API-8 y API-9 en *Hecho* y un commit con código en `src/` antes de esa fecha | API-37 |
| 3 | Cada commit lleva la clave del ticket y se sube el mismo día en que se termina el trabajo | Xavier | Desde el inicio del Sprint 2 | Al cierre del Sprint 2, `git log` muestra la clave `API-` en todos los commits del Sprint | API-38 |

### Acciones incorporadas al Sprint Backlog del Sprint 2

Las tres acciones ya están creadas en Jira con la etiqueta `retro-s1` y `sprint-2`: API-36, API-37 y API-38. Entran al Sprint 2 junto con API-8, API-9, API-11, HU-01 a HU-04 y los pendientes del Expediente (API-39 a API-44).

[PENDIENTE: cerrar el Sprint 1 en Jira, crear el Sprint 2 con sus fechas y mover estos tickets.]

## Aprobación

| Rol | Nombre | Aprobado |
|---|---|---|
| Product Owner | Xavier Fernández Zúñiga | [PENDIENTE] |
| Scrum Master | María Paz Ugalde Araya | [PENDIENTE] |
