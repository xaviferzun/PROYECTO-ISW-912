# Sección 07 — Planificación temporal, estimaciones y costos

> **Semana:** 8 · **Responsable:** Maria Paz Ugalde Araya · **Estado:** Borrador · **Jira:** API-27, API-43

## Estimaciones

Se utilizan dos medidas complementarias: los puntos de historia y las horas de esfuerzo. Los puntos de historia permiten comparar la complejidad y la incertidumbre de las historias de usuario, mientras que las horas ofrecen una referencia aproximada de la dedicación necesaria.

### Estimación mediante puntos de historia

Se utiliza la escala de 1 al 5, de acuerdo con el esfuerzo relativo y la incertidumbre de cada historia. Las estimaciones corresponden a las nueve historias definidas en la [Sección 06](06-alcance-product-backlog.md).

| ID | Jira | Historia de usuario | Puntos | Sprint previsto |
|---|---|---|---:|---|
| HU-01 | API-12 | Configurar la carpeta de origen y el destino del respaldo | 3 | Sprint 2 |
| HU-02 | API-13 | Ejecutar un respaldo manual | 3 | Sprint 2 |
| HU-03 | API-14 | Ver el resultado del respaldo | 2 | Sprint 2 |
| HU-04 | API-15 | Restaurar un respaldo completo | 5 | Sprint 2 |
| HU-05 | API-16 | Restaurar archivos específicos de un respaldo | 3 | Fuera del MVP (CR-03) |
| HU-06 | API-17 | Programar respaldos automáticos | 5 | Fuera del MVP (CR-03) |
| HU-07 | API-18 | Consultar el historial de respaldos | 3 | Fuera del MVP (CR-03) |
| HU-08 | API-19 | Verificar la integridad de un respaldo | 5 | Fuera del MVP (CR-03) |
| HU-09 | API-20 | Recibir una alerta cuando un respaldo falla | 3 | Fuera del MVP (CR-03) |
| | | **Total** | **32** | |

Después de la Review del Sprint 1 aprobamos CR-03: el MVP incluye solo HU-01 a HU-04, que suman **13 puntos y 44 horas**. HU-05 a HU-09 (19 puntos y 60 horas) siguen en el Product Backlog para una versión futura.

Las historias HU-04, HU-06 y HU-08 reciben 5 puntos ya que tienen mayor complejidad: requieren controlar la recuperación de archivos, ejecutar procesos programados o comparar huellas digitales para verificar la integridad. Las historias con menor puntuación tienen un alcance más delimitado.

### Estimación del esfuerzo de trabajo

Se estima el esfuerzo en horas para contar con una referencia de dedicación por funcionalidad. Estas horas son aproximadas y podrán ajustarse conforme avance el desarrollo.

| ID | Actividad | Esfuerzo estimado |
|---|---|---:|
| HU-01 | Configuración de origen y destino | 8 horas |
| HU-02 | Ejecución de respaldos manuales | 12 horas |
| HU-03 | Visualización de resultados | 8 horas |
| HU-04 | Restauración completa | 16 horas |
| HU-05 | Restauración de archivos específicos | 12 horas |
| HU-06 | Programación de respaldos automáticos | 16 horas |
| HU-07 | Historial de respaldos | 8 horas |
| HU-08 | Verificación de integridad | 16 horas |
| HU-09 | Alertas ante fallos | 8 horas |
| | **Total estimado** | **104 horas** |

Las 104 horas representan una estimación inicial del esfuerzo asociado a las funcionalidades del proyecto pero eso no quiere decir que corresponda a la duración del calendario ni a horas ya ejecutadas. Los avances se distribuye entre los dos participantes. Las actividades de documentación, reuniones Scrum y preparación de entregas se gestionan adicionalmente dentro de las semanas correspondientes.

## Plan temporal y cronograma de entregas

El proyecto utiliza un ciclo de vida híbrido: mantiene una planificación general de fechas y entregas, y desarrolla el producto de manera adaptativa mediante Scrum. Cada Sprint tiene una duración de una semana, según lo establecido en la [Sección 04](04-ciclo-vida-primer-sprint.md).

### Cronograma general

La tabla compara lo planificado al inicio con lo que pasó en realidad.

| Sprint | Planificado | Real | Contenido | Resultado |
|---|---|---|---|---|
| Sprint 1 | 28 oct – 3 nov | 1 – 10 nov (CR-02) | Habilitadoras HB-01 a HB-04 | No se cumplió el Sprint Goal ([acta](../scrum/sprints/sprint-01/acta-review-retrospective.md)) |
| Sprint 2 | 4 – 10 nov | 18 – 24 nov | Planificado: HU-01 a HU-03. Real: habilitadoras pendientes y HU-01 a HU-04 (CR-03) | MVP terminado y en revisión |
| Sprints 3 a 6 | 11 nov – 8 dic | No se realizan | HU-05 a HU-09, estabilización | Fuera del MVP (CR-03) |
| Entrega | — | 25 nov | Demo del MVP y entrega del Expediente | — |

### Seguimiento del cronograma

El seguimiento se realiza mediante Jira, donde se registran las historias de usuario, tareas, responsables y estados de avance. 
Al finalizar cada Sprint se compara el trabajo completado con lo planificado. 
También se puede utilizar el gráfico de trabajo pendiente para identificar desviaciones.

Si una actividad no se completa dentro del Sprint, el equipo analiza la causa y determina si debe trasladarse al siguiente Sprint o si corresponde ajustar las prioridades del Product Backlog.
 Cualquier cambio se comunica entre los integrantes y queda reflejado en Jira.

## Costos

El proyecto se desarrolla con un presupuesto bajo y aprovecha los recursos tecnológicos que ya poseen los integrantes. Por esta razón, se priorizan herramientas gratuitas, software de código abierto y almacenamiento local disponible. No se contempla contratar infraestructura propia de servidores ni servicios de almacenamiento en la nube, de acuerdo con las restricciones del proyecto descritas en la [Sección 02](02-contexto-restricciones.md).

### Estrategia de control de costos

Para mantener los costos dentro de lo establecido aplicamos las siguientes medidas:

- Utilizar herramientas gratuitas o de software libre durante el desarrollo.
- Aprovechar los equipos personales disponibles y evitar adquirir hardware adicional.
- Utilizar almacenamiento local o discos externos disponibles para realizar las pruebas.
- Evitar contratar servicios de almacenamiento en la nube, ya que no forman parte de la infraestructura prevista.
- Revisar las condiciones de uso y licencias de las herramientas y bibliotecas antes de incorporarlas.
- Evaluar cualquier necesidad de adquisición antes de comprometer recursos adicionales.

Cualquier gasto no previsto deberá discutirse y documentarse antes de realizarlo.

### Costo estimado

| Recurso | Uso | Costo |
|---|---|---:|
| Python 3 y Tkinter | Lenguaje y ventana del producto | ₡0 (software libre) |
| Git y GitHub (plan gratuito) | Control de versiones | ₡0 |
| Jira (plan gratuito, hasta 10 usuarios) | Backlog, Sprints y tablero | ₡0 |
| Computadoras personales y discos locales | Desarrollo y pruebas | ₡0 (equipo que ya tenemos) |
| **Total en dinero** | | **₡0** |

El costo principal es el tiempo del equipo: 44 horas estimadas para el MVP. Valorado a una tarifa de referencia de [PENDIENTE: tarifa por hora], el costo del esfuerzo sería 44 h × tarifa.
