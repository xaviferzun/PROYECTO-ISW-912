# Sección 10 — Comunicación y responsabilidades del equipo

> **Semana:** 7 (Plan de Comunicaciones y Tablero) · 10 (Working Agreements) · 11 (RACI) · **Responsable:** Xavier Fernández Zúñiga · **Estado:** Borrador · **Jira:** API-30

## Plan de Comunicaciones

El equipo tiene dos integrantes, por lo que existe un solo canal interno (2 × 1 / 2 = 1). El riesgo no es la cantidad de canales sino que la información se quede en la cabeza de una persona o se pierda en mensajes sueltos; por eso el plan define **qué** se comunica, **a quién**, **cuándo** y **por dónde**.

### Interesados y comunicación que necesitan

Basado en el análisis de la [Sección 03](03-interesados.md).

| Interesado | Poder / Interés | Qué información necesita | Frecuencia / evento | Canal | Responsable |
|---|---|---|---|---|---|
| Docente evaluador | 5 / 5 · Gestionar de cerca | Avance del Expediente y del producto, cumplimiento de entregables | Semanal (clase) y en cada entrega | Repositorio GitHub (commits), Jira, presentación en clase | Ambos |
| Equipo de desarrollo | 4 / 5 · Gestionar de cerca | Qué hace cada uno, bloqueos, decisiones técnicas | Daily Scrum (lunes a viernes) y eventos de cada Sprint | WhatsApp (Daily), tablero de Jira, reunión virtual (Meet) | Scrum Master |
| Institución / organización usuaria | 5 / 4 · Gestionar de cerca | Valor del producto, avance en hitos, decisiones que la afecten | Al cierre de cada Sprint (Sprint Review) | Demostración y resumen escrito | Product Owner |
| Soporte TI | 4 / 5 · Gestionar de cerca | Funcionamiento de alertas, historial y restauración | En las Sprint Review de los Sprints 3 a 5 | Demostración y retroalimentación | Product Owner |
| Equipo de seguridad | 5 / 3 · Mantener satisfecho | Cómo se protegen los respaldos y los datos personales | Cuando se defina la protección de los respaldos | Consulta puntual (correo o reunión) | Product Owner |
| Proveedor de nube | 4 / 2 · Mantener satisfecho | Requisitos de uso y costos, si se usa la nube como destino | Solo si se decide usar un servicio de nube | Documentación del proveedor | Scrum Master |
| Estudiantes, trabajadores y usuarios en general | 2 / 5 · Mantener informados | Cómo usar la herramienta; recoger su opinión | Pruebas de usabilidad en las Sprint Review | Guía de uso de una página y encuesta corta | Product Owner |

### Eventos de comunicación del equipo

| Evento | Cuándo | Duración | Participantes | Propósito | Registro |
|---|---|---|---|---|---|
| Sprint Planning | Miércoles, al inicio del Sprint (en o después de clase) | 30 min | Equipo | Elegir el trabajo del Sprint y definir el Sprint Goal | Jira (Sprint creado) y `scrum/sprints/sprint-XX/planning.md` |
| Daily Scrum | Lunes a viernes | Mensaje corto | Equipo | Qué avancé, qué haré, qué me bloquea | Mensaje en WhatsApp + tarjetas actualizadas en Jira |
| Sprint Review | Martes, al cierre del Sprint | 20 min | Equipo e interesados disponibles | Mostrar lo terminado y recoger retroalimentación | `scrum/sprints/sprint-XX/review.md` + captura del tablero |
| Sprint Retrospective | Martes, después de la Review | 15 min | Solo el equipo | Qué funcionó, qué mejorar y una acción concreta | `scrum/sprints/sprint-XX/retrospectiva.md` |
| Revisión con el docente | Cada clase (miércoles) | Según la clase | Equipo y docente | Validar el avance del Expediente y resolver dudas | Ajustes en el Expediente con su commit |

### Reglas de comunicación del equipo

| Regla | Detalle |
|---|---|
| Dónde se decide | Las decisiones del proyecto se toman en reunión o por WhatsApp, pero **solo cuentan cuando se registran**: en la tarea de Jira correspondiente y, si son importantes, en la [Sección 11](11-decisiones-cambios-evidencias.md). |
| Tiempo de respuesta | Mensajes del equipo: en menos de 24 horas. Revisión de una tarjeta en *En revisión*: en menos de 48 horas. |
| Fuente única del estado del trabajo | El tablero de Jira. Si algo no está en Jira, no está planificado. |
| Fuente única de los entregables | El repositorio de GitHub. Cada commit lleva la clave del ticket (ej. `API-28 docs(expediente): ...`). |
| Archivos compartidos | Nunca editar el mismo archivo al mismo tiempo; siempre `git pull` antes de editar. |

### Escalamiento de impedimentos y conflictos

