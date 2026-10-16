# Sección 04 — Ciclo de vida del proyecto y primer Sprint

> **Semana:** 3 · **Responsable:** Xavier Fernández Zúñiga · **Estado:** Borrador

## Ciclo de vida seleccionado y justificación

El proyecto sigue un **ciclo de vida híbrido**:

- **Predictivo** en lo que ya es estable: las restricciones (presupuesto bajo, privacidad de datos, compatibilidad con distintos sistemas), el objetivo del proyecto y las fechas fijas de entrega del curso. Esto se planifica desde el inicio.
- **Adaptativo** en el desarrollo del producto: las funciones de respaldo, restauración y alertas se construyen en Sprints semanales con Scrum, porque el principal riesgo (baja adopción) solo se comprueba probando con usuarios y ajustando según su retroalimentación.

### Mapa del ciclo de vida

```mermaid
flowchart LR
    A["Origen del problema<br/>Pérdida de información<br/>por falta de respaldos"] --> B["Inicio<br/>Charter, Product Goal,<br/>Scrum Team, interesados"]
    B --> C["Planificación base<br/>Alcance, backlog,<br/>riesgos, cronograma"]
    C --> D["Desarrollo iterativo<br/>Sprints semanales"]
    D -->|Retroalimentación| D
    D --> E["Cierre<br/>Demo, Informe Final,<br/>entrega del Expediente"]
```

| Fase | Qué ocurre | Enfoque |
|---|---|---|
| Origen del problema | El equipo identifica que personas y organizaciones pierden información por no contar con respaldos ante fallas, robos, virus o borrados accidentales. | — |
| Inicio | Project Charter, Product Goal, conformación del Scrum Team e identificación de interesados. | Predictivo |
| Planificación base | Alcance, Product Backlog inicial, riesgos, estimaciones y cronograma general. | Predictivo |
| Desarrollo iterativo | Sprints de una semana: se construye, se revisa y se ajusta según la retroalimentación. | Adaptativo |
| Cierre | Demo del incremento, Informe Final, entrega del Expediente y defensa oral (Semana 13). | Predictivo |

## Primer Sprint: Sprint Goal

**Sprint 1 · Duración:** 1 semana

> **Sprint Goal:** Dejar lista la base técnica del proyecto y comprobar que el sistema puede copiar una carpeta a un destino y registrar el resultado.

El primer Sprint se enfoca en **historias habilitadoras**: tareas que todavía no entregan una función al usuario, pero preparan el entorno y reducen la incertidumbre técnica para poder construir el producto en los siguientes Sprints.

| ID | Historia habilitadora | Prioridad |
|---|---|---|
| HB-01 | Definir la tecnología del producto (lenguaje, tipo de aplicación y librerías) y justificar la elección según las restricciones del proyecto. | Alta |
| HB-02 | Configurar el entorno de desarrollo y la estructura del código en la carpeta `src/` del repositorio. | Alta |
| HB-03 | Configurar el tablero de seguimiento en GitHub Projects con el backlog inicial. | Alta |
| HB-04 | Realizar una prueba técnica: copiar una carpeta local a un destino y registrar en un archivo si la operación fue exitosa o falló. | Alta |

### Por qué empezamos por estas

- **Sin base técnica no se puede construir:** elegir la tecnología y preparar el entorno es requisito para todo lo demás.
- **Reducen el riesgo técnico temprano:** la prueba técnica confirma que el respaldo es posible y permite verificar pronto la compatibilidad con distintos sistemas, una de nuestras restricciones.
- **Dan transparencia desde el inicio:** con el tablero de seguimiento, el avance de cada Sprint queda visible para el equipo y el docente.

### Planificación tentativa de los siguientes Sprints

| Sprint | Enfoque |
|---|---|
| Sprint 1 | Historias habilitadoras (base técnica). |
| Sprint 2 | Respaldo manual: elegir origen y destino, ejecutar el respaldo y ver el resultado. |
| Sprint 3 | Restauración de archivos respaldados. |
| Sprint 4 | Respaldos automáticos programados. |
| Sprint 5 en adelante | Verificación de integridad, alertas, historial y mejoras según retroalimentación. |

Esta planificación se ajustará al cierre de cada Sprint, según lo aprendido.

## Duración y eventos Scrum

| Evento | Cómo lo aplicamos |
|---|---|
| Sprint | 1 semana, alineado con las sesiones del curso. |
| Sprint Planning | Al inicio de cada Sprint: elegimos ítems del backlog y definimos el Sprint Goal. |
| Daily Scrum | Chequeo corto por mensaje: qué avancé, qué haré, qué me bloquea. |
| Sprint Review | Al final de cada Sprint mostramos lo avanzado y recogemos retroalimentación. |
| Sprint Retrospective | Al cierre de cada Sprint: qué funcionó y qué mejorar. |