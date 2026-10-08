> Traducción comunitaria (borrador) — Política P2-002 de NTARI, Difusión Multilingüe Global. Fuente: janus-facing-architecture.md (original en inglés, instantánea del 2026-10-08). Borrador comunitario asistido por máquina, pendiente de revisión por el mantenedor regional conforme a P2-002 §3.1. Las especificaciones técnicas centrales permanecen en inglés conforme al §2.2.
>
> ¿Encontraste un error en esta traducción? Tu corrección es una contribución
> bienvenida y valorada: haz un fork del repositorio del proyecto de NTARI y
> abre un pull request, o escríbenos a info@ntari.org.

# JFA: Arquitectura de Doble Faz (Janus Facing Architecture)

## Introducción

Cada miembro de una economía es un **prosumidor** — no solo consumidor, sino a la vez productor de algo de valor, aunque lo único que tenga por ofrecer sea su tiempo (Toffler, 1980). Nadie está en un solo lado de un intercambio; las dos caras son la misma persona.

La Arquitectura de Doble Faz (Janus Facing Architecture) lleva el nombre del dios romano que mira en dos direcciones a la vez, porque eso es lo que hace todo prosumidor: cada uno enfrenta exigencias tanto de producción como de consumo, al mismo tiempo. Permite a las comunidades atender la realidad económica del prosumo, y ofrece la opción de transformar el modelo de emisión: de dinero chartal exógeno — emitido por una autoridad externa a la comunidad (Knapp, 1924) — a crédito mutuo endógeno, emitido por los miembros entre sí a medida que transaccionan (Moore, 1988; Greco, 2009).

La segunda faz del nombre es política. Acemoglu y Robinson (2019) muestran que la libertad sobrevive únicamente dentro de un corredor estrecho, donde un Estado capaz — el Leviatán — se ve igualado por una sociedad igualmente capaz de controlarlo. Fuera del corredor, el Leviatán adopta sus otras formas: ausente, y la coordinación fracasa; despótico, y quien coordina domina a los coordinados; de papel, y los controles existen por escrito pero no en la práctica. Permanecer dentro del corredor exige lo que ellos llaman el efecto de la Reina Roja: Estado y sociedad corriendo juntos, cada uno acrecentando su capacidad porque el otro lo hace. Toda plataforma económica es un Leviatán en miniatura — coordina, hace cumplir y registra — y las plataformas dominantes de hoy son despóticas por construcción: evolucionan a la velocidad de la red mientras las instituciones destinadas a controlarlas se mueven a la velocidad de las reuniones.

La investigación de NTARI sitúa este fracaso en la infraestructura misma. Los sistemas deliberativos son cultura material: la arquitectura de una plataforma materializa una teoría sobre quién puede saber y quién puede decidir, y las arquitecturas de difusión predominantes tratan a los participantes como receptores pasivos (NTARI, 2025b). La brecha de velocidad resultante es estructural: la información se mueve a velocidad de red mientras la síntesis democrática sigue atada a ciclos electorales sincronizados por un reloj postal (NTARI, 2025a). JFA está construida para cerrar esa brecha desde dentro, disciplinada capa por capa por el costo de marcharse. Es un Leviatán encadenado en código.

La Arquitectura de Doble Faz (JFA) se organiza en cinco capas funcionales — Sustrato, Registro, Pacto, Gobernanza, y Economía e Información (E&I) — cada una implementada en tres niveles: el frontend, para la colaboración entre prosumidores; el orquestador, un backend que provee coordinación superpuesta entre comunidades geográficas; y el protocolo subyacente, el patrón para manejar datos de forma segura entre niveles.

El software de JFA está diseñado para publicarse y gestionarse en un entorno copyleft, generalmente la Licencia Pública General Affero de GNU, versión 3 o posterior (AGPL-3.0-or-later), lo que permite que nuevos frontends, federaciones, protocolos y arquitecturas evolucionen en el mercado global, formando un común de software libre.

