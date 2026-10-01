# PROYECTO-ISW-912
Proyecto para el curso de Administración de Proyectos Informáticos ISW-912

$readme = @'
# PROYECTO-ISW-912

Proyecto Incremental del curso **ISW-912 Administración de Proyectos Informáticos** — Universidad Técnica Nacional, Sede San Carlos · III Cuatrimestre 2026.

## Problema (propuesta)

Sistema de Respaldo y Recuperación de Información: pérdida de información por falta de respaldos ante fallas, robos, virus o borrados accidentales.

## Scrum Team

| Integrante | Rol Scrum |
|---|---|
| María Paz Ugalde | Por definir |
| Xavier Fernández | Por definir |


## Estructura del repositorio

| Carpeta | Contenido |
|---|---|
| `expediente/` | Expediente del Proyecto, secciones 00 a 12 |
| `scrum/sprints/` | Planning, Review y Retrospectiva de cada Sprint |
| `evidencias/` | Capturas, actas y registros de las sesiones |
| `src/` | Código fuente del producto |

## Expediente del Proyecto

| Sección | Tema | Semana |
|---|---|---|
| [00](expediente/00-portada-equipo.md) | Portada e identificación del equipo | 3 |
| [01](expediente/01-problema-product-goal.md) | Problema, oportunidad y Product Goal | 3 |
| [02](expediente/02-contexto-restricciones.md) | Contexto organizacional y restricciones | 4 |
| [03](expediente/03-interesados.md) | Interesados / stakeholders | 4 |
| [04](expediente/04-ciclo-vida-primer-sprint.md) | Ciclo de vida y primer Sprint | 5 |
| [05](expediente/05-backlog-sprint-backlog.md) | Backlog inicial y Sprint Backlog | 6 |
| [06](expediente/06-alcance-product-backlog.md) | Alcance, Product Backlog y criterios de aceptación | 7 |
| [07](expediente/07-planificacion-estimaciones-costos.md) | Planificación temporal, estimaciones y costos | 8 |
| [08](expediente/08-riesgos-adquisiciones.md) | Riesgos y adquisiciones | 9 |
| [09](expediente/09-calidad-dod.md) | Calidad y Definition of Done | 10 |
| [10](expediente/10-comunicacion-responsabilidades.md) | Comunicación y responsabilidades | 11 |
| [11](expediente/11-decisiones-cambios-evidencias.md) | Decisiones, cambios y evidencias | 12 |
| [12](expediente/12-incremento-final-cierre.md) | Incremento final y cierre | 13 |
'@
[IO.File]::WriteAllText((Join-Path (Get-Location).Path "README.md"), $readme, (New-Object System.Text.UTF8Encoding $false))
