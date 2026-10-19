> Tradução comunitária (rascunho) — Política P2-002 da NTARI, Difusão Multilíngue Global. Fonte: janus-facing-architecture.md (original em inglês, instantâneo de 2026-10-08). Rascunho comunitário assistido por máquina, pendente de revisão pelo mantenedor regional conforme P2-002 §3.1. As especificações técnicas centrais permanecem em inglês conforme o §2.2.
>
> Encontrou um erro nesta tradução? Sua correção é uma contribuição bem-vinda e
> valorizada: faça um fork do repositório do projeto da NTARI e abra um pull
> request, ou escreva para info@ntari.org.

# JFA: Arquitetura de Dupla Face (Janus Facing Architecture)

## Introdução

Cada membro de uma economia é um **prossumidor** — não apenas consumidor, mas ao mesmo tempo produtor de algo de valor, mesmo que tudo o que tenha a oferecer seja seu tempo (Toffler, 1980). Ninguém está de um lado só de uma troca; as duas faces são a mesma pessoa.

A Arquitetura de Dupla Face (Janus Facing Architecture) recebe o nome do deus romano que olha em duas direções ao mesmo tempo, porque é isso que todo prossumidor faz: cada um enfrenta exigências tanto de produção quanto de consumo, ao mesmo tempo. Ela permite que as comunidades enfrentem a realidade econômica do prossumo, e oferece a opção de transformar o modelo de emissão: de moeda chartal exógena — emitida por uma autoridade externa à comunidade (Knapp, 1924) — para crédito mútuo endógeno, emitido pelos membros entre si conforme transacionam (Moore, 1988; Greco, 2009).

A segunda face do nome é política. Acemoglu e Robinson (2019) mostram que a liberdade só sobrevive dentro de um corredor estreito, no qual um Estado capaz — o Leviatã — é igualado por uma sociedade igualmente capaz de contê-lo. Fora do corredor, o Leviatã assume suas outras formas: ausente, e a coordenação fracassa; despótico, e quem coordena domina os coordenados; de papel, e os freios existem por escrito, mas não na prática. Permanecer dentro do corredor exige o que eles chamam de efeito da Rainha Vermelha: Estado e sociedade correndo juntos, cada um ampliando sua capacidade porque o outro o faz. Toda plataforma econômica é um Leviatã em miniatura — coordena, faz cumprir e registra — e as plataformas dominantes de hoje são despóticas por construção: evoluem na velocidade da rede enquanto as instituições que deveriam contê-las se movem na velocidade das reuniões.

A pesquisa da NTARI localiza esse fracasso na própria infraestrutura. Sistemas deliberativos são cultura material: a arquitetura de uma plataforma materializa uma teoria sobre quem pode saber e quem pode decidir, e as arquiteturas de difusão predominantes tratam os participantes como destinatários passivos (NTARI, 2025b). A lacuna de velocidade resultante é estrutural: a informação se move na velocidade das redes, enquanto a síntese democrática permanece presa a ciclos eleitorais sincronizados por um relógio postal (NTARI, 2025a). A JFA foi construída para fechar essa lacuna por dentro, disciplinada camada por camada pelo custo de sair. É um Leviatã acorrentado em código.

A Arquitetura de Dupla Face (JFA) organiza-se em cinco camadas funcionais — Substrato, Registro, Pacto, Governança, e Economia e Informação (E&I) — cada uma implementada em três níveis: o frontend, para a colaboração entre prossumidores; o orquestrador, um backend que fornece coordenação sobreposta entre comunidades geográficas; e o protocolo subjacente, o padrão para o tratamento seguro de dados entre os níveis.

O software da JFA é projetado para ser publicado e gerido em ambiente copyleft, geralmente a Licença Pública Geral Affero da GNU, versão 3 ou posterior (AGPL-3.0-or-later), permitindo que novos frontends, federações, protocolos e arquiteturas evoluam no mercado global, formando um comum de software livre.

