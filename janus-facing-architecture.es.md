> Traducción comunitaria (borrador) — Política P2-002 de NTARI, Difusión Multilingüe Global. Fuente: janus-facing-architecture.md (original en inglés, instantánea del 2026-08-31). Borrador comunitario asistido por máquina, pendiente de revisión por el mantenedor regional conforme a P2-002 §3.1. Las especificaciones técnicas centrales permanecen en inglés conforme al §2.2.
>
> ¿Encontraste un error en esta traducción? Tu corrección es una contribución
> bienvenida y valorada: haz un fork del repositorio del proyecto de NTARI y
> abre un pull request, o escríbenos a info@ntari.org.

# JFA: Arquitectura de Doble Faz (Janus Facing Architecture)

## Introducción

La Arquitectura de Doble Faz — llamada así por el dios romano que mira en dos direcciones a la vez, igual que todo participante económico enfrenta exigencias tanto de producción como de consumo — permite a las comunidades atender la realidad económica del prosumo. Cada miembro de una economía no es solo consumidor, sino prosumidor (Toffler, 1980), que produce simultáneamente algo de valor aunque lo único que tenga por ofrecer sea su tiempo. Ofrece además la opción de transformar el modelo de emisión: de dinero chartal exógeno (emitido por una autoridad externa a la comunidad) a crédito mutuo endógeno (emitido por los miembros entre sí a medida que transaccionan).

La segunda faz del nombre es política. Acemoglu y Robinson (2019) muestran que la libertad sobrevive únicamente dentro de un corredor estrecho, donde un Estado capaz — el Leviatán — se ve igualado por una sociedad igualmente capaz de controlarlo. Fuera del corredor, el Leviatán adopta sus otras formas: ausente, y la coordinación fracasa; despótico, y quien coordina domina a los coordinados; de papel, y los controles existen por escrito pero no en la práctica. Permanecer dentro del corredor exige lo que ellos llaman el efecto de la Reina Roja: Estado y sociedad corriendo juntos, cada uno acrecentando su capacidad porque el otro lo hace. Toda plataforma económica es un Leviatán en miniatura — coordina, hace cumplir y registra — y las plataformas dominantes de hoy son despóticas por construcción: evolucionan a la velocidad de la red mientras las instituciones destinadas a controlarlas se mueven a la velocidad de las reuniones.

La investigación de NTARI sitúa este fracaso en la infraestructura misma. Los sistemas deliberativos son cultura material: la arquitectura de una plataforma materializa una teoría sobre quién puede saber y quién puede decidir, y las arquitecturas de difusión predominantes tratan a los participantes como receptores pasivos (NTARI, 2025b). La brecha de velocidad resultante es estructural: la información se mueve a velocidad de red mientras la síntesis democrática sigue atada a ciclos electorales sincronizados por un reloj postal (NTARI, 2025a). JFA está construida para cerrar esa brecha desde dentro: la comunidad que coordina es la comunidad que controla, ambas capacidades intercambiadas de forma continua en el mismo software y a la misma velocidad, disciplinadas capa por capa por el costo de marcharse. Es un Leviatán encadenado en código.

La Arquitectura de Doble Faz (JFA) se organiza en cinco capas funcionales — Sustrato, Registro, Pacto, Gobernanza, y Economía e Información (E&I) — cada una implementada en tres niveles: el frontend, para la colaboración entre prosumidores; el orquestador, un backend que provee coordinación superpuesta entre comunidades geográficas; y el protocolo subyacente, el patrón para manejar datos de forma segura entre niveles.

El software de JFA está diseñado para publicarse y gestionarse en un entorno copyleft, generalmente la Licencia Pública General Affero de GNU, lo que permite que nuevos frontends, federaciones, protocolos y arquitecturas evolucionen en el mercado global, formando un común de software libre.

