# Sección 08 — Riesgos y adquisiciones

> **Semana:** 9 · **Responsable:** Maria Paz Ugalde Araya · **Estado:** Borrador

## Registro de riesgos

Debido a que el equipo está conformado por dos integrantes y dispone de un presupuesto bajo, se consideran especialmente los riesgos relacionados con el tiempo, la disponibilidad de recursos, las dificultades técnicas, la seguridad de la información y el cumplimiento de los objetivos.

Para evaluar cada riesgo se utiliza una escala de probabilidad e impacto de 1 a 5. La probabilidad representa la posibilidad de que ocurra el riesgo y el impacto representa el nivel de afectación que tendría sobre el proyecto. El nivel se calcula multiplicando ambos valores.

| Puntuación | Nivel de riesgo |
|---:|---|
| 1–4 | Bajo |
| 5–9 | Medio |
| 10–16 | Alto |
| 17–25 | Crítico |

### Matriz de riesgos identificados

| ID | Riesgo | Probabilidad | Impacto | Nivel (P × I) | Prioridad |
|---|---|---:|---:|---:|---|
| R-01 | Retrasos en el desarrollo por la disponibilidad limitada de tiempo de los integrantes. | 4 | 5 | 20 | Crítica |
| R-02 | Incompatibilidad del sistema con diferentes sistemas operativos o estructuras de archivos. | 3 | 4 | 12 | Alta |
| R-03 | Pérdida o corrupción de información durante las operaciones de respaldo o restauración. | 3 | 5 | 15 | Alta |
| R-04 | Fallos en la ejecución de respaldos automáticos por problemas de programación o falta de disponibilidad del destino. | 3 | 4 | 12 | Alta |
| R-05 | Problemas de integración o conflictos entre los cambios realizados por los integrantes. | 3 | 3 | 9 | Media |
| R-06 | Dificultades técnicas al implementar la verificación de integridad mediante funciones hash. | 3 | 4 | 12 | Alta |
| R-07 | Baja adopción de la herramienta debido a una interfaz complicada o a la falta de confianza de los usuarios. | 3 | 4 | 12 | Alta |
| R-08 | Exposición de información personal o sensible almacenada en los respaldos. | 2 | 5 | 10 | Alta |
| R-09 | Dependencia de herramientas o bibliotecas externas que cambien sus condiciones de uso o presenten incompatibilidades. | 2 | 3 | 6 | Media |

Los riesgos se revisarán durante el desarrollo y al cierre de cada Sprint, el impacto podria haber modificaciones sugun se obtenga nueva información.

## Respuestas a los riesgos

Para cada riesgo se establecen acciones preventivas y respuestas que permitan disminuir su probabilidad de ocurrencia o reducir sus consecuencias.

## Plan de adquisiciones

El proyecto no contempla la compra de infraestructura tecnológica, contratación de servicios externos ni adquisición de licencias comerciales. Debido a la restricción presupuestaria establecida, se prioriza el aprovechamiento de los recursos existentes y la utilización de herramientas gratuitas o de software libre.

Las adquisiciones se entienden como la identificación, selección y disponibilidad de los recursos tecnológicos necesarios para desarrollar, administrar y probar el producto.

### Seguimiento y control de los riesgos

El seguimiento de los riesgos se realizará durante todo el ciclo de vida del proyecto mediante las siguientes actividades:

1. **Revisión periódica:** durante la planificación y retrospectiva de cada Sprint se revisarán los riesgos existentes y se identificarán nuevas situaciones que puedan afectar el trabajo.
2. **Registro de incidentes:** cuando un riesgo se materialice, se documentará la situación, sus consecuencias y las acciones aplicadas.
3. **Actualización de prioridades:** si aumenta la probabilidad o el impacto de un riesgo, se actualizará su clasificación y se priorizarán las acciones necesarias.
4. **Comunicación:** cualquier situación que pueda comprometer una entrega o afectar el alcance deberá comunicarse entre los integrantes y registrarse en Jira.
5. **Control de cambios:** si la respuesta a un riesgo requiere modificar el alcance, las prioridades o las fechas del proyecto.

### Recursos tecnológicos y herramientas

 Herramienta | Uso dentro del proyecto | Tipo de adquisición | Justificación |
|---|---|---|---|
| Jira | Gestión del Product Backlog, planificación de Sprints y seguimiento de tareas. | Servicio gratuito | Permite organizar el trabajo y visualizar el avance del equipo. |
| Git | Control de versiones del código fuente. | Software libre | Facilita el seguimiento de cambios y la integración del trabajo. |
| GitHub | Almacenamiento del repositorio y colaboración entre integrantes. | Servicio gratuito | Permite compartir el código y mantener un historial de modificaciones. |
| Entorno de desarrollo | Escritura, ejecución y depuración del código. | Herramienta gratuita | Proporciona los recursos necesarios para construir y probar el producto. |
| Bibliotecas y dependencias | Implementación de las funciones de respaldo, restauración, programación y verificación. | Software libre o gratuito | Evita desarrollar desde cero funcionalidades que pueden resolverse con herramientas existentes. |
| Almacenamiento local | Guardar respaldos y realizar pruebas de recuperación. | Recurso disponible | Permite comprobar el funcionamiento sin contratar infraestructura externa. |
| Discos externos | Simular destinos físicos para los respaldos. | Recurso disponible, sujeto a disponibilidad | Permite probar la copia y recuperación de información en dispositivos externos. |
