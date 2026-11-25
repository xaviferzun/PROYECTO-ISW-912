# Sección 12 — Producto / Incremento final y cierre del proyecto

> **Semana:** 13 · **Responsables:** María Paz Ugalde Araya y Xavier Fernández Zúñiga · **Estado:** Final · **Jira:** API-32

## Incremento final

El incremento que se entrega es la **versión 1.0 del MVP**: una aplicación de escritorio en Python con una ventana (Tkinter) que permite configurar, respaldar, ver el resultado y restaurar una carpeta. No necesita instalar librerías. Cómo ejecutarla está en el [README](../README.md):

```
python src/main.py
python -m unittest discover -s tests -v
```

### Historias entregadas

| ID | Historia | Estado | Evidencia |
|---|---|---|---|
| HB-01 | Definir la tecnología del producto | Hecho | D-03 en la [Sección 11](11-decisiones-cambios-evidencias.md), API-8 |
| HB-02 | Entorno y estructura del código en `src/` | Hecho | Commit `2f4fdbf`, API-9 |
| HB-03 | Tablero de Jira | Hecho | Proyecto `API` en Jira, captura en `evidencias/` |
| HB-04 | Prueba técnica de copia y registro | Hecho | `src/respaldo/nucleo.py`, commit `6f06c62`, API-11 |
| HU-01 | Configurar la carpeta de origen y el destino | Hecho | 2 pruebas automáticas y paso 2 de la Demo |
| HU-02 | Ejecutar un respaldo manual | Hecho | 3 pruebas automáticas y paso 3 de la Demo |
| HU-03 | Ver el resultado del respaldo | Hecho | 2 pruebas automáticas y paso 4 de la Demo |
| HU-04 | Restaurar un respaldo completo | Hecho | 2 pruebas automáticas y pasos 5 y 6 de la Demo |

La validación está en la [Sección 09](09-calidad-dod.md): las 9 pruebas automáticas pasan y los 7 pasos de la prueba manual pasaron el 24 de noviembre ([captura](../evidencias/demo-mvp-2026-11-24.png)).

### Historias que no se entregaron

| ID | Historia | Por qué |
|---|---|---|
| HU-05 | Restaurar archivos específicos | Diferida por CR-03 |
| HU-06 | Programar respaldos automáticos | Diferida por CR-03 |
| HU-07 | Consultar el historial de respaldos | Diferida por CR-03. En parte la cubre la lista de respaldos y el log |
| HU-08 | Verificar la integridad de un respaldo | Diferida por CR-03 |
| HU-09 | Recibir una alerta cuando un respaldo falla | Diferida por CR-03. En parte la cubre el aviso de *EXITO PARCIAL* o *FALLO* al terminar |

Siguen en el Product Backlog en ese orden, para una versión futura.

### Números del proyecto

| Medida | Planificado | Real |
|---|---|---|
| Sprints | 6 (28 oct – 8 dic) | 2 (Sprint 1: 1–10 nov, Sprint 2: 18–24 nov) |
| Puntos de historias de usuario | 32 | 13 (HU-01 a HU-04) |
| Horas estimadas de producto | 104 | 44 |
| Costo en dinero | ₡0 | ₡0 |
| Pruebas automáticas | — | 9, todas pasan |
| Commits en el repositorio | — | 41 al 24 de noviembre: 21 de Xavier y 20 de María Paz |
| Commits del Sprint 2 con la clave de Jira | Todos (API-38) | 17 de 17 |

## Resultados frente al Product Goal

> **Product Goal:** Que los usuarios puedan respaldar su información de forma automática y recuperarla de manera rápida y confiable cuando la necesiten.

Se cumplió la segunda parte: el usuario puede respaldar y recuperar su información de forma rápida y confiable. La primera parte, **que el respaldo sea automático, no se cumplió**, porque HU-06 quedó fuera del MVP.

| Objetivo específico del Charter ([Sección 00](00-portada-equipo.md)) | Resultado |
|---|---|
| 1. Configurar los respaldos (cuándo y dónde) | **En parte.** Se configura dónde (origen y destino). El cuándo depende de HU-06 |
| 2. Ejecutar respaldos automáticos y manuales con registro | **En parte.** Respaldo manual con log. Sin respaldo automático |
| 3. Restaurar la información total o parcialmente | **En parte.** Restauración total. La parcial es HU-05 |
| 4. Verificar la integridad y notificar fallos | **No.** HU-08 y HU-09 diferidas. Al terminar cada respaldo sí se avisa si hubo errores |
| 5. Documentar el proceso en el Expediente con Scrum | **Sí.** Secciones 00 a 12, actas de los Sprints, historial de cambios y Jira |

## Informe final

### Resumen