Este é o documento oficial, sob a curadoria do Network Theory Applied Research Institute, Inc. Os instrumentos anteriores estão preservados em [Historical Docs](Historical%20Docs/); os conceitos herdados deles constam na [triagem de conceitos](jfa-concept-triage-2026-08-24.md); o que permanece sem solução é nomeado em [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## Por que isso importa

Todo sistema que coordena pessoas exerce poder sobre elas, pretenda ou não. Isso não é um defeito; a coordenação o exige. Mas o poder só permanece saudável quando algo o contém — não um freio de papel, mas pessoas reais com interesse real, perto o bastante para agir. A maioria das plataformas hoje se move na velocidade da rede enquanto tudo o que foi construído para cobrá-las se move na velocidade das reuniões, e um freio que chega tarde não é freio algum. A resposta da JFA é parar de tratar coordenação e prestação de contas como dois sistemas: o mesmo software, as mesmas pessoas, a mesma velocidade.

## Princípios

**Responsabilidade compartilhada.** A comunidade que coordena a economia é a mesma comunidade que fiscaliza essa coordenação. As duas funções são trocadas continuamente — nunca divididas entre governantes e governados.

**Disciplina institucional.** Cada camada é disciplinada pelo custo de abandoná-la — o que um membro perde ao sair, e o que uma comunidade perde ao expulsar alguém. Onde sair é barato, a concorrência disciplina: as camadas de Substrato e de Economia e Informação. Onde sair é caro, os membros votam: as camadas de Pacto e de Governança. Onde sair é catastrófico, as decisões permanecem abertas a contestação: a camada de Registro. Cada camada nomeia abaixo o seu próprio custo, porque é esse custo que decide como uma disputa ali se resolve.

**Código enxuto e auditável.** O software de protocolo permanece pequeno, não depende de nada além da biblioteca padrão de sua linguagem, e é auditável por inteiro.

## Camada de Substrato

É o hardware onde tudo acontece, de propriedade de prossumidores de CPUs, GPUs, impressoras, armazenamento e sensores.

Sair daqui é barato, e a recusa de um transportador não custa a um prossumidor nada além de uma conexão. Um orquestrador que se recusa a transportar a sua capacidade não levou o seu hardware, os seus saldos nem o seu histórico, e outro orquestrador está a uma oferta publicada de distância. As querelas nesta camada, portanto, não são julgadas: um transporte que fica sem atestação dentro de sua janela de compromisso simplesmente é revertido, ninguém decide sobre ele, e um transportador que recusa ou falha com liberdade demais é desbancado por oferta melhor em vez de receber apelações.

### Nível de protocolo

Troca instruções e ordens através de um mercado distribuído de computação e armazenamento, operado em computadores de consumo hospedados em residências, escritórios e depósitos, bem como em equipamentos industriais reaproveitados.

Os nós ingressam nesse mercado por meio de sobreposições cifradas (overlays) e sondagem de saída (polling), sem exigir portas de entrada abertas nem endereço estático; basta a conexão tal como um provedor residencial a entrega. A linha 11 depende disso: um substrato que só funcionasse onde um provedor permite serviço de entrada carregaria um ponto de estrangulamento em cada provedor.

O trabalho do substrato tem integridade assegurada, não confidencialidade assegurada: um host pode ler o que o seu nó computa. O trabalho cujo resultado liquida um gasto ou entra no registro é executado em pelo menos dois hosts independentes, e o desacordo entre eles é avaliado, nunca tomado por confiável.

### Nível de orquestrador

Capacidade de computação federada de prossumidores, criando mais opções ao longo da geografia. Os orquestradores publicam ofertas de transporte no mercado do substrato, cada uma nomeando uma tarifa, um compromisso de entrega e uma chave pública; qualquer plataforma pode selecionar qualquer orquestrador alcançável, de modo que um transportador dominante é desbancado em vez de regulado. Transporte é entrega, não execução: um orquestrador leva gastos assinados até o conjunto de testemunhas e devolve atestações, nunca se confia nele para determinar se uma troca ocorreu, e pode ter perdas e basear-se em novas tentativas.

### Nível de frontend

Interface de Economia e Informação para prossumir computação e armazenamento.

## Camada de Registro

Uma função remunerada do substrato, que registra e serve o diálogo entre as camadas de Economia e Informação e de Pacto para o público.

O registro do que aconteceu é mantido por seis partes: os dois prossumidores da troca, o operador, o orquestrador e duas testemunhas mantêm, cada um, um registro próprio. Os hashes são, além disso, comprometidos em uma única cadeia pública, distribuída pelo substrato — o registro para todos aqueles que não mantêm nenhum registro próprio. Os compromissos de cada troca transportada por um orquestrador são copiados para a cadeia e armazenados em substrato financiado pela organização de curadoria da camada de Governança, de modo que o registro que liga as comunidades umas às outras não é pago por nenhuma delas. A cadeia é somente de adição: o dano é perdoado por anotação, nunca por apagamento. Uma plataforma deve ter pelo menos duas testemunhas independentes; com menos, uma implantação deve rotular-se como não federada. As testemunhas são designadas por um sorteio semeado a partir da cadeia pública, que qualquer um pode verificar, e são pagas pelo mercado do substrato, nunca pelo operador que observam.

Ninguém pode ser apagado do registro, e abandoná-lo é catastrófico. O que foi comprometido nunca é apagado, mas nenhuma cópia única é o registro, e cada cópia dura apenas enquanto é mantida: a do orquestrador, com o último transporte pago; as das testemunhas, enquanto seu armazenamento estiver pago; as próprias dos prossumidores e do operador, até que deixem de mantê-las; e a da cadeia, enquanto seu armazenamento estiver financiado. O registro sobrevive nas cópias que restarem; a cadeia é armazenada pelo substrato, e não pelo operador, de modo que pode sobreviver ao operador, ao frontend e à querela, e o que ela carrega além de cada guardião é o fato do compromisso, não o conteúdo. Como nada pode ser apagado do registro, nenhuma constatação aqui é jamais definitiva: uma entrada contestada é respondida por anotação, e a anotação é tão permanente quanto a entrada a que responde.

Uma troca entre comunidades continua sendo dois gastos soberanos. A citação que a liquida carrega também a tarifa de transporte do orquestrador, posta em custódia (escrow) com a troca na iniciação e liberada por essa mesma citação. A liberação é conjunta e de tudo ou nada — se a entrega não for atestada dentro da janela de compromisso da oferta, todos os gastos são revertidos — e a atestação do próprio orquestrador não conta para o limiar que libera a sua própria tarifa. A tarifa é dividida entre os livros-razão de origem dos dois prossumidores cuja troca foi transportada, cada um pagando sua parte em sua própria unidade; nada cruza uma fronteira comunitária. O crédito que ela rende é mantido pelas mesmas seis partes, citado por chave. A entrega é atestada somente pelas testemunhas; o operador mantém o seu registro de um transporte e nunca o atesta.

### Nível de protocolo

Captura, categoriza e aplica hash a cada transmissão dentro da pilha, a fim de estabelecer reputação por meio da camada de Pacto e de fundar a base de um meio de troca por meio de Economia e Informação.

### Nível de orquestrador

Federa registros ao longo da geografia, habilitando reputação e troca compartilhadas. O que a federação compartilha é verdade registrada — reputação e histórico de trocas — nunca uma unidade monetária.

### Nível de frontend

A compra e venda de armazenamento de registro através do substrato, remunerando os prossumidores que mantêm o registro.

## Camada de Pacto

Um contrato social aplicado em código, que informa expectativas flexíveis para as interações entre prossumidores.

Sair daqui é caro. Um prossumidor banido de uma plataforma mantém o registro de cada avaliação que conquistou ali — seis partes o guardam — mas a posição que ele carrega não o segue por padrão: na plataforma seguinte, a contagem de trocas em cada nível de avaliação é reconstruída uma troca testemunhada de cada vez. Esse preço é a razão pela qual um banimento repousa em evidência julgada, e não na palavra de um operador. Quando ocorrem aparentes violações do pacto, os operadores de plataforma julgam entre seus prossumidores; disputas que atravessam plataformas, e disputas entre um prossumidor e o operador de sua própria plataforma, são julgadas na camada de testemunhas — nenhum operador julga uma disputa da qual é parte. Onde quer que o julgamento ocorra, as partes dele avaliam quem julga — o operador entre seus próprios prossumidores, as testemunhas nos demais casos — de modo que os árbitros estão dentro do sistema de reputação que fazem cumprir.

Como sair é caro, aqui os membros votam: a federação do Pacto vota as mudanças conceituais e programáticas do pacto (a Escala de Avaliação de Trocas Baseada em Leveson, Leveson-Based Trade Assessment Scale, LBTAS), de sua API e de sua orquestração, e encomenda estudos formais dos efeitos do pacto escolhido sobre seus usuários.

### Nível de protocolo

Uma avaliação simples, escrita em código executável, para que os prossumidores avaliem suas interações entre si ao longo da pilha.

### Nível de orquestrador

Uma API que serve avaliações conformes através dos mercados de Economia e Informação da pilha, a partir de prossumidores do substrato.

### Nível de frontend

A interface de Economia e Informação onde a API é servida.

## Camada de Governança

É aqui, e é assim, que seres humanos se reúnem para agir colaborativamente sobre a pilha.

Sair daqui é caro, e esta é a única camada em que a expulsão alcança o próprio software: um membro expulso do Instituto perde, por um prazo delimitado, o voto que dá forma ao que todos os demais executam. Por isso a expulsão nunca é decisão de um operador — ela é remetida à federação de Governança e decidida pelo voto de seus membros conforme o estatuto, com constância em registro.

### Nível de protocolo

Organização sem fins lucrativos de curadoria de software copyleft.

### Nível de orquestrador

A associação ao Network Theory Applied Research Institute, obtida operando uma instância federada de software JFA ou participando como prossumidor em uma plataforma federada.

### Nível de frontend

A coordenação síncrona e assíncrona dos membros, regida pelo estatuto da organização.

## Camada de Economia e Informação

A camada de Economia e Informação é hospedada no substrato, sindicalizada com a camada de Registro, e facilita a conformidade com o pacto.

Sair daqui é barato por construção. Um operador pode banir um prossumidor de sua plataforma, mas não daquilo que ele construiu ali: as posições e o histórico sobrevivem a qualquer frontend, de modo que os banidos saem com seu registro intacto e seus saldos ainda devidos. Um banimento é uma perda de mercado, não uma perda de posição — e um operador cujos termos ou limite de crédito expulsam prossumidores perde o comércio em vez de vencer a discussão.

### Nível de protocolo

Cada plataforma econômica ou de informação tem um protocolo projetado para a troca que nela ocorre (por exemplo, agricultura, um jogo ou citações de pesquisa). Cada um assume que qualquer host do substrato pode ler o que ele computa.

### Nível de orquestrador

A Economia e Informação deve operar sobre hardware revogável, obtido e registrado pela camada de substrato. Uma plataforma não precisa de orquestrador próprio: seleciona um no mercado do substrato e paga o transporte com recursos da própria troca.

### Nível de frontend

Os designs de frontend das plataformas de Economia e Informação devem ser personalizáveis pelo usuário.

## As linhas que não podem ser cruzadas

Uma implementação que cruze qualquer uma destas não é uma JFA menor; é um software diferente vestindo o nome.

1. Todo crédito é uma nota promissória (IOU), criada no momento em que dois membros trocam — um saldo desce, outro sobe, somando sempre zero. Essa é a única maneira pela qual o dinheiro passa a existir: nada é cunhado, nada é emitido de fora, e nada se acumula como juros.
2. O crédito é conquistado, nunca comprado, e nunca resgatável por moeda fiduciária.
3. A moeda de cada comunidade é soberana — sem unidade compartilhada, sem conversão entre comunidades.
4. O valor fica em casa; apenas a verdade atravessa.
5. A troca entre comunidades são dois gastos soberanos ligados atomicamente pela cadeia pública — sem câmara de compensação, sem taxa de câmbio.
6. O registro é somente de adição — o dano é perdoado por anotação, nunca por apagamento.
7. Sem narrativas nem identidades no registro compartilhado — apenas hashes, tipos, marcas de tempo e referências.
8. A reputação nunca é um número único — o que os outros veem é a contagem de trocas em cada nível de avaliação.
9. A reputação decide se um membro negocia com base em confiança; um limite comum a toda a comunidade, fixado pelo operador e nunca derivado da reputação, decide quanto.
10. Uma implantação começa em custódia (escrow) — colateralizada, sem saldos negativos, sem crédito estendido entre contrapartes — e passa a um sistema de crédito mútuo híbrido ou pleno somente depois que o operador desenvolver capacidade, a rede de prossumidores for notificada, e as autorizações locais para prestar serviços de crédito mútuo forem publicadas na camada de governança — ou, quando a jurisdição não exigir nenhuma, for publicada ali, em seu lugar, uma constatação nesse sentido — e uma passagem ao crédito mútuo pleno for ratificada pelos prossumidores da implantação.
11. Nenhum host, conta ou fornecedor único cuja remoção possa parar a rede.
12. As posições e o histórico de um membro sobrevivem a qualquer frontend; os registros de uma comunidade sobrevivem a qualquer operador.

## Referências

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

Greco, T. H. (2009). *The End of Money and the Future of Civilization*. Chelsea Green Publishing.

Knapp, G. F. (1924). *The State Theory of Money*. Macmillan. (Obra original publicada em 1905)

Moore, B. J. (1988). *Horizontalists and Verticalists: The Macroeconomics of Credit Money*. Cambridge University Press.

Network Theory Applied Research Institute. (2025a, outubro). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, junho). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

Toffler, A. (1980). *The Third Wave*. William Morrow.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*

*Software: AGPL-3.0-or-later · Especificação: CC BY-SA 4.0*