1. **Impedimento** (algo bloquea una tarea): quien lo tiene lo avisa en el Daily y marca la tarjeta en Jira con la bandera *Impediment*.
2. Si no se resuelve en **48 horas**, el **Scrum Master** propone una solución o reparte el trabajo de otra forma.
3. Si afecta el alcance o una fecha de entrega, el **Product Owner** decide qué se ajusta en el backlog y se registra como cambio en la Sección 11.
4. Si el equipo no logra resolverlo (por ejemplo, un desacuerdo sobre el alcance o una duda sobre un entregable), se consulta al **docente** en la siguiente clase o por correo.

## Tablero de Trabajo

**Herramienta:** Jira (plan gratuito), proyecto `API`, tablero Scrum.
**Enlace:** https://xaviferzun-1784755725349.atlassian.net/jira/software/projects/API/boards/2

### Columnas y su significado

| Columna | Significado | Límite WIP |
|---|---|---|
| Por hacer | Trabajo del Sprint que nadie ha empezado. | — |
| En progreso | Alguien lo está trabajando; la tarjeta muestra su responsable. | 2 |
| En revisión | El responsable lo terminó y el otro integrante lo revisa (lee la sección o prueba el código). | 2 |
| Hecho | Cumple la regla de "Hecho" (abajo). | — |

### Justificación del límite WIP

- **En progreso = 2:** una tarea por persona a la vez. Así se termina antes de empezar algo nuevo y se evita tener muchas tareas a medias.
- **En revisión = 2:** si ya hay dos cosas esperando revisión, nadie empieza trabajo nuevo hasta revisarlas. Esto obliga a que ambos revisen el trabajo del otro, que es nuestra forma de aseguramiento de calidad (revisión por pares).

### Regla para mover una tarjeta a "Hecho"

Una tarjeta pasa a *Hecho* solo si:

- [ ] Cumple todos sus criterios de aceptación.
- [ ] Fue revisada por el otro integrante.
- [ ] Su resultado está subido al repositorio con un commit que incluye la clave del ticket.
- [ ] Si es código: se probó y funciona en la máquina de ambos integrantes.

Esta regla es la base de la Definition of Done que se detallará en la Sección 09.

### Estado del tablero — Sprint 1

El Sprint 1 (1 al 10 de noviembre) tiene cargadas las historias habilitadoras (HB-01 a HB-04) y las tareas del Expediente de esta etapa, cada una con su responsable visible.

![Tablero de Jira — Sprint 1](../evidencias/jira-sprint-01.png)

## Matriz de responsabilidades (RACI)

Define quién hace, quién responde y a quién se consulta o informa en cada actividad. Se basa en los roles Scrum de la [Sección 00](00-portada-equipo.md), en el reparto del Sprint Backlog de la [Sección 05](05-backlog-sprint-backlog.md) y en los responsables de cada sección del Expediente.

| Letra | Significado |
|---|---|
| **R** (Responsable) | Hace el trabajo. Puede haber más de una persona. |
| **A** (Aprobador) | Responde por el resultado y decide. **Hay una sola A por actividad.** Se escribe **A/R** cuando quien responde también hace el trabajo. |
| **C** (Consultado) | Da su opinión antes de cerrar la actividad. |
| **I** (Informado) | Se entera del resultado. |
| — | No participa. |

| # | Actividad | Xavier (Product Owner) | María Paz (Scrum Master) | Docente |
|---|---|:---:|:---:|:---:|
| 1 | Mantener el Product Backlog en Jira: orden, estimación y criterios de aceptación | A | R | I |
| 2 | Sprint Planning: Sprint Goal y Sprint Backlog | R | A | — |
| 3 | Daily Scrum por WhatsApp | R | A/R | — |
| 4 | Desarrollo del producto en `src/` y `tests/` | A/R | C | I |
| 5 | Revisión por pares y comentario «Revisado» en cada tarjeta | R | A/R | — |
| 6 | Pruebas automáticas y prueba manual en cada máquina (Sección 09) | R | A/R | — |
| 7 | Sprint Review: mostrar lo terminado y aceptar o devolver cada historia | A/R | R | I |
| 8 | Sprint Retrospective y acciones de mejora | R | A/R | — |
| 9 | Gestión de riesgos y problemas (Sección 08) | R | A/R | — |
| 10 | Decisiones y control de cambios (Sección 11) | A/R | C | C |
| 11 | Tablero de Jira: tarjetas, impedimentos y cierre de cada Sprint a tiempo | C | A/R | I |
| 12 | Secciones 00, 01, 02, 06, 07, 08 y 09 del Expediente | C | A/R | C |
| 13 | Secciones 03, 04, 05, 10 y 11 del Expediente | A/R | C | C |
| 14 | Sección 12 e Informe Final | C | A/R | I |
| 15 | Actas de los eventos Scrum, evidencias e historial de cambios | A/R | C | I |
| 16 | Preparación y presentación de la Demo | A/R | R | I |
| 17 | Defensa oral | A/R | R | I |

### Cómo se leyó la matriz

