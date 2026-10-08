> Traducción comunitaria (borrador) — Política P2-002 de NTARI, Difusión Multilingüe Global. Fuente: README.md (original en inglés, instantánea del 2026-10-05). Borrador comunitario asistido por máquina, pendiente de revisión por el mantenedor regional según P2-002 §3.1. Las especificaciones técnicas centrales permanecen en inglés según §2.2.
>
> ¿Encontraste un error en esta traducción? Tu corrección es una contribución
> bienvenida y valorada: haz un fork del repositorio y abre un pull request en
> https://github.com/NTARI-RAND/Janus.

# Arquitectura de Doble Faz (Janus Facing Architecture)

El documento oficial de la Arquitectura de Doble Faz (JFA), custodiado por
Network Theory Applied Research Institute, Inc. (NTARI) conforme a
[sus estatutos](https://github.com/NTARI-RAND/bylaws) §1.4(a).

JFA permite a las comunidades atender la realidad económica del prosumo y ofrece
un camino del dinero chartal exógeno al crédito mutuo endógeno. Se organiza en
cinco capas funcionales — Sustrato, Registro, Pacto, Gobernanza, y Economía e
Información — cada una implementada en tres niveles: frontend, orquestador
y protocolo.

## El documento

| | |
|---|---|
| **Documento oficial** | [janus-facing-architecture.md](janus-facing-architecture.md) |
| **Preguntas sin resolver** | [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) |
| **Conceptos heredados de instrumentos anteriores** | [jfa-concept-triage-2026-08-24.md](jfa-concept-triage-2026-08-24.md) |
| **Suite de conformidad ejecutable** | [jfa-conformance-suite.py](jfa-conformance-suite.py) |
| **El sustrato bajo las restricciones de los proveedores (P1-004, artículo complementario)** | [P1-004_Substrate-Constraints_v0.1.md](P1-004_Substrate-Constraints_v0.1.md) |
| **Instrumentos anteriores** | [Historical Docs/](Historical%20Docs/) |

El documento en inglés es el que tiene autoridad. Las traducciones se ofrecen
para ampliar el alcance, no para la interpretación.

| Idioma | Archivo |
|---|---|
| العربية (árabe) | [janus-facing-architecture.ar.md](janus-facing-architecture.ar.md) |
| Español | [janus-facing-architecture.es.md](janus-facing-architecture.es.md) |
| Français (francés) | [janus-facing-architecture.fr.md](janus-facing-architecture.fr.md) |
| हिन्दी (hindi) | [janus-facing-architecture.hi.md](janus-facing-architecture.hi.md) |
| Português (portugués) | [janus-facing-architecture.pt.md](janus-facing-architecture.pt.md) |
| toki pona | [janus-facing-architecture.tok.md](janus-facing-architecture.tok.md) |
| 中文 (chino) | [janus-facing-architecture.zh.md](janus-facing-architecture.zh.md) |

## Las líneas que no pueden cruzarse

La sección del documento oficial titulada *Las líneas que no pueden cruzarse*
contiene las doce disposiciones que ninguna implementación conforme puede
violar. Léela antes de construir.

## Implementaciones

Las implementaciones de referencia y las instancias se encuentran en sus propios
repositorios:

- [Tell](https://github.com/NTARI-RAND/Tell) — la capa de Registro: registro por
  operador, con testigos, de solo adición
- [Agrinet](https://github.com/NTARI-RAND/Agrinet) — protocolo de red agrícola
  federada
- [SoHoLINK](https://github.com/NTARI-RAND/SoHoLINK) ·
  [Cloudy](https://github.com/NTARI-RAND/Cloudy) ·
  [sohocloud-protocol](https://github.com/NTARI-RAND/sohocloud-protocol) —
  capa de Sustrato
- [lighthouse](https://github.com/NTARI-RAND/lighthouse) ·
  [shelter](https://github.com/NTARI-RAND/shelter) ·
  [childcare-trust-network](https://github.com/NTARI-RAND/childcare-trust-network) ·
  [shanina](https://github.com/NTARI-RAND/shanina) ·
  [COER](https://github.com/NTARI-RAND/COER) ·
  [world-chase-tag](https://github.com/NTARI-RAND/world-chase-tag) — semillas e
  instancias de la capa de Economía e Información

Las semillas se ajustan al estándar; la forma se adapta, los mínimos obligan.

## Verificar el documento

La suite es el peldaño que sostiene la carga: vincula la prosa a un registro de
invariantes con identificadores estables, de modo que el documento y el registro
no pueden distanciarse sin que la verificación falle. Solo biblioteca estándar,
sin dependencias.

```
python jfa-conformance-suite.py                 # check the document
python jfa-conformance-suite.py --list          # print the invariant registry
python jfa-conformance-suite.py --doc PATH      # check another copy
python jfa-conformance-suite.py --project PATH  # check a repo's open-questions deliverable
```

Código de salida 0 cuando todas las verificaciones ejecutadas pasan; 1 en caso
contrario. Ejecútala después de cualquier edición del documento oficial.

De los 26 invariantes registrados, 3 se vinculan aquí, en la capa del documento,
y 23 están **delegados**: vinculan software en ejecución o un instrumento de
gobernanza, y solo pueden hacerse cumplir mediante pruebas que residan junto a
ese código o ese instrumento. Se mantienen en el registro con identificadores
estables y se informan como delegados y no vinculados hasta que un repositorio
publique pruebas que citen esos identificadores. Un repositorio conforme cita
los identificadores; mientras no lo haga, su conformidad es autodeclarada.
Informar desde aquí un invariante delegado como "verificado" sería
autodeclaración disfrazada de ejecutor de pruebas, por lo que el sustituto se
etiqueta como tal.

## Aún no publicado aquí

El diseño de la mecánica de disputas — "el diseño de la mecánica de disputas"
tal como lo definen [los estatutos](https://github.com/NTARI-RAND/bylaws) §1.5 —
y los artículos de estructura y de robótica se conservan en el almacén de
documentos de NTARI y todavía no están en este repositorio.

## Licencia

Dos licencias, como indica el propio pie del documento:

| Qué | Licencia |
|---|---|
| La especificación — el documento oficial, sus traducciones y los instrumentos anteriores | [CC BY-SA 4.0](LICENSE-SPEC) |
| El software — la suite de conformidad | [AGPL-3.0](LICENSE) |
