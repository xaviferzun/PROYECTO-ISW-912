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

Cada elemento tiene una categotia, tipo y un dueño el cual es el que vijila el riesgo y reponde cuando se activa.
La oprtunidad se mide con la misma escala, pero el impacto es un benefisio. 

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

### Mapa de calor

Cruza la probabilidad (filas) con el impacto (columnas) de las amenazas que siguen abiertas. En cada celda se indica el nivel según la tabla de puntuación. R-01 aparece en su posición original solo como referencia, porque ya es un problema. O-01 no se dibuja aquí porque es una oportunidad.

| Probabilidad ↓ / Impacto → | 1 · Muy bajo | 2 · Bajo | 3 · Medio | 4 · Alto | 5 · Muy alto |
|---|---|---|---|---|---|
| **5 · Muy alta** | Medio | Alto | Alto | Crítico | Crítico |
| **4 · Alta** | Bajo | Medio | Alto | Alto | **R-01** (problema)<br>Crítico |
| **3 · Media** | Bajo | Medio | **R-05**<br>Medio | **R-02, R-04, R-06, R-07**<br>Alto | **R-03**<br>Alto |
| **2 · Baja** | Bajo | Bajo | **R-09**<br>Medio | Medio | **R-08**<br>Alto |
| **1 · Muy baja** | Bajo | Bajo | Bajo | Bajo | Medio |

Seis de las ocho amenazas abiertas están en nivel Alto, y R-03 es la de mayor puntuación (15). Por eso las respuestas de la siguiente sección empiezan por los riesgos de nivel Alto.


### Problemas: riesgos que ya ocurrieron

Cuando un riesgo se materializa deja de ser una posibilidad y se maneja como problema: se registra qué pasó, qué se hizo y cuándo se cierra.

| Campo | R-01 · Atraso en el desarrollo |
|---|---|
| Qué pasó | El Sprint 1 (1 al 10 de noviembre) no cumplió su objetivo. No se decidió la tecnología, `src/` quedó vacío y no hubo Incremento. En la Review del 18 de noviembre el proyecto iba unos dos Sprints atrasado ([acta](../scrum/sprints/sprint-01/acta-review-retrospective.md)). |
| Causa | La decisión técnica (API-8) quedó sin tomar todo el Sprint y no hubo Daily que lo hiciera visible. |
| Respuesta aplicada | CR-02 movió las fechas del Sprint 1. CR-03 redujo el alcance de 32 a 13 puntos y de 104 a 44 horas. Se agregaron la sesión técnica (API-37), el Daily los lunes, miércoles y viernes (Working Agreement 3), la revisión por pares (API-36) y los commits con clave de Jira (API-38). |
| Estado | Abierto. El código del MVP (HU-01 a HU-04) ya está en el repositorio desde el 22 de noviembre. El problema se cierra cuando el Sprint 2 termine con esas historias en *Hecho*. |
| Si empeora | Si el 24 de noviembre HU-04 sigue sin pasar a *Hecho*, se entrega lo que esté terminado, se muestran las pruebas automáticas y el log como indica la [Sección 11](11-decisiones-cambios-evidencias.md), y el Product Owner registra el ajuste como CR. |
| Dueño | María Paz |
| Fecha de revisión | 24 de noviembre de 2026 (Retrospective del Sprint 2) |
| Riesgo residual | Alto (3 × 4 = 12). No hay otro Sprint antes de la entrega del 25 de noviembre. |

## Respuestas a los riesgos

Para cada riesgo se establecen acciones preventivas y respuestas que permitan disminuir su probabilidad de ocurrencia o reducir sus consecuencias.

Para las amenazas se elige una de estas estrategias: **evitar** (cambiar el plan para que el riesgo no exista), **mitigar** (bajar su probabilidad o su impacto), **transferir** (pasarlo a un tercero) o **aceptar** (dejarlo y tener un plan por si ocurre). Para las oportunidades se usa **explotar**, **mejorar** o **aceptar**. En este proyecto no se transfiere ningún riesgo, porque no hay seguros ni proveedores externos (ver Plan de adquisiciones).

Cada tabla indica la acción concreta, el **disparador** (la señal que activa el plan de contingencia), el dueño, la fecha de revisión y el riesgo que queda después de aplicar la respuesta. Las fechas siguen el calendario del Sprint 2: Daily el lunes 23, Sprint Review y Retrospective el martes 24 y entrega el miércoles 25 de noviembre de 2026.

### R-02 · Incompatibilidad con sistemas operativos y estructuras de archivos

