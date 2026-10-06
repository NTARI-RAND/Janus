> Traducción comunitaria (borrador) — Política P2-002 de NTARI, Difusión Multilingüe Global. Fuente: P1-004_Substrate-Constraints_v0.1.md (original en inglés, instantánea del 2026-10-05). Borrador comunitario asistido por máquina, pendiente de revisión por el mantenedor regional conforme a P2-002 §3.1. Las especificaciones técnicas centrales permanecen en inglés conforme al §2.2.
>
> **El instrumento operativo es el texto en inglés, P1-004_Substrate-Constraints_v0.1.md. Esta traducción se ofrece para facilitar la comprensión y no tiene efecto jurídico alguno; donde difiera del inglés, prevalece el inglés.**
>
> ¿Encontraste un error en esta traducción? Tu corrección es una contribución
> bienvenida y valorada: haz un fork del repositorio del proyecto de NTARI
> (https://github.com/NTARI-RAND/Janus) y abre un pull request, o escríbenos a
> info@ntari.org.

# Enrutado, no negociado: el sustrato residencial bajo las restricciones de las operadoras

**Network Theory Applied Research Institute**
ID del documento: P1-004 · Versión: 0.1 (Borrador) · Septiembre de 2026

*Complemento del documento oficial de la Arquitectura de Doble Faz (Janus Facing Architecture). Este artículo analiza; nunca gobierna. Donde recomienda una regla, la regla entra en vigor únicamente mediante enmienda del documento oficial conforme al §9.2 de los estatutos y de su registro conforme al §9.16.*

## Resumen

La Arquitectura de Doble Faz sitúa su capa de sustrato en hardware de consumo alojado en hogares, oficinas y depósitos. Tres hechos físicos de la banda ancha de consumo se oponen a ello: las conexiones llevan direcciones dinámicas detrás de una traducción de direcciones de red a escala de operadora (CGNAT), sus políticas de uso aceptable prohíben los servidores de entrada, y su ancho de banda de subida es una fracción del de bajada. Un cuarto hecho se opone al modelo de confianza: un host con posesión física de una máquina puede leer su memoria, y las funciones de ejecución confidencial que lo impedirían están ausentes de los procesadores de consumo por decisión de los fabricantes.

Este artículo sostiene que las restricciones de las operadoras se tratan mejor como un entorno físico adverso que se sortea en código, y no como una condición de política que se negocia por la vía jurídica, y expone el argumento empírico a favor de esa elección. Luego establece lo que sortearlas exige en realidad, separa las partes que la técnica resuelve de las que no resuelve, y deja constancia de una cuestión jurídica que ningún diseño de protocolo puede responder.

## 1. La elección del terreno

Hay dos maneras de responder a una restricción impuesta por una operadora de red. Cambiar las obligaciones de la operadora mediante la ley y la regulación, o construir software que no necesite que la operadora cambie. La propia investigación de la arquitectura indica de cuál cabe esperar resultados.

El trabajo de NTARI sobre la velocidad de la información democrática describe un desajuste estructural: la información y la infraestructura se mueven a velocidad de red mientras la síntesis democrática sigue atada a los ciclos electorales (NTARI, 2025a). El efecto de la Reina Roja de Acemoglu y Robinson nombra la consecuencia: cuando un corredor deja atrás al otro, se pierde el corredor (Acemoglu & Robinson, 2019). La regulación de la banda ancha en Estados Unidos es un ejemplo nítido. Dos décadas de reglamentación disputada sobre la neutralidad de la red terminaron el 2 de enero de 2025, cuando el Sexto Circuito anuló en su totalidad la orden de 2024 de la Comisión Federal de Comunicaciones (FCC), al sostener que la Comisión carecía de autoridad legal para clasificar la banda ancha como servicio de telecomunicaciones (Ohio Telecom Association v. FCC, 2025). Apoyándose en Loper Bright, el tribunal eliminó la deferencia que había permitido a la regla sobrevivir a impugnaciones anteriores. Lo que queda a nivel federal es un régimen de divulgación: la Comisión puede exigir a un proveedor que publique sus prácticas de gestión del tráfico y no puede prohibirlas. Ocho estados legislan en ese vacío, lo que significa que actualmente no existe una respuesta jurídica uniforme a nivel nacional y que los permisos de un despliegue dependen de dónde se ubiquen sus nodos.

Ese historial no es un argumento contra la participación cívica. Es un argumento contra la dependencia. Un protocolo cuya viabilidad espera una regla favorable es un protocolo que deja de funcionar durante años, y las contrapartes en ese terreno son empresas establecidas cuya capacidad de cabildeo supera la de este instituto en órdenes de magnitud. El software escrito para funcionar bajo los términos que las operadoras ya imponen funciona hoy y sigue funcionando sea cual sea el rumbo de la regla.

**La posición.** Las restricciones de las operadoras son, a efectos de diseño, una restricción física inmutable. El cabildeo puede continuar como asunto cívico, y este artículo no toma posición en su contra, pero nunca es una dependencia de la arquitectura y ningún plan de despliegue puede dar por sentado su éxito.

Una salvedad corresponde aquí y no en una nota al pie. Esta elección está disponible para las tres restricciones siguientes porque cada una tiene una respuesta técnica. No está disponible para toda restricción, y la última sección del artículo nombra una en la que no lo está.

## 2. Alcanzabilidad sin servidor

**La restricción.** Una conexión residencial no es un entorno de alojamiento. Su dirección cambia, suele estar detrás de una traducción de direcciones de red a escala de operadora que no ofrece ninguna ruta de entrada, y su política de uso aceptable por lo general prohíbe ejecutar servidores. La política residencial de Comcast es representativa: prohíbe el equipo que proporcione «contenido de red o cualquier otro servicio a cualquier persona fuera de la LAN de sus Instalaciones, salvo para su uso residencial personal y no comercial», y menciona como ejemplos el alojamiento web, el intercambio de archivos y los servidores proxy (Comcast, 2021).

**Lo que la técnica responde.** Todo lo relativo a la alcanzabilidad. Un nodo que nunca acepta una conexión entrante no se ve afectado por el direccionamiento dinámico, ni por la traducción a escala de operadora, ni por la prohibición de servidores de entrada, porque nada de eso restringe las conexiones salientes. El nodo abre la conexión hacia el coordinador, la mantiene o la reabre según un calendario, y solicita trabajo.

El protocolo de referencia ya tiene esta forma y no necesitó cambios. Sus operaciones del lado del nodo son `SubmitListing`, `Heartbeat`, `PollJobs`, `Decline`, `ReportJob` y `Fees`, y cada una de ellas es una solicitud que inicia el nodo. El coordinador implementa una interfaz intercambiable y responde; nunca llama al nodo. Lo que faltaba no era el mecanismo sino el compromiso. Una propiedad que se cumple por accidente de la implementación actual puede perderse en la próxima refactorización, de modo que el documento oficial ahora la enuncia y el registro la vincula:

> Los nodos se incorporan a ese mercado mediante superposiciones cifradas (overlays) y sondeo saliente (polling), sin requerir puertos de entrada abiertos ni una dirección estática; basta la conexión tal como la entrega un proveedor residencial. La línea 11 depende de ello: un sustrato que solo funcionara donde un proveedor permite el servicio entrante cargaría con un punto de estrangulamiento en cada proveedor.

Registrada como `SUB-no-inbound-requirement`, vinculada a la implementación. Un repositorio la vincula al publicar pruebas que citen el identificador y demuestren que un nodo completa el ciclo de empleo completo —registro, latido, sondeo, ejecución, informe— sin socket de escucha, sin dirección estática y con una dirección traducida y cambiante delante. Mientras tales pruebas no existan, la invariante se informa como no vinculada conforme al §9.15 de los estatutos, y la afirmación de este artículo sobre la implementación de referencia es exactamente la autodeclaración que el §9.6 se niega a reconocer.

El razonamiento de la línea 11 es la parte sustantiva, y es la razón por la que esto pertenece al documento y no a una guía de despliegue. La línea 11 prohíbe cualquier host, cuenta o proveedor único cuya remoción pudiera detener la red. Un sustrato que requiriera servicio entrante solo funcionaría donde una operadora lo permite, lo que convertiría a cada operadora en un veto: un punto de estrangulamiento por proveedor, distribuido en apariencia y centralizado de hecho.

**Tres notas sobre el mecanismo.** Primero, sobre el transporte: las conexiones HTTPS y WebSocket ordinarias en el puerto 443 son el medio adecuado porque es lo que la ruta de red permite de forma fiable y lo que todo cliente web ya emite. Este artículo deliberadamente no describe ese tráfico como disfrazado. No es camuflaje; es el protocolo estándar para la tarea, y la honestidad importa porque el encuadre del camuflaje invita a creer que una medida técnica ha respondido una cuestión de permiso, y la sección 5 muestra que no lo ha hecho.

Segundo, sobre la versión seis del protocolo de internet: elimina la traducción a escala de operadora allí donde ambos extremos la tienen, y su adopción superó la mitad del tráfico de Google a nivel mundial el 28 de marzo de 2026, con Estados Unidos cerca del 57 por ciento (Google, 2026). Vale la pena usarla y vale la pena no exigir nada de ella. El direccionamiento universal no es lo mismo que la alcanzabilidad universal: una dirección enrutable globalmente sigue estando detrás de un cortafuegos que descarta los paquetes entrantes no solicitados, y un nodo que suponga lo contrario falla en la otra mitad de las conexiones. La versión seis es una optimización de la postura saliente, nunca un reemplazo de ella.

Tercero, sobre las redes superpuestas cifradas. Las superposiciones en malla son una respuesta real para las rutas de nodo a nodo que el coordinador no debería mediar, y existen implementaciones con nombre propio. No pueden entrar en el módulo de protocolo. El principio de código escueto limita el software de protocolo a la biblioteca estándar de su lenguaje para que siga siendo auditable en su totalidad, y el protocolo de referencia cumple actualmente esto de forma estricta: su módulo no declara ninguna dependencia, que es la propiedad que impide que cualquier coordinador único se convierta en un centro. Una biblioteca de superposición de gran tamaño dentro de ese módulo acabaría con ello. Por lo tanto, una superposición pertenece por debajo del protocolo como transporte a nivel de despliegue, elegida para cada despliegue y reemplazable, o se implementa de forma mínima dentro de la hoja. La redacción del documento es deliberadamente genérica por la misma razón por la que el documento no incluye nombres de productos.

Hay una tensión relacionada que el instituto no debería disimular. El despliegue del coordinador de referencia está actualmente detrás de una única red comercial de distribución de contenidos, y el diseño de transporte de la pila agrícola da por sentado el túnel de ese proveedor. Eso es conveniente, no es conforme con el espíritu de la línea 11, y es un punto de estrangulamiento exactamente del tipo que esta sección elimina en la capa de la operadora mientras lo deja en pie una capa más arriba. Queda fuera del alcance de este artículo y corresponde a la lista de problemas abiertos del sustrato.

## 3. Asimetría del ancho de banda

**La restricción.** Las conexiones de consumo son asimétricas por diseño, a menudo de diez a uno o peor, y cada vez más a menudo con tarificación por consumo. Un nodo no puede servir como origen general de contenidos, y una carga de trabajo que envíe imágenes grandes a cada host pasará su tiempo en transferencia en lugar de en cómputo.

**Lo que la técnica responde.** La mayor parte, manteniendo pequeñas las cargas útiles en lugar de moverlas más rápido. Tres decisiones de diseño hacen el trabajo, y sus efectos se multiplican.

**El tráfico de coordinación es pequeño por construcción.** La línea 7 mantiene las narrativas y las identidades fuera del registro compartido: solo hashes, tipos, marcas de tiempo y referencias. Un mínimo de privacidad adoptado por razones de privacidad tiene una consecuencia en el ancho de banda: el tráfico de la capa de Registro está acotado por el tamaño de los hashes y los encabezados y no por el tamaño de lo que se intercambió. El contenido se queda con las partes. Los mensajes de coordinación que sostienen el mercado son un puñado de estructuras firmadas sobre una codificación canónica de bytes. Nada de esto sobrecarga un enlace de subida doméstico, y es en este sentido que los paquetes son ligeros: las transmisiones propias de la arquitectura son ligeras porque una línea que no puede cruzarse las obliga a serlo.

**El trabajo se envía como módulos aislados (sandbox), no como imágenes de máquina.** Esta es la única recomendación de este artículo que pide a la implementación de referencia que cambie en lugar de mantener su forma. El agente de nodo actual ejecuta los trabajos mediante un ejecutor de contenedores, lo que significa que un primer trabajo en un nodo nuevo descarga capas que se miden en cientos de megabytes antes de que empiece cualquier trabajo. Un módulo WebAssembly para la misma tarea se mide en megabytes o menos, arranca en milisegundos, lleva un modelo de capacidades de denegación por defecto en lugar de uno de exclusión voluntaria, y es portable a través del hardware de consumo heterogéneo que el sustrato espera, en lugar de requerir una arquitectura coincidente. Un entorno de ejecución sin dependencias nativas mantiene el agente de nodo auditable con el mismo espíritu que el módulo de protocolo. Los contenedores deberían seguir disponibles para las cargas de trabajo que realmente necesitan un entorno operativo completo, en nodos cuyas conexiones y operadores puedan soportarlos, y deberían dejar de ser la opción por defecto. La contrapartida es real y debe enunciarse: WebAssembly cuesta algo de rendimiento frente a la ejecución nativa y no puede alojar software existente arbitrario sin modificarlo. Para el trabajo irregular, ligero, de sensores y coordinación —el patrón agrícola al que esta arquitectura sirve primero—, esa contrapartida es favorable.

**Los trabajos se encolan localmente.** Un nodo guarda su cola y sus informes pendientes en un almacén local integrado y los vacía cuando la conexión lo permite. La consecuencia es que un enlace de subida deficiente retrasa el trabajo en lugar de perderlo, y una conexión intermitente deja de ser motivo de descalificación. Esto importa más allá del ancho de banda: el piloto agrícola ya prevé las brechas de conectividad rural con captura de datos sin conexión y sincronización posterior, y la misma propiedad hace que un nodo en ese entorno sea un participante y no una carga.

Ninguna de estas tres es una invención novedosa y ninguna está registrada como invariante. Son postura de diseño, consignadas aquí para que un despliegue pueda evaluarse frente a ellas y para que el razonamiento sobreviva a las personas que lo tuvieron. La junta podría considerar si la opción por defecto de módulo en lugar de imagen debería convertirse en una invariante registrada; este artículo todavía no lo recomienda, porque la implementación de referencia no la cumple hoy y un registro que se adelanta al código enseña una lección equivocada sobre lo que significa el registro.

## 4. Ejecución en hardware que controla el host

**La restricción.** Un prosumidor que aloja un nodo tiene la posesión física de la máquina. Puede leer su memoria, inspeccionar su disco y observar lo que calcula. La respuesta convencional es la ejecución confidencial por hardware, y no está disponible en esta capa por una cuestión de estrategia de producto de los fabricantes y no de costo. Intel declaró obsoletas las Software Guard Extensions en los procesadores de cliente a partir de la undécima generación de su línea Core y las conserva en los componentes para servidores y nube (Intel, 2021). La Secure Encrypted Virtualization de AMD, incluida la generación con paginación anidada, es una función de servidor EPYC y no está presente en Ryzen ni en Threadripper (AMD, 2021). Exigir cualquiera de las dos excluiría prácticamente todo el hardware de consumo y volvería a admitir precisamente el control de acceso de los centros de datos que la capa de sustrato existe para desplazar. Exigir enclaves no aseguraría el sustrato común; lo aboliría.

**Lo que la técnica responde, y hasta dónde.** No la confidencialidad frente a un host decidido. En esta sección cambia el método del artículo, y decirlo con claridad es más útil que una solución alternativa presentada con más confianza de la que merece.

La respuesta disponible para la arquitectura no es confiar en el host, sino hacer que la deshonestidad sea visible y costosa, usando la maquinaria que la pila ya se debe a sí misma. Tres partes:

**Ejecución redundante con desacuerdo calificado.** Un trabajo con consecuencias se despacha a dos o más hosts independientes y se comparan sus resultados. El acuerdo es evidencia; el desacuerdo es un evento que entra en el pacto, donde la calificación más baja de la escala ya significa que una parte fue perjudicada, explotada o atendida con intención maliciosa. El mecanismo de cumplimiento existe: la función de testigo es trabajo compensado del sustrato, y el sustrato debe un tipo de trabajo en el que los testigos se asignan al azar para que ninguna de las partes de un intercambio pueda elegir a su testigo. La ejecución redundante es ese mismo patrón de mercado aplicado al cómputo en lugar de al mantenimiento de registros, y la asignación aleatoria es lo que hace que la colusión entre los ejecutores de un trabajo sea cuestión de azar y no de elección. El costo es un múltiplo del cómputo, pagado deliberadamente para la clase de trabajo que lo justifica, y compra detección y no prevención: la misma postura que la capa de Registro ya adopta frente a la manipulación.

**La minimización de datos como control principal.** Un host no puede extraer lo que nunca llega. La línea 7 ya mantiene las identidades y las narrativas fuera del registro compartido; la disciplina correspondiente en la capa de sustrato es que un trabajo lleve los menos datos que le permitan completarse, que las entradas sensibles se repartan entre hosts cuando el trabajo lo permita, y que una carga de trabajo que requiera un gran cuerpo coherente de datos sensibles sobre personas identificables sea una carga de trabajo para hardware cuyo operador rinda cuentas por ella. Esa última cláusula es un límite real del alcance del sustrato y debe enunciarse como tal en lugar de sortearse mediante ingeniería.

**La atestación como capacidad opcional, con precio y calificada.** Cuando un comprador necesita realmente confidencialidad respaldada por hardware, la respuesta es un mercado, no un mandato. Un host con ese hardware anuncia la capacidad como parte de su oferta, los compradores que la necesitan pagan por ella, y la afirmación queda sujeta a la misma calificación del pacto que cualquier otra declaración que haga un host. Esto mantiene el piso abierto al hardware de consumo mientras permite que el techo suba dondequiera que un host haya invertido, y sitúa la decisión en la parte que asume el riesgo.

**Estado.** Esta es la parte de la revisión de septiembre de 2026 que no está resuelta. La posición anterior está argumentada, no adoptada: no hay ninguna invariante registrada, y un identificador candidato para la ejecución redundante consta en el registro de preguntas abiertas como decisión que corresponde a la junta conforme al §9.16. Registrarlo obligaría al sustrato a construir un tipo de trabajo que no ha construido. El estado honesto es que la arquitectura tiene una respuesta coherente a la observación por parte del operador del host y todavía no se ha comprometido con ella.

## 5. Lo que la técnica no responde

El sondeo saliente elimina por completo el problema de los servidores de entrada. No elimina el problema del uso aceptable, y este artículo engañaría a sus lectores si diera a entender lo contrario.

Léase de nuevo la política representativa. Prohíbe el equipo que sirva a cualquier persona fuera de la red de las instalaciones «salvo para su uso residencial personal y no comercial». La prohibición de servidores de entrada es un enunciado sobre puertos y se responde no usando ninguno. La vertiente no comercial es un enunciado sobre la compensación, y la compensación es precisamente lo esencial: un prosumidor que aloja sustrato recibe un pago, en dinero fiat en la implementación actual y en crédito comunitario más adelante. Ninguna elección de transporte, número de puerto ni cifrado cambia ese hecho, y un diseño que afirme haberlo sorteado ha confundido un mecanismo con un permiso. La cuestión es si la participación compensada en una línea residencial activa esa vertiente, y la respuesta es una interpretación de términos contractuales en una jurisdicción, no una propiedad del software.

El instituto debería someterla a revisión de un asesor jurídico, y la ocasión natural está a mano: el piloto combinado de calor y cómputo ya tiene ante el asesor jurídico dos preguntas abiertas sobre si un nodo que genera ingresos en un hogar cambia la posición del hogar frente a su aseguradora bajo las exclusiones por uso comercial. La cuestión de los términos de la operadora es la misma pregunta dirigida a un contrato distinto, y debería ir en el mismo paquete en lugar de esperar uno propio. Vale la pena nombrar ya sus formas prácticas: si se requiere una conexión de categoría empresarial, si se sostiene un planteamiento de minimis o de reparto de costos, si la respuesta varía tanto según la operadora que la orientación para los operadores de nodos deba ser regional, y qué le dice un despliegue a los posibles hosts antes de que se inscriban.

La última de ellas es un asunto del pacto tanto como un asunto jurídico. Un prosumidor tiene derecho a saber qué puede significar la participación para su propio contrato de servicio antes de asumirla, y el propio compromiso de la arquitectura con una relación calificada y divulgada entre operador y prosumidor hace que el silencio sobre este punto sea la opción por defecto equivocada.

## 6. Dónde quedó esto

| Nivel | Qué cambió | Cumplimiento |
|---|---|---|
| Documento oficial | El nivel de protocolo del sustrato enuncia la postura saliente, sin requisito de conexiones entrantes, y la vincula a la línea 11 | El conjunto de pruebas (suite) verifica el texto; pasa con 26 invariantes |
| Registro de conformidad | Se añadió `SUB-no-inbound-requirement`, vinculada a la implementación | No vinculada hasta que las pruebas de nodo citen el identificador (§9.15) |
| Registro de preguntas abiertas | La entrada 9 consigna la restricción, las resoluciones, la parte abierta y la cuestión jurídica | §9.3 |
| Este artículo | La postura sobre ancho de banda y ejecución confidencial, argumentada y no vinculada | Ninguno; analiza y no gobierna |

Dos obligaciones de procedimiento acompañan al cambio del documento y no quedan satisfechas por este artículo. Una enmienda del documento oficial y de su registro se tramita conforme a los §9.2 y §9.16 de los estatutos, y durante el arranque (bootstrap) la junta fundadora ejerce esa facultad, con cada acto consignado en el registro de gobernanza como acto de arranque conforme al §16.1, abierto a la membresía como cualquier otra decisión. El conjunto de pruebas pasa con el texto enmendado, como exige el §9.2 antes de la adopción, y las versiones en siete idiomas conforme a P2-002 se actualizaron junto con el original en inglés.

## Fuentes

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

AMD. (2021, 15 de marzo). *AMD EPYC 7003 series processors set new standard*. https://www.amd.com/en/newsroom/press-releases/2021-3-15-amd-epyc-7003-series-cpus-set-new-standard-as-hig.html

Comcast. (2021, 1 de febrero). *Acceptable use policy for Xfinity Internet (residential)*. https://www.xfinity.com/corporate/customers/policies/highspeedinternetaup

Google. (2026). *IPv6 adoption statistics*. https://www.google.com/intl/en/ipv6/statistics.html

Intel. (2021). *Intel SGX deprecation on client processors* [discusión en Intel Community]. https://community.intel.com/t5/Intel-Software-Guard-Extensions/Intel-SGX-deprecated-in-11th-Gen-processors/m-p/1351848

Internet Society. (2026, abril). *18 years later, IPv6 reaches majority*. https://pulse.internetsociety.org/en/blog/2026/04/18-years-later-ipv6-reaches-majority/

Network Theory Applied Research Institute. (2025a, octubre). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, junio). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

*Ohio Telecom Association v. FCC*, Nos. 24-7000 et al. (6th Cir. Jan. 2, 2025). Análisis del Congressional Research Service: https://www.congress.gov/crs-product/LSB11264

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*Especificación: CC BY-SA 4.0*
