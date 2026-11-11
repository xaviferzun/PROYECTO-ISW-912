# Sección 06 — Alcance, Product Backlog priorizado y criterios de aceptación

> **Semana:** 7 · **Responsable:** Maria Paz Ugalde Araya· **Estado: Borrador**  

## Declaración de alcance

El proyecto desarrollará una **herramienta que se ejecuta en la computadora del usuario para respaldar y recuperar información**, dirigida a pequeñas organizaciones sin un área de TI ([Sección 02](02-contexto-restricciones.md)). La herramienta permitirá:

1. Configurar qué carpeta se respalda y hacia qué destino se dirige (disco externo u otra carpeta).
2. Respaldar la información de forma manual o automática, según una frecuencia elegida por el usuario.
3. Restaurar un respaldo completo o archivos específicos.
4. Dar confianza en los respaldos mediante un historial de operaciones, la verificación de integridad y alertas cuando algo falla.

Esto confirma el alcance preliminar del Project Charter ([Sección 00](00-portada-equipo.md)) y responde directamente al Product Goal: *que los usuarios puedan respaldar su información de forma automática y recuperarla de manera rápida y confiable cuando la necesiten.*


## Fuera de alcance

- Respaldo de sistemas operativos completos o imágenes de disco.
- Infraestructura propia de almacenamiento en la nube o servidores.
- Aplicación móvil o versión web pública.
- Gestión de múltiples usuarios con permisos o cuentas.
- Cifrado avanzado de los respaldos (se documenta como mejora futura y se consulta con el equipo de seguridad, según la [Sección 03](03-interesados.md)).

## Product Backlog priorizado



Ordenado de mayor a menor prioridad. La estimación se clasifica en escala **1, 2, 3, 5** según el esfuerzo y la incertidumbre entre historias. El Sprint previsto puede cambiar al cierre de cada Sprint.

| Prioridad | ID | Jira | Historia | Épica | Puntos | Sprint previsto |
|---|---|---|---|---|---|---|
| 1 | HU-01 | API-12 | Configurar la carpeta de origen y el destino del respaldo | Configuración y respaldo manual | 3 | Sprint 2 |
| 2 | HU-02 | API-13 | Ejecutar un respaldo manual | Configuración y respaldo manual | 3 | Sprint 2 |
| 3 | HU-03 | API-14 | Ver el resultado del respaldo | Configuración y respaldo manual | 2 | Sprint 2 |
| 4 | HU-04 | API-15 | Restaurar un respaldo completo | Restauración de información | 5 | Sprint 3 |
| 5 | HU-05 | API-16 | Restaurar archivos específicos de un respaldo | Restauración de información | 3 | Sprint 3 |
| 6 | HU-06 | API-17 | Programar respaldos automáticos | Respaldos automáticos programados | 5 | Sprint 4 |
| 7 | HU-07 | API-18 | Consultar el historial de respaldos | Verificación, alertas e historial | 3 | Sprint 4 |
| 8 | HU-08 | API-19 | Verificar la integridad de un respaldo | Verificación, alertas e historial | 5 | Sprint 5 |
| 9 | HU-09 | API-20 | Recibir una alerta cuando un respaldo falla | Verificación, alertas e historial | 3 | Sprint 5 |

**Total:** 32 puntos en 9 historias que fueron distribuidos en los Sprints 2 a 5. El Sprint 6 queda para la preparación de la Demo.

### Criterios de priorización

- **Primero lo que hace funcionar el producto:** sin configurar y ejecutar un respaldo (HU-01 a HU-03) no existe nada que restaurar, programar o verificar.
- **Luego lo que entrega el valor principal:** la restauración (HU-04, HU-05) es la razón de ser de un respaldo y el centro del Product Goal.
- **Después lo que ataca la causa del problema:** los respaldos automáticos (HU-06) eliminan la dependencia de que alguien se acuerde de hacerlos.
- **Por último lo que da confianza:** historial, verificación y alertas (HU-07 a HU-09) reducen el riesgo de fallas no detectadas. Si el tiempo no alcanza, son las primeras en quedar para una versión futura sin afectar el funcionamiento básico.

## Historias de usuario y criterios de aceptación

### HU-01 · Configurar la carpeta de origen y el destino del respaldo (API-12)

Como **usuario**  quiero **respaldar una carpeta y el destino donde se guardará el respaldo**, para **controlar qué información se protege y dónde queda guardada**.