| Campo | Detalle |
|---|---|
| Nivel inicial | Alto (3 × 4 = 12) |
| Estrategia | Mitigar |
| Acción concreta | El producto usa solo la librería estándar de Python (D-03) y rutas con `pathlib`. La única parte que depende del sistema operativo es abrir la carpeta de un respaldo, que tiene una opción para Windows, macOS y Linux. Las pruebas automáticas ya usan nombres con espacios, tildes y «ñ» (`clientes ñandú.csv`, `año 2026`). Antes de pasar una historia con código a *Hecho* se prueba en la máquina de cada integrante. [PENDIENTE: sistema operativo y versión de Python de cada integrante.] |
| Disparador | Una prueba falla en una de las dos máquinas, o un archivo con nombre especial no aparece en el respaldo. |
| Plan de contingencia | Registrar un Error en Jira con el mensaje y el sistema operativo, reproducirlo en la otra máquina y corregirlo. Si no se corrige antes del 24 de noviembre, se anota como limitación en el Expediente y la Demo se hace en la máquina donde funciona. |
| Dueño | Xavier |
| Fecha de revisión | 23 de noviembre de 2026 |
| Riesgo residual | Medio (2 × 4 = 8). Solo se prueba en dos computadoras. |

### R-03 · Pérdida o corrupción de información

| Campo | Detalle |
|---|---|
| Nivel inicial | Alto (3 × 5 = 15) |
| Estrategia | Mitigar, y aceptar lo que queda mientras HU-08 siga fuera del MVP |
| Acción concreta | Cada respaldo se guarda en una carpeta nueva con fecha y nunca sobrescribe otro (D-04). Antes de restaurar, el sistema avisa si hay archivos con el mismo nombre y pide confirmación (D-06). Las pruebas automáticas comparan byte por byte lo copiado con el original (`test_respaldo_copia_todo_con_subcarpetas`) y comprueban que la restauración recupera lo borrado (`test_restauracion_completa_recupera_lo_borrado`). Todas las pruebas usan carpetas de ejemplo, nunca datos reales. |
| Disparador | Falla una de esas pruebas, el respaldo termina en *EXITO PARCIAL* o *FALLO* en el log, o al probar a mano faltan archivos en la carpeta restaurada. |
| Plan de contingencia | No usar el respaldo afectado y repetirlo desde el origen, que el sistema no modifica. Abrir un Error en Jira y no pasar HU-02 ni HU-04 a *Hecho* hasta corregirlo. |
| Dueño | Xavier |
| Fecha de revisión | 23 de noviembre de 2026 |
| Riesgo residual | Alto (2 × 5 = 10). La verificación con huellas hash (HU-08) quedó fuera por CR-03, así que el MVP no detecta por sí solo un archivo dañado después de copiado. Se acepta para esta entrega y se reduce cuando se haga HU-08. |

### R-04 · Fallos en los respaldos por programación o destino no disponible

| Campo | Detalle |
|---|---|
| Nivel inicial | Alto (3 × 4 = 12) |
| Estrategia | Evitar la parte automática y mitigar la del destino |
| Acción concreta | Los respaldos automáticos (HU-06) quedaron fuera del MVP por CR-03, así que esa parte no se construye en esta entrega. En el respaldo manual, el sistema revisa que el destino esté disponible antes de copiar y muestra un mensaje. Si algo falla, no se lanza una excepción: el problema queda en el log (`test_origen_invalido_falla_sin_excepcion_y_queda_en_log`). Un archivo con error no detiene a los demás (D-05). |
| Disparador | Un respaldo termina en *FALLO* o *EXITO PARCIAL*, o el destino (por ejemplo un disco externo) no está conectado a la hora de la Demo. |
| Plan de contingencia | Repetir el respaldo con una carpeta local como destino. Si falla durante la exposición, se muestran las pruebas automáticas y el log, como indica la [Sección 11](11-decisiones-cambios-evidencias.md). |
| Dueño | Xavier |
| Fecha de revisión | 24 de noviembre de 2026 |
| Riesgo residual | Medio (2 × 4 = 8). Sin alertas (HU-09), si un respaldo falla el usuario solo lo ve en pantalla y en el log. Si HU-06 se retoma, el riesgo se evalúa de nuevo. |

### R-06 · Dificultades con la verificación de integridad (hash)

| Campo | Detalle |
|---|---|
| Nivel inicial | Alto (3 × 4 = 12) |
| Estrategia | Evitar |
| Acción concreta | HU-08 está diferida por CR-03 y no entra al Sprint 2. Sigue en el Product Backlog (API-19). |
| Disparador | El Product Owner propone traer HU-08 a un Sprint. |
| Plan de contingencia | Antes de comprometerla, hacer una prueba técnica corta, como la de HB-04, con `hashlib`, que viene incluida en Python. Si no sale en ese tiempo, la historia sigue diferida. |
| Dueño | Xavier |
| Fecha de revisión | 24 de noviembre de 2026 (Sprint Review) |
| Riesgo residual | Bajo (1 × 4 = 4) para esta entrega. Vuelve a evaluarse si HU-08 se retoma. |