El proyecto buscó resolver un problema común: personas y pequeñas organizaciones pierden información porque no hacen respaldos o no saben si funcionaron. Lo trabajamos dos personas con Scrum: Xavier como Product Owner y María Paz como Scrum Master, los dos como Developers. Usamos Jira para el backlog y los Sprints, y GitHub para el código y el Expediente.

### Cómo se desarrolló

1. **Semanas 3 a 8 (planificación):** Charter, problema, interesados, ciclo de vida híbrido, backlog con 9 historias, estimaciones y cronograma de 6 Sprints. Cada integrante tuvo sus secciones (ver la RACI en la [Sección 10](10-comunicacion-responsabilidades.md)).
2. **Sprint 1 (1–10 nov):** el objetivo era dejar lista la base técnica. **No se cumplió**: la tecnología no se decidió a tiempo, no hubo Daily y el trabajo se juntó al final. El Expediente sí avanzó (Secciones 06 a 09).
3. **Review y Retrospective del Sprint 1 (18 nov):** reconocimos el atraso y aprobamos **CR-03**: reducir la entrega a un MVP con HU-01 a HU-04. Definimos tres acciones de mejora (API-36, API-37, API-38) y los Working Agreements.
4. **Sprint 2 (18–24 nov):** se decidió la tecnología, se construyó el MVP con sus pruebas y se completó el Expediente. Detalle en el [acta del Sprint 2](../scrum/sprints/sprint-02/acta-review-retrospective.md).

### Desempeño del proyecto

| Área | Resultado |
|---|---|
| **Alcance** | Se entregó el 41 % de los puntos planificados (13 de 32), con las historias de mayor prioridad. El cambio quedó registrado como CR-03 |
| **Tiempo** | Se usaron 2 Sprints en vez de 6. Hubo una semana sin Sprint activo (11–17 nov) |
| **Costo** | ₡0 en dinero, como se planificó ([Sección 07](07-planificacion-estimaciones-costos.md)) |
| **Calidad** | 9 pruebas automáticas y prueba manual completa en un equipo. La prueba en la segunda máquina no se hizo |
| **Riesgos** | R-01 (atraso) ocurrió y se manejó con CR-03. Los demás riesgos se controlaron con las respuestas de la [Sección 08](08-riesgos-adquisiciones.md) |
| **Equipo** | El trabajo quedó repartido: 21 commits de Xavier y 20 de María Paz. La revisión por pares (API-36) se cumplió solo en parte |

## Lecciones aprendidas

| # | Qué pasó | Qué aprendimos | Qué haríamos distinto |
|---|---|---|---|
| 1 | La decisión de tecnología se quedó abierta todo el Sprint 1 y bloqueó el producto | Una decisión pendiente puede detener todo el trabajo que depende de ella | Tomar las decisiones técnicas en el primer día del primer Sprint |
| 2 | Hubo tarjetas en *Listo* sin cumplir sus criterios | Sin una Definition of Done desde el inicio, "Listo" significa cosas distintas para cada uno | Escribir la DoD antes del primer Sprint y usar siempre la columna *En revisión* |
| 3 | No hicimos Daily en el Sprint 1 | Sin un chequeo corto, nadie notó a tiempo que el producto no avanzaba | Daily corto por mensaje tres veces por semana desde el primer día |
| 4 | Reducir el alcance (CR-03) permitió entregar algo que funciona | Es mejor entregar menos historias terminadas que muchas a medias | Definir el MVP desde la planificación y no esperar a ir atrasados |
| 5 | Poner la clave de Jira en cada commit dio trazabilidad entre tareas y cambios | Con eso se puede mostrar qué se hizo, quién lo hizo y cuándo | Mantenerlo desde el primer commit |
| 6 | El Expediente avanzó más rápido que el producto | Documentar es más fácil de empezar, pero el producto es lo que valida el plan | Equilibrar cada Sprint con trabajo de producto y de documentación |

## Cierre del proyecto

- **Entrega oficial:** 25 de noviembre de 2026, con el Expediente completo, el repositorio, la Demo y la defensa oral.
- **Cierre en Jira:** el Sprint 2 se cerró el 24 de noviembre. Lo que no se entregó (HU-05 a HU-09) queda en el Product Backlog.
- **Para una próxima versión:** HU-06 (respaldos automáticos) es la primera, porque completa el Product Goal. Después HU-05, HU-08, HU-09 y HU-07, y probar el producto en Linux y macOS.
- **Retroalimentación del docente:** se agregará aquí después de la exposición.

| Rol | Nombre | Acepta el cierre |
|---|---|---|
| Product Owner | Xavier Fernández Zúñiga | Sí, 24 de noviembre de 2026 |
| Scrum Master | María Paz Ugalde Araya | Sí, 24 de noviembre de 2026 |