- El usuario puede seleccionar una carpeta de origen y una carpeta de destino.
- El sistema valida que ambas rutas existan y que el destino no esté dentro del origen; si no son válidas, muestra un mensaje claro.
- La configuración se guarda y sigue disponible al volver a abrir el programa.
- El usuario puede ver y modificar la configuración guardada.

### HU-02 · Ejecutar un respaldo manual (API-13)

Como **usuario**, quiero **ejecutar un respaldo manual cuando lo necesite** para **proteger información sencible**.

- Se copia todo el contenido de la carpeta de origen, incluidas las subcarpetas que van hacia el destino.
- Cada respaldo se guarda en una carpeta separada con fecha y hora, sin sobrescribir respaldos anteriores.
- Mientras se ejecuta, el usuario ve que el proceso está en curso.
- Si un archivo no se puede copiar lo que hace es que el respaldo continúa con los demás y el problema queda registrado.

### HU-03 · Ver el resultado del respaldo (API-14)

Como **usuario**, quiero **ver si el respaldo se ejecuto correctamente o falló**, para **saber si la información está realmente protegida**.

- Al terminar, el sistema muestra un resumen: resultado (éxito, éxito parcial o fallo), cantidad de archivos copiados, tamaño total y duración.
- Si hubo errores, el resumen indica cuántos archivos fallaron y por qué.
- El resultado queda guardado en el archivo de registro (log) con fecha y hora.

### HU-04 · Restaurar un respaldo completo (API-15)

Como **usuario**, quiero **restaurar un respaldo completo a una carpeta que yo elija**, para **recuperar toda mi información después de una pérdida**.

- El sistema muestra la lista de respaldos disponibles ordenados por fecha.
- El usuario elige un respaldo y una carpeta de destino para la restauración.
- Si en el destino ya existen archivos con el mismo nombre, el sistema pide confirmación antes de reemplazarlos.
- Al terminar, muestra cuántos archivos se restauraron y si hubo errores, y lo registra en el log.

### HU-05 · Restaurar archivos específicos de un respaldo (API-16)

Como **usuario**, quiero **restaurar solo algunos archivos o carpetas de un respaldo**, para **recuperar lo que borré por accidente sin reemplazar todo lo demás**.

- El usuario puede explorar el contenido de un respaldo y seleccionar uno o varios archivos o carpetas.
- Solo se restauran los elementos seleccionados, manteniendo su estructura de carpetas.
- Se aplica la misma confirmación de reemplazo que en HU-04.
- La operación queda registrada en el log.

### HU-06 · Programar respaldos automáticos (API-17)

Como **usuario**, quiero **programar respaldos automáticos con la frecuencia que yo elija**, para **no depender de acordarme de hacerlos**.

- El usuario puede elegir una frecuencia (diaria o semanal) y una hora.
- El respaldo se ejecuta automáticamente a la hora programada.
- El usuario puede ver la próxima ejecución programada y desactivar la programación.
- Cada ejecución automática queda registrada igual que un respaldo manual.


### HU-07 · Consultar el historial de respaldos (API-18)

Como **usuario**, quiero **consultar el historial de respaldos** para **saber cuándo fue la última vez que se respaldó la ultima copia de información**.

- El sistema muestra una lista de operaciones con fecha y hora como:  manual o restauración, resultado y cantidad de archivos.
- La lista está ordenada de la más reciente a la más antigua.
- Se destaca la fecha del último respaldo exitoso.

### HU-08 · Verificar la integridad de un respaldo (API-19)

Como **usuario**, quiero **comprobar que un respaldo está completo y sin daños**, para **tener la seguridad de que podré restaurarlo cuando lo necesite**.

- Al crear un respaldo, el sistema guarda una huella (hash) de cada archivo.
- El usuario puede pedir la verificación de un respaldo; el sistema compara las huellas y reporta si está íntegro o qué archivos faltan o cambiaron.
- El resultado de la verificación queda registrado en el historial.

### HU-09 · Recibir una alerta cuando un respaldo falla (API-20)

Como **usuario**, quiero **recibir una alerta cuando un respaldo automático falla o no se ejecuta**, para **corregir el problema antes de perder información**.

- Si un respaldo termina con fallo o éxito parcial, el sistema muestra una notificación visible.
- Si pasan más días de los configurados sin un respaldo exitoso, el sistema avisa al abrirse.
- La alerta indica qué pasó y qué puede hacer el usuario (por ejemplo, "El destino no está disponible: conecte el disco externo").
