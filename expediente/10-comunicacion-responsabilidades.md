# Sección 10 — Comunicación y responsabilidades del equipo

> **Semana:** 7 (Plan de Comunicaciones y Tablero) · 11 (RACI y Working Agreements) · **Responsable:** Xavier Fernández Zúñiga · **Estado:** Borrador · **Jira:** API-30

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

> Se completará en la Semana 11.

## Working Agreements

> Se completarán en la Semana 11, a partir de las reglas de comunicación de esta sección y de lo aprendido en las Retrospectives.