Este es el documento oficial, custodiado por Network Theory Applied Research Institute, Inc. Los instrumentos anteriores se conservan en [Historical Docs](Historical%20Docs/); los conceptos heredados de ellos constan en el [triaje de conceptos](jfa-concept-triage-2026-08-24.md); lo que sigue sin resolver se nombra en [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## Por qué importa

Todo sistema que coordina personas ejerce poder sobre ellas, lo pretenda o no. Eso no es un defecto; la coordinación lo requiere. Pero el poder solo se mantiene sano cuando algo lo controla — no un control de papel, sino personas reales con intereses reales, lo bastante cerca para actuar. La mayoría de las plataformas se mueven hoy a la velocidad de la red mientras todo lo construido para pedirles cuentas se mueve a la velocidad de las reuniones, y un control que llega tarde no es control en absoluto. La respuesta de JFA es dejar de tratar la coordinación y la rendición de cuentas como dos sistemas: el mismo software, las mismas personas, la misma velocidad.

## Principios

**Responsabilidad compartida.** La comunidad que coordina la economía es la misma comunidad que controla esa coordinación. Las dos funciones se intercambian de forma continua, nunca se separan en gobernantes y gobernados.

**Disciplina institucional.** Cada capa se disciplina por el costo de abandonarla — lo que un miembro pierde al marcharse, y lo que una comunidad pierde al expulsar a alguien. Donde marcharse es barato, disciplina la competencia: las capas de Sustrato y de Economía e Información. Donde marcharse es costoso, los miembros votan: las capas de Pacto y de Gobernanza. Donde marcharse es catastrófico, las decisiones quedan abiertas a impugnación: la capa de Registro. Cada capa nombra abajo su propio costo, porque ese costo es lo que decide cómo se zanja una disputa en ella.

**Código escueto y auditable.** El software de protocolo se mantiene pequeño, no depende de nada más que de la biblioteca estándar de su lenguaje, y es auditable en su totalidad.

## Capa de Sustrato

Es el hardware donde todo ocurre, propiedad de prosumidores de CPU, GPU, impresoras, almacenamiento y sensores.

Salir de aquí es barato, y la negativa de un transportista no le cuesta a un prosumidor más que una conexión. Un orquestador que se niega a transportar tu capacidad no se ha llevado tu hardware, tus saldos ni tu historial, y otro orquestador está a una oferta publicada de distancia. Las querellas en esta capa, por tanto, no se adjudican: un transporte que queda sin atestar dentro de su ventana de compromiso simplemente se revierte, nadie falla sobre él, y a un transportista que se niega o falla con demasiada libertad se lo desbanca con una oferta mejor en lugar de apelar ante él.

### Nivel de protocolo

Intercambia instrucciones y órdenes a través de un mercado distribuido de cómputo y almacenamiento operado en computadoras de consumo alojadas en hogares, oficinas y depósitos, así como en equipo industrial reacondicionado.

Los nodos se incorporan a ese mercado mediante superposiciones cifradas (overlays) y sondeo saliente (polling), sin requerir puertos de entrada abiertos ni una dirección estática; basta la conexión tal como la entrega un proveedor residencial. La línea 11 depende de ello: un sustrato que solo funcionara donde un proveedor permite el servicio entrante cargaría con un punto de estrangulamiento en cada proveedor.

El trabajo del sustrato tiene asegurada la integridad, no la confidencialidad: un host puede leer lo que computa su nodo. El trabajo cuyo resultado liquida un gasto o entra en el registro se ejecuta en al menos dos hosts independientes, y su desacuerdo se califica, nunca se le da confianza.

### Nivel de orquestador

Capacidad de cómputo federada de prosumidores, que crea más opciones a lo largo de la geografía. Los orquestadores publican ofertas de transporte en el mercado del sustrato, cada una nombrando una tarifa, un compromiso de entrega y una clave pública; cualquier plataforma puede seleccionar cualquier orquestador alcanzable, de modo que a un transportista dominante se lo desbanca en lugar de regularlo. El transporte es entrega, no ejecución: un orquestador lleva gastos firmados al conjunto de testigos y devuelve atestaciones, nunca se confía en él para determinar si un intercambio ocurrió, y puede ser con pérdidas y basado en reintentos.

### Nivel de frontend

Interfaz de Economía e Información para prosumir cómputo y almacenamiento.

## Capa de Registro

Una función compensada del sustrato, que registra y sirve el diálogo entre las capas de Economía e Información y de Pacto para el público.

El registro de lo ocurrido lo guardan seis partes: los dos prosumidores del intercambio, el operador, el orquestador y dos testigos conservan cada uno un registro propio. Los hashes se comprometen además a una cadena pública única, distribuida a través del sustrato — el registro para todos quienes no guardan ninguno propio. Los compromisos de cada intercambio transportado por un orquestador se copian a la cadena y se almacenan en sustrato financiado por la organización de custodia de la capa de Gobernanza, de modo que el registro que liga a las comunidades entre sí no lo paga ninguna de ellas. La cadena es de solo adición: el daño se perdona mediante anotación, nunca borrando. Una plataforma debe tener al menos dos testigos independientes; con menos, un despliegue debe etiquetarse a sí mismo como no federado. Los testigos se asignan mediante un sorteo sembrado desde la cadena pública, que cualquiera puede verificar, y los paga el mercado del sustrato, nunca el operador al que observan.

Nadie puede ser borrado del registro, y abandonarlo es catastrófico. Lo comprometido nunca se borra, pero ninguna copia única es el registro, y cada copia dura solo mientras se conserva: la del orquestador, con el último transporte pagado; las de los testigos, mientras su almacenamiento esté pagado; las propias de los prosumidores y del operador, hasta que dejen de conservarlas; y la de la cadena, mientras su almacenamiento esté financiado. El registro sobrevive en las copias que queden; la cadena la almacena el sustrato y no el operador, de modo que puede sobrevivir al operador, al frontend y a la querella, y lo que lleva más allá de cada custodio es el hecho del compromiso, no el contenido. Como nada puede borrarse del registro, ninguna constatación aquí es jamás definitiva: una entrada disputada se responde mediante anotación, y la anotación es tan permanente como la entrada a la que responde.

Un intercambio entre comunidades sigue siendo dos gastos soberanos. La cita que lo liquida lleva también la tarifa de transporte del orquestador, puesta en depósito de garantía (escrow) con el intercambio al iniciarse y liberada por esa misma cita. La liberación es conjunta y de todo o nada — si la entrega no se atesta dentro de la ventana de compromiso de la oferta, todos los gastos se revierten — y la atestación propia del orquestador no cuenta para el umbral que libera su propia tarifa. La tarifa se reparte entre los libros mayores de origen de los dos prosumidores cuyo intercambio fue transportado, pagando cada uno su parte en su propia unidad; nada cruza una frontera comunitaria. El crédito que gana lo guardan las mismas seis partes, citado por clave. La entrega la atestan únicamente los testigos; el operador conserva su registro de un transporte y nunca lo atesta.

### Nivel de protocolo

Captura, categoriza y aplica hash a cada transmisión dentro de la pila, a fin de establecer reputación mediante la capa de Pacto y de sentar la base de un medio de intercambio mediante Economía e Información.

### Nivel de orquestador

Federa registros a lo largo de la geografía, habilitando reputación e intercambio compartidos. Lo que la federación comparte es verdad registrada — reputación e historial de intercambios — nunca una unidad monetaria.

### Nivel de frontend

La compra y venta de almacenamiento de registro a través del sustrato, compensando a los prosumidores que conservan el registro.

## Capa de Pacto

Un contrato social ejecutado en código, que informa expectativas flexibles para las interacciones entre prosumidores.

Salir de aquí es costoso. Un prosumidor vetado de una plataforma conserva el registro de cada calificación que ganó allí — seis partes lo guardan — pero la posición que ese registro conlleva no lo sigue por defecto: en la siguiente plataforma, el recuento de intercambios en cada nivel de calificación se reconstruye un intercambio atestiguado a la vez. Ese precio es la razón de que un veto descanse en evidencia adjudicada y no en la palabra de un operador. Cuando ocurren aparentes incumplimientos del pacto, los operadores de plataforma adjudican entre sus prosumidores; las disputas que cruzan plataformas, y las disputas entre un prosumidor y el operador de su propia plataforma, se adjudican en la capa de testigos — ningún operador adjudica una disputa de la que es parte. Dondequiera que ocurra la adjudicación, las partes de esta califican a quien adjudica — el operador entre sus propios prosumidores, los testigos en los demás casos — de modo que los árbitros están dentro del sistema de reputación que hacen cumplir.

Como salir es costoso, aquí los miembros votan: la federación del Pacto vota los cambios conceptuales y programáticos del pacto (la Escala de Evaluación de Intercambios Basada en Leveson, LBTAS), de su API y de su orquestación, y encarga estudios formales de los efectos del pacto elegido sobre sus usuarios.

### Nivel de protocolo

Una evaluación simple, escrita en código ejecutable, para que los prosumidores califiquen sus interacciones entre sí a lo largo de la pila.

### Nivel de orquestador

Una API que sirve evaluaciones conformes a través de los mercados de Economía e Información de la pila, desde prosumidores del sustrato.

### Nivel de frontend

La interfaz de Economía e Información donde se sirve la API.

## Capa de Gobernanza

Aquí es donde y cómo los seres humanos se reúnen para actuar colaborativamente sobre la pila.

Salir de aquí es costoso, y esta es la única capa donde la expulsión alcanza al software mismo: un miembro expulsado del Instituto pierde, por un plazo acotado, el voto que da forma a lo que todos los demás ejecutan. Por eso la expulsión nunca es decisión de un operador — se remite a la federación de Gobernanza y la decide el voto de sus miembros conforme a los estatutos, con constancia en el registro.

### Nivel de protocolo

Organización sin fines de lucro de custodia de software copyleft.

### Nivel de orquestador

La membresía en el Network Theory Applied Research Institute, obtenida operando una instancia federada de software JFA o participando como prosumidor en una plataforma federada.

### Nivel de frontend

La coordinación sincrónica y asincrónica de los miembros, regida por los estatutos de la organización.

## Capa de Economía e Información

La capa de Economía e Información se aloja en el sustrato, se sindica con la capa de Registro, y facilita el cumplimiento del pacto.

Salir de aquí es barato por construcción. Un operador puede vetar a un prosumidor de su plataforma, pero no de lo que construyó allí: las posiciones y el historial sobreviven a cualquier frontend, de modo que quien es vetado se va con su registro intacto y sus saldos aún debidos. Un veto es una pérdida de mercado, no una pérdida de posición — y un operador cuyos términos o límite de crédito expulsan a los prosumidores pierde el comercio en lugar de ganar la discusión.

### Nivel de protocolo

Cada plataforma económica o de información tiene un protocolo diseñado para el intercambio que se realiza (por ejemplo, agricultura, un juego o citas de investigación). Cada uno asume que cualquier host del sustrato puede leer lo que computa.

### Nivel de orquestador

La Economía e Información debe ejecutarse sobre hardware revocable, obtenido y registrado por la capa de sustrato. Una plataforma no necesita orquestador propio: selecciona uno del mercado del sustrato y paga el transporte con cargo al intercambio.

### Nivel de frontend

Los diseños de frontend de las plataformas de Economía e Información deben ser personalizables por el usuario.

## Las líneas que no pueden cruzarse

Una implementación que cruce cualquiera de estas no es un JFA más pequeño; es software distinto que lleva el nombre.

1. Todo crédito es un pagaré (IOU), creado en el momento en que dos miembros intercambian — un saldo baja, otro sube, sumando siempre cero. Esa es la única manera en que el dinero llega a existir: nada se acuña, nada se emite desde fuera, y nada se acumula como interés.
2. El crédito se gana, nunca se compra, y nunca es canjeable por dinero fiat.
3. La moneda de cada comunidad es soberana — sin unidad compartida, sin conversión entre comunidades.
4. El valor se queda en casa; solo la verdad cruza.
5. El intercambio entre comunidades son dos gastos soberanos ligados atómicamente por la cadena pública — sin cámara de compensación, sin tipo de cambio.
6. El registro es de solo adición — el daño se perdona anotando, nunca borrando.
7. Sin narrativas ni identidades en el registro compartido — solo hashes, tipos, marcas de tiempo y referencias.
8. La reputación nunca es un número único — lo que los demás ven es el recuento de intercambios en cada nivel de calificación.
9. La reputación decide si un miembro comercia sobre confianza; un límite común a toda la comunidad, fijado por el operador y nunca derivado de la reputación, decide cuánto.
10. Un despliegue comienza en depósito de garantía (escrow) — colateralizado, sin saldos negativos, sin crédito extendido entre contrapartes — y pasa a un sistema de crédito mutuo híbrido o pleno solo después de que el operador desarrolle capacidad, se notifique a la red de prosumidores, y las autorizaciones locales para prestar servicios de crédito mutuo se publiquen en la capa de gobernanza — o, cuando la jurisdicción no exija ninguna, se publique allí en su lugar una constatación de ese hecho — y de que un paso al crédito mutuo pleno sea ratificado por los prosumidores del despliegue.
11. Ningún host, cuenta o proveedor único cuya remoción pudiera detener la red.
12. Las posiciones y el historial de un miembro sobreviven a cualquier frontend; los registros de una comunidad sobreviven a cualquier operador.

## Referencias

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

Greco, T. H. (2009). *The End of Money and the Future of Civilization*. Chelsea Green Publishing.

Knapp, G. F. (1924). *The State Theory of Money*. Macmillan. (Obra original publicada en 1905)

Moore, B. J. (1988). *Horizontalists and Verticalists: The Macroeconomics of Credit Money*. Cambridge University Press.

Network Theory Applied Research Institute. (2025a, octubre). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, junio). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

Toffler, A. (1980). *The Third Wave*. William Morrow.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*Software: AGPL-3.0-or-later · Especificación: CC BY-SA 4.0*
