> Tradução comunitária (rascunho) — Política P2-002 da NTARI, Difusão Multilíngue Global. Fonte: P1-004_Substrate-Constraints_v0.1.md (original em inglês, instantâneo de 2026-10-05). Rascunho comunitário assistido por máquina, pendente de revisão pelo mantenedor regional conforme P2-002 §3.1. As especificações técnicas centrais permanecem em inglês conforme o §2.2.
>
> **O instrumento operativo é o texto em inglês, P1-004 v0.1. Esta tradução é fornecida para fins de compreensão e não tem efeito jurídico algum; onde divergir do inglês, prevalece o inglês.**
>
> Encontrou um erro nesta tradução? Sua correção é uma contribuição bem-vinda e
> valorizada: faça um fork do repositório do projeto da NTARI
> (https://github.com/NTARI-RAND/Janus) e abra um pull request, ou escreva para
> info@ntari.org.

# Roteado, não negociado: o substrato residencial sob as restrições das operadoras

**Network Theory Applied Research Institute**
ID do documento: P1-004 · Versão: 0.1 (Rascunho) · Setembro de 2026

*Acompanha o documento oficial da Arquitetura de Dupla Face. Este artigo analisa; nunca rege. Onde recomenda uma regra, a regra só entra em vigor por emenda do documento oficial conforme o §9.2 do estatuto e de seu registro conforme o §9.16.*

## Resumo

A Arquitetura de Dupla Face coloca sua camada de substrato em hardware de consumo instalado em residências, escritórios e depósitos. Três fatos físicos da banda larga de consumo se opõem a isso: as conexões têm endereços dinâmicos por trás da tradução de endereços de rede em nível de operadora, suas políticas de uso aceitável proíbem servidores de entrada, e sua largura de banda de envio é uma fração da de recebimento. Um quarto fato se opõe ao modelo de confiança: quem tem a posse física de uma máquina pode ler sua memória, e os recursos de execução confidencial que impediriam isso estão ausentes dos processadores de consumo por decisão dos fabricantes.

Este artigo sustenta que as restrições das operadoras são mais bem tratadas como um ambiente físico adversário a ser contornado em código, e não como uma condição de política a ser negociada juridicamente, e apresenta o argumento empírico para essa escolha. Em seguida, expõe o que contorná-las realmente exige, separa as partes que a técnica resolve das partes que ela não resolve, e registra uma questão jurídica que nenhum projeto de protocolo pode responder.

## 1. A escolha do foro

Há duas maneiras de responder a uma restrição imposta por uma operadora de rede. Mudar as obrigações da operadora por meio da lei e da regulação, ou construir software que não precise que a operadora mude. A própria pesquisa da arquitetura diz de qual delas se devem esperar resultados.

O trabalho da NTARI sobre a velocidade da informação democrática descreve um descompasso estrutural: a informação e a infraestrutura se movem na velocidade da rede, enquanto a síntese democrática permanece presa a ciclos eleitorais (NTARI, 2025a). O efeito da Rainha Vermelha de Acemoglu e Robinson nomeia a consequência — quando um dos competidores dispara à frente do outro, perde-se o corredor (Acemoglu & Robinson, 2019). A regulação da banda larga nos Estados Unidos é um exemplo nítido. Duas décadas de regulamentação contestada sobre a neutralidade da rede terminaram em 2 de janeiro de 2025, quando o Tribunal de Apelações do Sexto Circuito anulou integralmente a ordem de 2024 da Federal Communications Commission, entendendo que a Comissão não tinha autoridade legal para classificar a banda larga como serviço de telecomunicações (Ohio Telecom Association v. FCC, 2025). Com base em Loper Bright, o tribunal eliminou a deferência que havia permitido à regra sobreviver a contestações anteriores. O que resta em âmbito federal é um regime de divulgação: a Comissão pode exigir que um provedor publique suas práticas de gestão de tráfego e não pode proibi-las. Oito estados legislam nessa lacuna, o que significa que atualmente não existe uma resposta jurídica uniforme em âmbito nacional e que as permissões de uma implantação dependem de onde seus nós se encontram.

Esse histórico não é um argumento contra o engajamento cívico. É um argumento contra a dependência. Um protocolo cuja viabilidade espera por uma regra favorável é um protocolo que deixa de funcionar durante anos seguidos, e as contrapartes nesse foro são empresas estabelecidas cuja capacidade de lobby supera a deste instituto em ordens de grandeza. O software escrito para funcionar sob os termos que as operadoras já impõem funciona hoje e continua funcionando qualquer que seja o rumo da regra.

**A posição.** As restrições das operadoras são, para fins de projeto, uma restrição física imutável. O lobby pode prosseguir como questão cívica, e este artigo não toma posição contra ele, mas ele nunca é uma dependência da arquitetura, e nenhum plano de implantação pode presumir seu sucesso.

Uma ressalva pertence a este ponto, e não a uma nota de rodapé. Essa escolha está disponível para as três restrições abaixo porque cada uma tem uma resposta técnica. Ela não está disponível para toda restrição, e a seção final do artigo nomeia uma em que não está.

## 2. Alcançabilidade sem servidor

**A restrição.** Uma conexão residencial não é um ambiente de hospedagem. Seu endereço muda, ela costuma ficar por trás de uma tradução de endereços de rede em nível de operadora que não oferece caminho de entrada algum, e sua política de uso aceitável geralmente proíbe a execução de servidores. A política residencial da Comcast é representativa: proíbe equipamentos que forneçam "conteúdo de rede ou quaisquer outros serviços a qualquer pessoa fora da LAN de suas Instalações, exceto para seu uso residencial pessoal e não comercial", e cita como exemplos hospedagem de sites, compartilhamento de arquivos e servidores proxy (Comcast, 2021).

**O que a técnica responde.** Tudo o que diz respeito à alcançabilidade. Um nó que nunca aceita uma conexão de entrada não é afetado pelo endereçamento dinâmico, pela tradução em nível de operadora nem pela proibição de servidores de entrada, porque nenhuma dessas coisas restringe conexões de saída. O nó abre a conexão com o coordenador, mantém-na ou a reabre conforme um cronograma, e pede trabalho.

O protocolo de referência já tem esse formato e não precisou ser alterado. Suas operações do lado do nó são `SubmitListing`, `Heartbeat`, `PollJobs`, `Decline`, `ReportJob` e `Fees` — cada uma delas uma requisição que o nó inicia. O coordenador implementa uma interface plugável e responde; nunca disca para o nó. O que faltava não era o mecanismo, mas o compromisso. Uma propriedade que se mantém por acaso da implementação atual pode ser perdida na próxima refatoração; por isso, o documento oficial agora a enuncia e o registro a vincula:

> Os nós ingressam nesse mercado por meio de sobreposições cifradas (overlays) e sondagem de saída (polling), sem exigir portas de entrada abertas nem endereço estático; basta a conexão tal como um provedor residencial a entrega. A linha 11 depende disso: um substrato que só funcionasse onde um provedor permite serviço de entrada carregaria um ponto de estrangulamento em cada provedor.

Registrado como `SUB-no-inbound-requirement`, vinculado à implementação. Um repositório o vincula ao entregar testes que citem o identificador e provem que um nó completa o ciclo de trabalho completo — registrar, enviar heartbeat, sondar, executar, relatar — sem socket de escuta, sem endereço estático e com um endereço traduzido e mutável à sua frente. Até que tais testes existam, a invariante é relatada como não vinculada conforme o §9.15 do estatuto, e a afirmação deste artigo sobre a implementação de referência é exatamente a autodeclaração que o §9.6 se recusa a reconhecer.

O raciocínio da linha 11 é a parte substantiva, e é por isso que isto pertence ao documento, e não a um guia de implantação. A linha 11 proíbe qualquer host, conta ou fornecedor único cuja remoção possa parar a rede. Um substrato que exigisse serviço de entrada só funcionaria onde uma operadora o permitisse, fazendo de cada operadora um poder de veto — um ponto de estrangulamento por provedor, distribuído na aparência e centralizado de fato.

**Três notas sobre o mecanismo.** Primeiro, quanto ao transporte: conexões HTTPS e WebSocket comuns na porta 443 são o veículo certo, porque é isso que o caminho de rede permite de forma confiável e o que todo cliente web já emite. Este artigo deliberadamente não descreve esse tráfego como disfarçado. Não é camuflagem; é o protocolo padrão para a tarefa, e a honestidade importa porque o enquadramento da camuflagem convida à crença de que uma medida técnica respondeu a uma questão de permissão, o que a seção 5 mostra não ser o caso.

Segundo, quanto à versão seis do protocolo de internet: ela elimina a tradução em nível de operadora onde ambas as pontas a têm, e a adoção ultrapassou metade do tráfego do Google em todo o mundo em 28 de março de 2026, com os Estados Unidos perto de 57 por cento (Google, 2026). Vale a pena usá-la, e vale a pena não exigir nada dela. Endereçabilidade universal não é o mesmo que alcançabilidade universal — um endereço roteável globalmente continua por trás de um firewall que descarta pacotes de entrada não solicitados, e um nó que presuma o contrário falha na metade restante das conexões. A versão seis é uma otimização da postura de saída, nunca um substituto para ela.

Terceiro, quanto às redes de sobreposição cifradas. As sobreposições em malha são uma resposta real para caminhos de nó a nó que o coordenador não deve intermediar, e existem implementações conhecidas. Elas não podem entrar no módulo de protocolo. O princípio do código enxuto restringe o software de protocolo à biblioteca padrão de sua linguagem para que ele permaneça auditável por inteiro, e o protocolo de referência atualmente cumpre isso estritamente — seu módulo não declara dependência alguma, que é a propriedade que impede qualquer coordenador individual de se tornar um centro. Uma grande biblioteca de sobreposição dentro desse módulo acabaria com isso. Uma sobreposição pertence, portanto, abaixo do protocolo, como transporte em nível de implantação, escolhida por implantação e substituível, ou é implementada de forma mínima dentro da folha. A redação do documento é deliberadamente genérica pela mesma razão pela qual o documento não traz nomes de produtos.

Há uma tensão relacionada que o instituto não deve encobrir. A implantação do coordenador de referência fica atualmente por trás de uma única rede comercial de distribuição de conteúdo, e o projeto de transporte da pilha agrícola pressupõe o túnel desse fornecedor. Isso é conveniente, não está em conformidade com o espírito da linha 11, e é um ponto de estrangulamento exatamente do tipo que esta seção elimina na camada da operadora, ao mesmo tempo que o deixa intacto uma camada acima. Isso está fora do escopo aqui e pertence à lista de problemas em aberto do substrato.

## 3. Assimetria de largura de banda

**A restrição.** As conexões de consumo são assimétricas por projeto, muitas vezes na proporção de dez para um ou pior, e cada vez mais tarifadas por consumo. Um nó não pode servir como origem geral de conteúdo, e uma carga de trabalho que envia imagens grandes a cada host passará seu tempo em transferência, e não em computação.

**O que a técnica responde.** A maior parte, mantendo as cargas pequenas, e não movendo-as mais depressa. Três escolhas de projeto fazem o trabalho, e seus efeitos se somam.

**O tráfego de coordenação é pequeno por construção.** A linha 7 mantém narrativas e identidades fora do registro compartilhado — apenas hashes, tipos, marcas de tempo e referências. Um piso de privacidade adotado por razões de privacidade tem uma consequência de largura de banda: o tráfego da camada de registro é limitado pelo tamanho de hashes e cabeçalhos, e não pelo tamanho do que foi trocado. O conteúdo fica com as partes. As mensagens de coordenação que sustentam o mercado são um punhado de estruturas assinadas sobre uma codificação canônica de bytes. Nada aqui sobrecarrega um link de envio doméstico, e é nesse sentido que os pacotes são leves: as transmissões da própria arquitetura são leves porque uma linha que não pode ser cruzada as obriga a sê-lo.

**O trabalho é entregue como módulos em sandbox, não como imagens de máquina.** Esta é a única recomendação deste artigo que pede à implementação de referência que mude, em vez de manter seu formato. O agente de nó atual executa trabalhos por meio de um executor de contêineres, o que significa que o primeiro trabalho em um nó novo baixa camadas medidas em centenas de megabytes antes que qualquer trabalho comece. Um módulo WebAssembly para a mesma tarefa mede megabytes ou menos, inicia em milissegundos, traz um modelo de capacidades que nega por padrão, em vez de um modelo de exclusão voluntária, e é portável entre o hardware de consumo heterogêneo que o substrato espera, em vez de exigir uma arquitetura correspondente. Um runtime sem dependências nativas mantém o agente de nó auditável no mesmo espírito do módulo de protocolo. Os contêineres devem continuar disponíveis para cargas de trabalho que realmente precisem de um ambiente operacional completo, em nós cujas conexões e operadores possam suportá-los, e devem deixar de ser o padrão. A troca é real e deve ser declarada: o WebAssembly custa algum desempenho em relação à execução nativa e não pode hospedar software existente arbitrário sem modificação. Para trabalho irregular, leve, de sensores e coordenação — o padrão agrícola que esta arquitetura atende primeiro —, essa troca é favorável.

**Os trabalhos ficam em fila local.** Um nó mantém sua fila e seus relatórios pendentes em um armazenamento embutido local e os escoa quando a conexão permite. A consequência é que um link de envio ruim atrasa o trabalho em vez de perdê-lo, e uma conexão intermitente deixa de ser motivo de desqualificação. Isso importa para além da largura de banda: o piloto agrícola já prevê lacunas de conectividade rural com entrada offline e sincronização posterior, e a mesma propriedade faz de um nó nesse cenário um participante, e não um passivo.

Nenhuma dessas três é uma invenção nova, e nenhuma está registrada como invariante. São postura de projeto, registradas aqui para que uma implantação possa ser avaliada em relação a elas e para que o raciocínio sobreviva às pessoas que o tiveram. O conselho pode querer considerar se o padrão de módulo em vez de imagem deveria se tornar uma invariante registrada; este artigo ainda não o recomenda, porque a implementação de referência não o cumpre hoje, e um registro que se adianta ao código ensina a lição errada sobre o que significa registrar.

## 4. Execução em hardware que o host controla

**A restrição.** Um prossumidor que hospeda um nó tem a posse física da máquina. Pode ler sua memória, inspecionar seu disco e observar o que ela computa. A resposta convencional é a execução confidencial em hardware, e ela não está disponível nesta camada por uma questão de estratégia de produto dos fabricantes, e não de custo. A Intel descontinuou o Software Guard Extensions nos processadores de cliente a partir da décima primeira geração de sua linha Core e o mantém em peças para servidores e nuvem (Intel, 2021). O Secure Encrypted Virtualization da AMD, incluindo a geração com paginação aninhada, é um recurso dos servidores EPYC e não está presente nos Ryzen nem nos Threadripper (AMD, 2021). Exigir qualquer um deles excluiria essencialmente todo o hardware de consumo e readmitiria justamente o controle de acesso dos data centers que a camada de substrato existe para deslocar. Exigir enclaves não protegeria o substrato comum; o aboliria.

**O que a técnica responde, e até onde.** Não a confidencialidade diante de um host determinado. É nesta seção que o método do artigo muda, e dizê-lo com franqueza é mais útil do que uma solução alternativa apresentada com mais confiança do que merece.

A resposta disponível para a arquitetura não é confiar no host, mas tornar a desonestidade visível e cara, usando mecanismos que a pilha já deve a si mesma. Três partes:

**Execução redundante com divergência avaliada.** Um trabalho de importância é despachado para dois ou mais hosts independentes, e seus resultados são comparados. A concordância é evidência; a divergência é um evento que entra no pacto, em que a avaliação mais baixa da escala já significa que uma parte foi prejudicada, explorada ou atendida com intenção maliciosa. O ponto de aplicação existe: testemunhar é trabalho remunerado do substrato, e o substrato deve um tipo de trabalho em que as testemunhas são designadas aleatoriamente, de modo que nenhuma das partes de uma troca possa escolher sua testemunha. A execução redundante é esse mesmo padrão de mercado aplicado à computação, e não ao registro, e a designação aleatória é o que faz do conluio entre os executores de um trabalho uma questão de acaso, e não de escolha. O custo é um múltiplo da computação, pago deliberadamente para a classe de trabalho que o justifica, e compra detecção, não prevenção — a mesma postura que a camada de registro já adota diante de adulterações.

**A minimização de dados como controle principal.** Um host não pode extrair o que nunca chega. A linha 7 já mantém identidades e narrativas fora do registro compartilhado; a disciplina correspondente na camada de substrato é que um trabalho carregue o mínimo de dados que lhe permita ser concluído, que entradas sensíveis sejam particionadas entre hosts onde o trabalho o permitir, e que uma carga de trabalho que exija um grande conjunto coerente de dados sensíveis sobre pessoas identificáveis seja uma carga de trabalho para hardware cujo operador responda por ele. Essa última cláusula é um limite real para o alcance do substrato e deve ser declarada como tal, em vez de contornada por engenharia.

**A atestação como capacidade opcional, precificada e avaliada.** Onde um comprador realmente precisa de confidencialidade apoiada em hardware, a resposta é um mercado, não uma imposição. Um host com esse hardware anuncia a capacidade como parte de sua oferta, os compradores que precisam dela pagam por ela, e a alegação fica sujeita à mesma avaliação do pacto que qualquer outra declaração feita por um host. Isso mantém o piso aberto ao hardware de consumo, enquanto permite que o teto suba onde quer que um host tenha investido, e situa a decisão junto à parte que assume o risco.

**Situação.** Esta é a parte da revisão de setembro de 2026 que não está resolvida. A posição acima é argumentada, não adotada: nenhuma invariante está registrada, e um identificador candidato para a execução redundante consta no registro de questões em aberto como uma decisão a cargo do conselho conforme o §9.16. Registrá-lo obrigaria o substrato a construir um tipo de trabalho que ainda não construiu. A situação honesta é que a arquitetura tem uma resposta coerente para a observação pelo operador do host e ainda não se comprometeu com ela.

## 5. O que a técnica não responde

A sondagem de saída elimina completamente o problema do servidor de entrada. Ela não elimina o problema do uso aceitável, e este artigo enganaria seus leitores se insinuasse o contrário.

Leia novamente a política representativa. Ela proíbe equipamentos que sirvam qualquer pessoa fora da rede das instalações, "exceto para seu uso residencial pessoal e não comercial". A proibição de servidores de entrada é uma afirmação sobre portas e é respondida não se usando nenhuma. A vertente não comercial é uma afirmação sobre remuneração, e a remuneração é justamente o ponto: um prossumidor que hospeda substrato é pago, em moeda fiduciária na implementação atual e em crédito comunitário mais tarde. Nenhuma escolha de transporte, número de porta ou cifragem muda esse fato, e um projeto que alegue tê-lo contornado confundiu um mecanismo com uma permissão. A questão é se a participação remunerada em uma linha residencial aciona essa vertente, e a resposta é uma interpretação de termos contratuais em uma jurisdição, não uma propriedade do software.

O instituto deveria submeter a questão à análise da assessoria jurídica, e a ocasião natural está à mão: o piloto combinado de calor e computação já tem duas questões em aberto perante a assessoria jurídica sobre se um nó que gera receita em uma residência altera a posição do domicílio perante sua seguradora, em razão de exclusões por uso comercial. A questão dos termos das operadoras é a mesma questão dirigida a outro contrato, e deve entrar no mesmo pacote, em vez de esperar pelo seu próprio. Vale a pena nomear agora suas formas práticas — se é exigida uma conexão de nível empresarial, se um enquadramento de valor ínfimo (de minimis) ou de rateio de custos se sustenta, se a resposta varia tanto entre operadoras que as orientações para operadores de nós precisam ser regionais, e o que uma implantação comunica a possíveis hosts antes que se inscrevam.

A última delas é uma questão do pacto tanto quanto jurídica. Um prossumidor tem o direito de saber o que a participação pode significar para seu próprio contrato de serviço antes de aderir, e o próprio compromisso da arquitetura com uma relação avaliada e transparente entre operador e prossumidor faz do silêncio sobre esse ponto o padrão errado.

## 6. Aonde isto chegou

| Nível | O que mudou | Aplicação |
|---|---|---|
| Documento oficial | O nível de protocolo do substrato enuncia a postura de saída, sem exigência de entrada, e a vincula à linha 11 | A suíte verifica o texto; passa com 26 invariantes |
| Registro de conformidade | `SUB-no-inbound-requirement` adicionado, vinculado à implementação | Não vinculado até que testes de nó citem o identificador (§9.15) |
| Registro de questões em aberto | A entrada 9 registra a restrição, as resoluções, a parte em aberto e a questão jurídica | §9.3 |
| Este artigo | A postura sobre largura de banda e execução confidencial, argumentada e não vinculada | Nenhuma; analisa e não rege |

Duas obrigações processuais acompanham a alteração do documento e não são cumpridas por este artigo. Uma emenda do documento oficial e de seu registro tramita conforme os §§9.2 e 9.16 do estatuto, e durante o arranque (bootstrap) o conselho fundador exerce esse poder, com cada ato registrado no registro de governança como ato de arranque conforme o §16.1, aberto à associação como qualquer outra decisão. A suíte passa com o texto emendado, como o §9.2 exige antes da adoção, e as versões nos sete idiomas previstas na P2-002 foram atualizadas junto com o original em inglês.

## Fontes

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

AMD. (2021, 15 de março). *AMD EPYC 7003 series processors set new standard*. https://www.amd.com/en/newsroom/press-releases/2021-3-15-amd-epyc-7003-series-cpus-set-new-standard-as-hig.html

Comcast. (2021, 1º de fevereiro). *Acceptable use policy for Xfinity Internet (residential)*. https://www.xfinity.com/corporate/customers/policies/highspeedinternetaup

Google. (2026). *IPv6 adoption statistics*. https://www.google.com/intl/en/ipv6/statistics.html

Intel. (2021). *Intel SGX deprecation on client processors* [discussão na Intel Community]. https://community.intel.com/t5/Intel-Software-Guard-Extensions/Intel-SGX-deprecated-in-11th-Gen-processors/m-p/1351848

Internet Society. (2026, abril). *18 years later, IPv6 reaches majority*. https://pulse.internetsociety.org/en/blog/2026/04/18-years-later-ipv6-reaches-majority/

Network Theory Applied Research Institute. (2025a, outubro). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, junho). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

*Ohio Telecom Association v. FCC*, Nos. 24-7000 et al. (6th Cir. Jan. 2, 2025). Análise do Congressional Research Service: https://www.congress.gov/crs-product/LSB11264

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*Especificação: CC BY-SA 4.0*