Este es el documento oficial, custodiado por Network Theory Applied Research Institute, Inc. Los instrumentos anteriores se conservan en [Historical Docs](Historical%20Docs/); los conceptos heredados de ellos constan en el [triaje de conceptos](jfa-concept-triage-2026-08-24.md); lo que sigue sin resolver se nombra en [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## Principios

**Responsabilidad compartida.** La comunidad que coordina la economía es la misma comunidad que controla esa coordinación. Las dos funciones se intercambian de forma continua, nunca se separan en gobernantes y gobernados.

**Disciplina institucional.** Cada capa se disciplina por el costo de abandonarla: donde marcharse es barato, disciplina la competencia; donde marcharse es costoso, los miembros votan; donde marcharse es imposible, las decisiones quedan abiertas a impugnación.

**Código escueto y auditable.** El software de protocolo se mantiene pequeño, no depende de nada más que de la biblioteca estándar de su lenguaje, y es auditable en su totalidad.

## Capa de Sustrato

Es el hardware donde todo ocurre, propiedad de prosumidores de CPU, GPU, impresoras, almacenamiento y sensores.

### Nivel de protocolo

Intercambia instrucciones y órdenes a través de un mercado distribuido de cómputo y almacenamiento operado en computadoras de consumo alojadas en hogares, oficinas y depósitos, así como en equipo industrial reacondicionado.

### Nivel de orquestador

Capacidad de cómputo federada de prosumidores, que crea más opciones a lo largo de la geografía.

### Nivel de frontend

Interfaz de E&I para prosumir cómputo y almacenamiento.

## Capa de Registro

Una función compensada del sustrato, que registra y sirve el diálogo entre las capas de E&I y de Pacto para el público.

El registro de lo ocurrido se guarda de seis maneras. Cada parte de una transacción conserva su propio registro; el operador conserva el suyo; dos testigos conservan los suyos; y los hashes se comprometen a una cadena pública única, distribuida a través del sustrato — el registro para todos quienes no fueron ni transactores, ni testigos, ni operador. La cadena es de solo adición: el daño se perdona mediante anotación, nunca borrando. Una plataforma debe tener al menos dos testigos independientes; con menos, un despliegue debe etiquetarse a sí mismo como no federado.

### Nivel de protocolo

Captura, categoriza y aplica hash a cada transmisión dentro de la pila, a fin de establecer reputación mediante la capa de Pacto y de sentar la base de un medio de intercambio mediante E&I.

### Nivel de orquestador

Federa registros a lo largo de la geografía, habilitando reputación e intercambio compartidos. Lo que la federación comparte es verdad registrada — reputación e historial de intercambios — nunca una unidad monetaria.

### Nivel de frontend

Servicio compensado de cómputo y registro provisto por prosumidores en la capa de sustrato de E&I.

## Capa de Pacto

Un contrato social ejecutado en código, que informa expectativas flexibles para las interacciones entre prosumidores.

### Nivel de protocolo

Una evaluación simple, escrita en código ejecutable, para que los prosumidores califiquen sus interacciones entre sí a lo largo de la pila.

### Nivel de orquestador

Una API que sirve evaluaciones conformes a través de los mercados de E&I de la pila, desde prosumidores del sustrato. Cuando ocurren aparentes incumplimientos del pacto, los operadores de plataforma adjudican entre sus prosumidores; las disputas que cruzan plataformas se adjudican en la capa de testigos. Quienes adjudican son calificados por su conducta por ambos prosumidores u operadores involucrados.

### Nivel de frontend

La interfaz de E&I donde se sirve la API.

## Capa de Gobernanza

Aquí es donde y cómo los seres humanos se reúnen para actuar colaborativamente sobre la pila.

### Nivel de protocolo

Organización sin fines de lucro de custodia de software copyleft.

### Nivel de orquestador

La membresía en el Network Theory Applied Research Institute, obtenida operando una instancia federada de software JFA.

### Nivel de frontend

La coordinación sincrónica y asincrónica de los miembros, regida por los estatutos de la organización.

## Capa de Economía e Información

La capa de E&I se aloja en el sustrato, se sindica con la capa de Registro, y facilita el cumplimiento del pacto.

### Nivel de protocolo

Cada plataforma económica o de información tiene un protocolo diseñado para el intercambio que se realiza (por ejemplo, agricultura, un juego o citas de investigación).

### Nivel de orquestador

E&I debe ejecutarse sobre hardware revocable, obtenido y registrado por la capa de sustrato.

### Nivel de frontend

Los diseños de frontend de las plataformas de E&I deben ser personalizables por el usuario.

## Las líneas que no pueden cruzarse

Una implementación que cruce cualquiera de estas no es un JFA más pequeño; es software distinto que lleva el nombre.

1. El dinero se crea en el momento del intercambio — un saldo baja, otro sube, sumando siempre cero.
2. El crédito se gana, nunca se compra, y nunca es canjeable por dinero fiat.
3. La moneda de cada comunidad es soberana — sin unidad compartida, sin conversión entre comunidades.
4. El valor se queda en casa; solo la verdad cruza.
5. El intercambio entre comunidades son dos gastos soberanos ligados atómicamente por la cadena pública — sin cámara de compensación, sin tipo de cambio.
6. El registro es de solo adición — el daño se perdona anotando, nunca borrando.
7. Sin narrativas ni identidades en el registro compartido — solo hashes, tipos, marcas de tiempo y referencias.
8. La reputación nunca es un número único — lo que los demás ven es el recuento de intercambios en cada nivel de calificación.
9. La reputación decide si un miembro comercia sobre confianza; un límite común a toda la comunidad, fijado por el operador y nunca derivado de la reputación, decide cuánto.
10. Un despliegue comienza en depósito de garantía (escrow) — colateralizado, sin saldos negativos, sin crédito extendido entre contrapartes — y pasa a un sistema de crédito mutuo híbrido o pleno solo después de que el operador desarrolle capacidad, se notifique a la red de prosumidores, y las autorizaciones locales para prestar servicios de crédito mutuo se publiquen en la capa de gobernanza — o, cuando la jurisdicción no exija ninguna, se publique allí en su lugar una constatación de ese hecho.
11. Ningún host, cuenta o proveedor único cuya remoción pudiera detener la red.
12. Las posiciones y el historial de un miembro sobreviven a cualquier frontend; los registros de una comunidad sobreviven a cualquier operador.

## Referencias

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

Network Theory Applied Research Institute. (2025a, octubre). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, junio). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

Toffler, A. (1980). *The Third Wave*. William Morrow.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*