### R-07 · Baja adopción por una interfaz complicada

| Campo | Detalle |
|---|---|
| Nivel inicial | Alto (3 × 4 = 12) |
| Estrategia | Mitigar |
| Acción concreta | La ventana tiene tres partes (Configuración, Respaldo y Respaldos disponibles) y los mensajes de error indican la causa. Se hace la prueba con usuarios de la [Sección 09](09-calidad-dod.md) con al menos una persona que no sea del equipo. [PENDIENTE: persona de prueba y fecha.] |
| Disparador | La persona de prueba no completa 3 de las 4 tareas sin ayuda, o no entiende un mensaje. |
| Plan de contingencia | Cambiar los textos de los botones y mensajes que causaron la duda y repetir la prueba. Si no hay tiempo, se anota en el Product Backlog como mejora. |
| Dueño | Xavier |
| Fecha de revisión | 24 de noviembre de 2026 (Sprint Review) |
| Riesgo residual | Medio (3 × 3 = 9). Sin historial ni alertas (HU-07 y HU-09, fuera por CR-03), el usuario tiene menos formas de confiar en la herramienta. |

### R-08 · Exposición de información sensible

| Campo | Detalle |
|---|---|
| Nivel inicial | Alto (2 × 5 = 10) |
| Estrategia | Mitigar lo que el equipo controla y aceptar el cifrado, que está fuera de alcance |
| Acción concreta | Las pruebas y la Demo usan solo datos ficticios. El log no guarda el contenido de los archivos. La configuración y el log se guardan en la carpeta `.sistema-respaldo` del usuario, no en el repositorio. El otro integrante revisa que cada commit no tenga credenciales ni rutas personales (Definition of Done). El cifrado de los respaldos queda como mejora futura ([Sección 06](06-alcance-product-backlog.md)) y se consulta al equipo de seguridad si se retoma ([Sección 03](03-interesados.md)). |
| Disparador | Aparece un dato real, una credencial o una ruta personal en un commit, en una carpeta de ejemplo o en una captura. |
| Plan de contingencia | Quitar el dato y subir un commit de corrección el mismo día. Si es una contraseña o una clave, cambiarla de inmediato. Avisar en el ticket de Jira. |
| Dueño | María Paz |
| Fecha de revisión | 24 de noviembre de 2026, antes de la entrega |
| Riesgo residual | Medio (1 × 5 = 5). Los respaldos que haga un usuario quedan como copias sin cifrar en su destino. |

### R-05 · Conflictos entre los cambios de los integrantes

| Campo | Detalle |
|---|---|
| Nivel inicial | Medio (3 × 3 = 9) |
| Estrategia | Mitigar |
| Acción concreta | Hacer `git pull` antes de editar y no editar el mismo archivo al mismo tiempo ([Sección 10](10-comunicacion-responsabilidades.md)). Cada commit lleva la clave del ticket y se sube el mismo día (Working Agreement 7). En el Sprint 2 casi todo el código lo escribe una sola persona, lo que baja la probabilidad de conflictos. |
| Disparador | `git pull` o `git push` avisa de un conflicto. |
| Plan de contingencia | Resolver el conflicto entre los dos en una llamada, comparando los dos cambios. Nadie usa `git push --force`. |
| Dueño | María Paz |
| Fecha de revisión | 24 de noviembre de 2026 |
| Riesgo residual | Bajo (2 × 2 = 4) |

### R-09 · Dependencia de herramientas y bibliotecas externas

| Campo | Detalle |
|---|---|
| Nivel inicial | Medio (2 × 3 = 6) |
| Estrategia | Evitar en las bibliotecas y mitigar en Jira y GitHub |
| Acción concreta | El MVP usa solo la librería estándar de Python (D-03), sin instalar nada. Antes de agregar una biblioteca se revisan compatibilidad, licencia e instalación (proceso de selección de esta sección). Para Jira y GitHub se aplica el plan de salida de más abajo. |
| Disparador | Alguien propone instalar una biblioteca con `pip`, o Jira o GitHub no están disponibles por más de 24 horas, o cambian las condiciones de su plan gratuito. |
| Plan de contingencia | Plan de salida para Jira y GitHub. |
| Dueño | María Paz |
| Fecha de revisión | 24 de noviembre de 2026 |
| Riesgo residual | Bajo (1 × 3 = 3) |

