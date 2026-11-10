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





