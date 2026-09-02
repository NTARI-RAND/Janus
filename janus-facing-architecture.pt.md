> Tradução comunitária (rascunho) — Política P2-002 da NTARI, Difusão Multilíngue Global. Fonte: janus-facing-architecture.md (original em inglês, instantâneo de 2026-08-31). Rascunho comunitário assistido por máquina, pendente de revisão pelo mantenedor regional conforme P2-002 §3.1. As especificações técnicas centrais permanecem em inglês conforme o §2.2.
>
> Encontrou um erro nesta tradução? Sua correção é uma contribuição bem-vinda e
> valorizada: faça um fork do repositório do projeto da NTARI e abra um pull
> request, ou escreva para info@ntari.org.

# JFA: Arquitetura de Dupla Face (Janus Facing Architecture)

## Introdução

A Arquitetura de Dupla Face — assim chamada em referência ao deus romano que olha em duas direções ao mesmo tempo, tal como todo participante econômico enfrenta exigências tanto de produção quanto de consumo — permite que as comunidades enfrentem a realidade econômica do prossumo. Cada membro de uma economia não é apenas consumidor, mas prossumidor (Toffler, 1980), produzindo simultaneamente algo de valor mesmo que tudo o que tenha a oferecer seja seu tempo. Oferece também a opção de transformar o modelo de emissão: de moeda chartal exógena (emitida por uma autoridade externa à comunidade) para crédito mútuo endógeno (emitido pelos membros entre si conforme transacionam).

A segunda face do nome é política. Acemoglu e Robinson (2019) mostram que a liberdade só sobrevive dentro de um corredor estreito, no qual um Estado capaz — o Leviatã — é igualado por uma sociedade igualmente capaz de contê-lo. Fora do corredor, o Leviatã assume suas outras formas: ausente, e a coordenação fracassa; despótico, e quem coordena domina os coordenados; de papel, e os freios existem por escrito, mas não na prática. Permanecer dentro do corredor exige o que eles chamam de efeito da Rainha Vermelha: Estado e sociedade correndo juntos, cada um ampliando sua capacidade porque o outro o faz. Toda plataforma econômica é um Leviatã em miniatura — coordena, faz cumprir e registra — e as plataformas dominantes de hoje são despóticas por construção: evoluem na velocidade da rede enquanto as instituições que deveriam contê-las se movem na velocidade das reuniões.

A pesquisa da NTARI localiza esse fracasso na própria infraestrutura. Sistemas deliberativos são cultura material: a arquitetura de uma plataforma materializa uma teoria sobre quem pode saber e quem pode decidir, e as arquiteturas de difusão predominantes tratam os participantes como destinatários passivos (NTARI, 2025b). A lacuna de velocidade resultante é estrutural: a informação se move na velocidade das redes, enquanto a síntese democrática permanece presa a ciclos eleitorais sincronizados por um relógio postal (NTARI, 2025a). A JFA foi construída para fechar essa lacuna por dentro: a comunidade que coordena é a comunidade que fiscaliza, as duas capacidades trocadas continuamente no mesmo software e na mesma velocidade, disciplinadas camada por camada pelo custo de sair. É um Leviatã acorrentado em código.

A Arquitetura de Dupla Face (JFA) organiza-se em cinco camadas funcionais — Substrato, Registro, Pacto, Governança, e Economia e Informação (E&I) — cada uma implementada em três níveis: o frontend, para a colaboração entre prossumidores; o orquestrador, um backend que fornece coordenação sobreposta entre comunidades geográficas; e o protocolo subjacente, o padrão para o tratamento seguro de dados entre os níveis.

O software da JFA é projetado para ser publicado e gerido em ambiente copyleft, geralmente a Licença Pública Geral Affero da GNU, permitindo que novos frontends, federações, protocolos e arquiteturas evoluam no mercado global, formando um comum de software livre.

Este é o documento oficial, sob a curadoria do Network Theory Applied Research Institute, Inc. Os instrumentos anteriores estão preservados em [Historical Docs](Historical%20Docs/); os conceitos herdados deles constam na [triagem de conceitos](jfa-concept-triage-2026-08-24.md); o que permanece sem solução é nomeado em [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md).

## Princípios

**Responsabilidade compartilhada.** A comunidade que coordena a economia é a mesma comunidade que fiscaliza essa coordenação. As duas funções são trocadas continuamente — nunca divididas entre governantes e governados.

**Disciplina institucional.** Cada camada é disciplinada pelo custo de abandoná-la: onde sair é barato, a concorrência disciplina; onde sair é caro, os membros votam; onde sair é impossível, as decisões permanecem abertas a contestação.

**Código enxuto e auditável.** O software de protocolo permanece pequeno, não depende de nada além da biblioteca padrão de sua linguagem, e é auditável por inteiro.

## Camada de Substrato

É o hardware onde tudo acontece, de propriedade de prossumidores de CPUs, GPUs, impressoras, armazenamento e sensores.

### Nível de protocolo

Troca instruções e ordens através de um mercado distribuído de computação e armazenamento, operado em computadores de consumo hospedados em residências, escritórios e depósitos, bem como em equipamentos industriais reaproveitados.

### Nível de orquestrador

Capacidade de computação federada de prossumidores, criando mais opções ao longo da geografia.

### Nível de frontend

Interface de E&I para prossumir computação e armazenamento.

## Camada de Registro

