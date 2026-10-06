> Tradução comunitária (rascunho) — política P2-002 da NTARI, Transmissão Multilíngue Global. Fonte: README.md (original em inglês, snapshot de 2026-10-05). Rascunho comunitário assistido por máquina, pendente de revisão do mantenedor regional conforme P2-002 §3.1. As especificações técnicas centrais permanecem em inglês conforme §2.2.
>
> Notou algum erro nesta tradução? Correções de tradução são contribuições
> valiosas e muito bem-vindas: faça um fork do repositório e abra um pull
> request em https://github.com/NTARI-RAND/Janus.

# Arquitetura de Dupla Face (Janus Facing Architecture)

O documento oficial da Arquitetura de Dupla Face (JFA), sob a curadoria do
Network Theory Applied Research Institute, Inc. (NTARI) nos termos do §1.4(a) do
[seu estatuto](https://github.com/NTARI-RAND/bylaws).

A JFA permite que as comunidades enfrentem a realidade econômica do prossumo e
oferece um caminho da moeda chartal exógena para o crédito mútuo endógeno. Ela
se organiza em cinco camadas funcionais — Substrato, Registro, Pacto, Governança,
e Economia e Informação — cada uma implementada em três níveis: frontend,
orquestrador e protocolo.

## O documento

| | |
|---|---|
| **Documento oficial** | [janus-facing-architecture.md](janus-facing-architecture.md) |
| **Questões sem solução** | [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) |
| **Conceitos herdados de instrumentos anteriores** | [jfa-concept-triage-2026-08-24.md](jfa-concept-triage-2026-08-24.md) |
| **Suíte de conformidade executável** | [jfa-conformance-suite.py](jfa-conformance-suite.py) |
| **Substrato sob restrições das operadoras (P1-004, artigo complementar)** | [P1-004_Substrate-Constraints_v0.1.md](P1-004_Substrate-Constraints_v0.1.md) |
| **Instrumentos anteriores** | [Historical Docs/](Historical%20Docs/) |

O documento em inglês é o que faz fé. As traduções são oferecidas para ampliar o
alcance, não para fins de interpretação.

| Idioma | Arquivo |
|---|---|
| العربية (árabe) | [janus-facing-architecture.ar.md](janus-facing-architecture.ar.md) |
| Español (espanhol) | [janus-facing-architecture.es.md](janus-facing-architecture.es.md) |
| Français (francês) | [janus-facing-architecture.fr.md](janus-facing-architecture.fr.md) |
| हिन्दी (híndi) | [janus-facing-architecture.hi.md](janus-facing-architecture.hi.md) |
| Português (português) | [janus-facing-architecture.pt.md](janus-facing-architecture.pt.md) |
| toki pona | [janus-facing-architecture.tok.md](janus-facing-architecture.tok.md) |
| 中文 (chinês) | [janus-facing-architecture.zh.md](janus-facing-architecture.zh.md) |

## As linhas que não podem ser cruzadas

A seção do documento oficial intitulada *As linhas que não podem ser cruzadas*
contém as doze disposições que nenhuma implementação conforme pode violar.
Leia-a antes de construir.

## Implementações

As implementações de referência e as instâncias ficam em seus próprios
repositórios:

- [Tell](https://github.com/NTARI-RAND/Tell) — a camada de Registro: registro
  por operador, testemunhado e somente de adição
- [Agrinet](https://github.com/NTARI-RAND/Agrinet) — protocolo de rede agrícola
  federada
- [SoHoLINK](https://github.com/NTARI-RAND/SoHoLINK) ·
  [Cloudy](https://github.com/NTARI-RAND/Cloudy) ·
  [sohocloud-protocol](https://github.com/NTARI-RAND/sohocloud-protocol) —
  camada de Substrato
- [lighthouse](https://github.com/NTARI-RAND/lighthouse) ·
  [shelter](https://github.com/NTARI-RAND/shelter) ·
  [childcare-trust-network](https://github.com/NTARI-RAND/childcare-trust-network) ·
  [shanina](https://github.com/NTARI-RAND/shanina) ·
  [COER](https://github.com/NTARI-RAND/COER) ·
  [world-chase-tag](https://github.com/NTARI-RAND/world-chase-tag) — sementes e
  instâncias da camada de Economia e Informação

As sementes são conformes ao padrão; a forma se adapta, os pisos obrigam.

## Verificação do documento

A suíte é o degrau que sustenta o peso: ela vincula o texto a um registro de
invariantes com IDs estáveis, de modo que o documento e o registro não podem se
distanciar sem que a verificação falhe. Apenas a biblioteca padrão, sem
dependências.

```
python jfa-conformance-suite.py                 # check the document
python jfa-conformance-suite.py --list          # print the invariant registry
python jfa-conformance-suite.py --doc PATH      # check another copy
python jfa-conformance-suite.py --project PATH  # check a repo's open-questions deliverable
```

Código de saída 0 quando todas as verificações executadas passam, 1 caso
contrário. Execute-a após qualquer edição do documento oficial.

Dos 26 invariantes registrados, 3 estão vinculados aqui, na camada do documento,
e 23 são **delegados** — eles vinculam software em execução ou um instrumento de
governança, e só podem ser aplicados por testes que fiquem junto a esse código
ou a esse instrumento. Eles constam do registro com IDs estáveis e são
reportados como delegados e não vinculados até que um repositório publique
testes que citem esses IDs. Um repositório conforme cita os IDs; enquanto não o
fizer, sua conformidade é autodeclarada. Reportar daqui um invariante delegado
como "verificado" seria autodeclaração disfarçada de executor de testes; por
isso, o substituto é rotulado como tal.

## Ainda não publicado aqui

O projeto da mecânica de disputas — "o projeto da mecânica de disputas", tal
como [o estatuto](https://github.com/NTARI-RAND/bylaws) o define no §1.5 — e os
artigos sobre estrutura e robótica estão guardados no acervo de documentos
da NTARI e ainda não estão neste repositório.

## Licença

Duas licenças, conforme declara o próprio rodapé do documento:

| O quê | Licença |
|---|---|
| A especificação — o documento oficial, suas traduções e os instrumentos anteriores | [CC BY-SA 4.0](LICENSE-SPEC) |
| O software — a suíte de conformidade | [AGPL-3.0](LICENSE) |