### O-01 · Adelantar una historia diferida

| Campo | Detalle |
|---|---|
| Nivel inicial | Medio (3 × 3 = 9) |
| Estrategia | Aceptar: se aprovecha solo si sobra tiempo |
| Acción concreta | Si HU-01 a HU-04 terminan antes del cierre del Sprint 2, Xavier revisa si HU-05 (restaurar archivos específicos) o HU-07 (historial) caben. El código ya tiene `listar_respaldos` y cada respaldo guarda un `manifiesto.json` con la lista de archivos y su tamaño, que esas historias podrían usar. Si se decide hacerla, se pide como cambio (CR) antes de trabajarla, como indica el Working Agreement 10. |
| Disparador | HU-01 a HU-04 están en *Hecho* antes del 24 de noviembre y queda tiempo en el Sprint. |
| Plan si no se aprovecha | HU-05 y HU-07 siguen en el Product Backlog (API-16 y API-18) para una versión futura. El alcance de la entrega no cambia. |
| Dueño | Xavier |
| Fecha de revisión | 23 de noviembre de 2026 |
| Beneficio esperado | Una historia más en el MVP sin cambiar la tecnología. |

### Plan de salida para Jira y GitHub

Jira y GitHub son servicios de terceros (R-09). El repositorio y el sitio de Jira están hoy en la cuenta de Xavier, por lo que perder el acceso a esa cuenta también afectaría a María Paz. Este plan dice qué hacer si alguno deja de estar disponible.

| Servicio | Qué podría pasar | Qué ya tenemos | Pasos de salida |
|---|---|---|---|
| **Jira** | Se pierde el acceso, el plan gratuito cambia o el servicio no responde por más de 24 horas. | Capturas del tablero en `evidencias/`. Las historias y sus criterios están en la [Sección 06](06-alcance-product-backlog.md). Cada commit lleva la clave `API-` de su ticket. | 1. Al cierre de cada Sprint, exportar los tickets a CSV y guardarlos en `evidencias/` [PENDIENTE: primera exportación el 24 de noviembre].<br>2. Si Jira no vuelve, llevar el estado del trabajo en GitHub Projects, la alternativa que se evaluó en D-01, usando el CSV.<br>3. Anotar la decisión en la [Sección 11](11-decisiones-cambios-evidencias.md). |
| **GitHub** | Se pierde el acceso al repositorio o el servicio no responde el día de la entrega. | Cada integrante tiene un clon local con todo el historial. | 1. Antes de la entrega, crear un `.zip` del repositorio con `git archive --format=zip -o PROYECTO-ISW-912.zip HEAD`.<br>2. Si GitHub no vuelve, crear un repositorio nuevo en otro servicio gratuito y ejecutar `git remote set-url origin <url-nueva>` y `git push --all`.<br>3. Avisar al docente del cambio de enlace. [PENDIENTE: confirmar con el docente cómo entregar si GitHub falla.] |

**Dueños:** María Paz hace las exportaciones y el `.zip`. Xavier mantiene las cuentas y confirma que María Paz tiene permiso de escritura en el repositorio y en el proyecto de Jira.

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

### Proceso de selección de recursos

La selección de herramientas y recursos se realiza considerando los siguientes criterios:

- **Costo:** Se priorizan herramientas gratuitas o de código abierto.
- **Compatibilidad:** Deben funcionar con las tecnologías seleccionadas para el desarrollo del producto.
- **uUso:** Prmitir que los integrantes trabajen sin configuraciones excesivamente complejas.
- **Confiabilidad:** Contar con documentación y condiciones de uso que permitan utilizarlas durante el proyecto.
- **Seguridad:** Evitar exponer información sensible y que comprometa la integridad de los respaldos.

Antes de incorporar una nueva biblioteca o herramienta el equipo revisará compatibilidad, licencia y requisitos de instalación.

### Gestión de proveedores

El proyecto no requiere actualmente proveedores externos ya que no se contempla contratar almacenamiento en la nube ni adquirir servicios comerciales. Si en futuras etapas se identifica la necesidad de utilizar un servicio externo, se evaluarán sus condiciones de uso, costos, disponibilidad, seguridad y compatibilidad con el producto.


### Criterios de aceptación de los recursos

Para considerar que una herramienta este disponible para utilizarse deberá cumplir con las siguientes condiciones:

- Estar correctamente instalado o configurado.
- Ser compatible con el entorno de desarrollo.
- Permitir realizar las actividades para las que fue seleccionado.
- No generar costos adicionales en el proyecto.
- Contar con documentación suficiente para facilitar su utilización y mantenimiento.