- **Producto:** el Product Owner responde por el backlog, el desarrollo, la Review, los cambios y la Demo. Todas las historias del Sprint 2 están asignadas a Xavier en la [Sección 05](05-backlog-sprint-backlog.md), por eso María Paz aparece como consultada en el desarrollo y como revisora en la actividad 5.
- **Proceso:** la Scrum Master responde porque los eventos se hagan, la revisión por pares se cumpla y los Sprints se cierren a tiempo. Son los puntos que fallaron en el Sprint 1 ([acta](../scrum/sprints/sprint-01/acta-review-retrospective.md)).
- **Expediente:** cada sección la responde quien aparece como responsable en su encabezado, y la otra persona la revisa antes de pasar la tarjeta a *Hecho*. Por eso queda como C.
- **Docente:** evalúa el trabajo. En la matriz aparece como informado de lo que recibe (commits, Jira, Review, Demo) y como consultado en el Expediente, que se revisa con él cada clase y en los cambios que mueven una fecha de entrega.
- **Sección 12:** el encabezado de esa sección dice «por definir». Se asignó a María Paz como propuesta. [PENDIENTE: confirmar quién responde por la Sección 12 y el Informe Final.]
- **Desacuerdos:** si dos personas no se ponen de acuerdo sobre quién responde por una actividad, se aplican los Working Agreements 8 y 9 de esta sección.

## Working Agreements

> **Versión:** 1 · **Acordados el:** 22 de noviembre de 2026 · **Próxima revisión:** Retrospective del Sprint 2 · **Jira:** API-40

Son las reglas con las que trabajamos los dos. Salen del Plan de Comunicaciones de esta sección y de lo que aprendimos en la Retrospective del Sprint 1. Cada regla se puede revisar: o se cumplió o no se cumplió.

**Puño de cinco:** cada integrante vota con 0 a 5 dedos qué tan de acuerdo está con la regla. Si alguien vota 2 o menos, se conversa y se ajusta la regla antes de aprobarla.

| # | Tema | Acuerdo | Cómo se verifica | Puño de cinco (Xavier / María Paz) |
|---|---|---|---|---|
| 1 | Comunicación | Usamos el grupo de WhatsApp del proyecto como canal oficial. Lo que se decida ahí lo anotamos en el ticket de Jira ese mismo día | Cada decisión tiene un comentario en su ticket con la fecha | 5 / 5 |
| 2 | Comunicación | Respondemos los mensajes del equipo en menos de 24 horas | Revisión del chat en la Retrospective | 5 / 5 |
| 3 | Ritmo | Hacemos el Daily por WhatsApp los lunes, miércoles y viernes antes de las 9 p. m.: qué hice, qué voy a hacer y qué me bloquea | Hay tres mensajes de Daily por persona cada semana | 5 / 5 |
| 4 | Ritmo | En el Sprint Planning cada uno dice cuántas horas puede dar esa semana y qué días no va a estar disponible | Queda anotado en el `planning.md` de cada Sprint | 5 / 5 |
| 5 | Calidad | Toda tarjeta pasa por *En revisión*. El otro integrante la revisa en menos de 48 horas y deja el comentario "Revisado" antes de moverla a *Hecho* | Toda tarjeta en *Hecho* tiene el comentario "Revisado" (API-36) | 5 / 5 |
| 6 | Calidad | El código entra a `main` por Pull Request, aprobado por el otro integrante y cumpliendo la Definition of Done | Todo cambio en `src/` tiene un Pull Request aprobado en GitHub | 5 / 5 |
| 7 | Calidad | Cada commit empieza con la clave del ticket de Jira y se sube el mismo día en que se termina el trabajo | `git log` del Sprint: todos los commits tienen la clave `API-` (API-38) | 5 / 5 |
| 8 | Decisiones | Las decisiones de producto las toma el Product Owner después de escuchar al equipo. Las de proceso, las tomamos entre los dos. Si en 24 horas no hay acuerdo, desempata el PO en producto y la Scrum Master en proceso | Cada decisión registrada en la Sección 11 dice quién la tomó | 5 / 5 |
| 9 | Conflictos | Un desacuerdo lo planteamos directo entre los dos, por llamada o mensaje privado, hablando del trabajo y no de la persona. Si en 48 horas no se resuelve, la Scrum Master lo lleva a la Retrospective. Si pone en riesgo una entrega, lo consultamos con el docente | Los desacuerdos que se escalaron aparecen en el acta de la Retrospective | 5 / 5 |
| 10 | Cambios | Todo cambio de alcance o de fecha lo pedimos como ticket en Jira con la etiqueta `cambio` y lo registramos como CR en la Sección 11 antes de trabajarlo | Cada cambio hecho tiene su CR en el [Registro de Solicitudes de Cambio](11-decisiones-cambios-evidencias.md) | 5 / 5 |

Estos acuerdos se revisan en cada Retrospective. Si una regla no se cumplió, se conversa por qué y se decide si se mantiene, se cambia o se quita. Cada versión nueva queda en el [historial de cambios](historial-de-cambios.md).

**Firma:** los acuerdos quedan aprobados con un commit hecho por un integrante y firmado también por el otro con `Co-authored-by`.