Uma função remunerada do substrato, que registra e serve o diálogo entre as camadas de E&I e de Pacto para o público.

O registro do que aconteceu é mantido de seis maneiras. Cada parte de uma transação mantém o seu próprio registro; o operador mantém o seu; duas testemunhas mantêm os seus; e os hashes são comprometidos em uma única cadeia pública, distribuída pelo substrato — o registro para todos aqueles que não foram transatores, testemunhas nem operador. A cadeia é somente de adição: o dano é perdoado por anotação, nunca por apagamento. Uma plataforma deve ter pelo menos duas testemunhas independentes; com menos, uma implantação deve rotular-se como não federada.

### Nível de protocolo

Captura, categoriza e aplica hash a cada transmissão dentro da pilha, a fim de estabelecer reputação por meio da camada de Pacto e de fundar a base de um meio de troca por meio de E&I.

### Nível de orquestrador

Federa registros ao longo da geografia, habilitando reputação e troca compartilhadas. O que a federação compartilha é verdade registrada — reputação e histórico de trocas — nunca uma unidade monetária.

### Nível de frontend

Serviço remunerado de computação e registro fornecido por prossumidores na camada de substrato de E&I.

## Camada de Pacto

Um contrato social aplicado em código, que informa expectativas flexíveis para as interações entre prossumidores.

### Nível de protocolo

Uma avaliação simples, escrita em código executável, para que os prossumidores avaliem suas interações entre si ao longo da pilha.

### Nível de orquestrador

Uma API que serve avaliações conformes através dos mercados de E&I da pilha, a partir de prossumidores do substrato. Quando ocorrem aparentes violações do pacto, os operadores de plataforma julgam entre seus prossumidores; disputas que atravessam plataformas são julgadas na camada de testemunhas. Quem julga é avaliado por sua conduta por ambos os prossumidores ou operadores envolvidos.

### Nível de frontend

A interface de E&I onde a API é servida.

## Camada de Governança

É aqui, e é assim, que seres humanos se reúnem para agir colaborativamente sobre a pilha.

### Nível de protocolo

Organização sem fins lucrativos de curadoria de software copyleft.

### Nível de orquestrador

A associação ao Network Theory Applied Research Institute, obtida operando uma instância federada de software JFA.

### Nível de frontend

A coordenação síncrona e assíncrona dos membros, regida pelo estatuto da organização.

## Camada de Economia e Informação

A camada de E&I é hospedada no substrato, sindicalizada com a camada de Registro, e facilita a conformidade com o pacto.

### Nível de protocolo

Cada plataforma econômica ou de informação tem um protocolo projetado para a troca que nela ocorre (por exemplo, agricultura, um jogo ou citações de pesquisa).

### Nível de orquestrador

E&I deve operar sobre hardware revogável, obtido e registrado pela camada de substrato.

### Nível de frontend

Os designs de frontend das plataformas de E&I devem ser personalizáveis pelo usuário.

## As linhas que não podem ser cruzadas

Uma implementação que cruze qualquer uma destas não é uma JFA menor; é um software diferente vestindo o nome.

1. O dinheiro é criado no momento da troca — um saldo desce, outro sobe, somando sempre zero.
2. O crédito é conquistado, nunca comprado, e nunca resgatável por moeda fiduciária.
3. A moeda de cada comunidade é soberana — sem unidade compartilhada, sem conversão entre comunidades.
4. O valor fica em casa; apenas a verdade atravessa.
5. A troca entre comunidades são dois gastos soberanos ligados atomicamente pela cadeia pública — sem câmara de compensação, sem taxa de câmbio.
6. O registro é somente de adição — o dano é perdoado por anotação, nunca por apagamento.
7. Sem narrativas nem identidades no registro compartilhado — apenas hashes, tipos, marcas de tempo e referências.
8. A reputação nunca é um número único — o que os outros veem é a contagem de trocas em cada nível de avaliação.
9. A reputação decide se um membro negocia com base em confiança; um limite comum a toda a comunidade, fixado pelo operador e nunca derivado da reputação, decide quanto.
10. Uma implantação começa em custódia (escrow) — colateralizada, sem saldos negativos, sem crédito estendido entre contrapartes — e passa a um sistema de crédito mútuo híbrido ou pleno somente depois que o operador desenvolver capacidade, a rede de prossumidores for notificada, e as autorizações locais para prestar serviços de crédito mútuo forem publicadas na camada de governança — ou, quando a jurisdição não exigir nenhuma, for publicada ali, em seu lugar, uma constatação nesse sentido.
11. Nenhum host, conta ou fornecedor único cuja remoção possa parar a rede.
12. As posições e o histórico de um membro sobrevivem a qualquer frontend; os registros de uma comunidade sobrevivem a qualquer operador.

## Referências

Acemoglu, D., & Robinson, J. A. (2019). *The Narrow Corridor: States, Societies, and the Fate of Liberty*. Penguin Press.

Network Theory Applied Research Institute. (2025a, outubro). *Addressing democratic information velocity* (P1-002). https://www.ntari.org/post/ntari-whitepaper-addressing-democratic-information-velocity

Network Theory Applied Research Institute. (2025b, junho). *The material culture of democratic deliberation*. https://www.ntari.org/post/the-material-culture-of-democratic-deliberation

Toffler, A. (1980). *The Third Wave*. William Morrow.

---

*Network Theory Applied Research Institute, Inc. — 501(c)(3) — EIN 92-3047136 — info@ntari.org*
