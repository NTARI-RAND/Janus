> 社区翻译（草稿）—— NTARI 政策 P2-002《全球多语言广播》。来源：README.md（英文原版，2026-10-05 快照）。本文件为机器辅助的社区草稿，依据 P2-002 §3.1 尚待区域维护者审校。根据 §2.2，核心技术规范仍以英文为准。
>
> 如发现译文有误，欢迎 fork 仓库并提交 Pull Request
> 来改进翻译：https://github.com/NTARI-RAND/Janus。翻译修正与代码贡献同样宝贵，我们诚挚欢迎。

# 双面架构（Janus Facing Architecture）

双面架构（JFA）的正式文件，由 Network Theory Applied Research Institute, Inc.（NTARI）
依据[其章程](https://github.com/NTARI-RAND/bylaws) §1.4(a) 托管。

JFA 使社区得以应对产消一体（prosumership）的经济现实，并提供一条从外生的法定货币
通往内生的互助信用的路径。它由五个功能层组成——基质层（Substrate）、记录层（Record）、
约定层（Covenant）、治理层（Governance），以及经济与信息层（Economy & Information）——
每一层以三个层级实现：前端、编排器与协议。

## 文件

| | |
|---|---|
| **正式文件** | [janus-facing-architecture.md](janus-facing-architecture.md) |
| **待决问题** | [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) |
| **自先前文本承继的概念** | [jfa-concept-triage-2026-08-24.md](jfa-concept-triage-2026-08-24.md) |
| **可执行的符合性测试套件** | [jfa-conformance-suite.py](jfa-conformance-suite.py) |
| **运营商约束下的基质（P1-004，配套论文）** | [P1-004_Substrate-Constraints_v0.1.md](P1-004_Substrate-Constraints_v0.1.md) |
| **先前文本** | [Historical Docs/](Historical%20Docs/) |

英文文件具有权威性。提供译本是为了扩大覆盖面，而非用于解释。

| 语言 | 文件 |
|---|---|
| العربية（阿拉伯语） | [janus-facing-architecture.ar.md](janus-facing-architecture.ar.md) |
| Español（西班牙语） | [janus-facing-architecture.es.md](janus-facing-architecture.es.md) |
| Français（法语） | [janus-facing-architecture.fr.md](janus-facing-architecture.fr.md) |
| हिन्दी（印地语） | [janus-facing-architecture.hi.md](janus-facing-architecture.hi.md) |
| Português（葡萄牙语） | [janus-facing-architecture.pt.md](janus-facing-architecture.pt.md) |
| toki pona（道本语） | [janus-facing-architecture.tok.md](janus-facing-architecture.tok.md) |
| 中文（Chinese） | [janus-facing-architecture.zh.md](janus-facing-architecture.zh.md) |

## 不可逾越的界线

正式文件中题为*不可逾越的界线*的一节，载有任何符合规范的实现都不得违反的十二项条款。
动手构建之前，请先阅读该节。

## 实现

参考实现与实例位于各自的仓库中：

- [Tell](https://github.com/NTARI-RAND/Tell) —— 记录层：按运营者划分、有见证、
  仅追加的记录
- [Agrinet](https://github.com/NTARI-RAND/Agrinet) —— 联邦化农业网络协议
- [SoHoLINK](https://github.com/NTARI-RAND/SoHoLINK) ·
  [Cloudy](https://github.com/NTARI-RAND/Cloudy) ·
  [sohocloud-protocol](https://github.com/NTARI-RAND/sohocloud-protocol) ——
  基质层
- [lighthouse](https://github.com/NTARI-RAND/lighthouse) ·
  [shelter](https://github.com/NTARI-RAND/shelter) ·
  [childcare-trust-network](https://github.com/NTARI-RAND/childcare-trust-network) ·
  [shanina](https://github.com/NTARI-RAND/shanina) ·
  [COER](https://github.com/NTARI-RAND/COER) ·
  [world-chase-tag](https://github.com/NTARI-RAND/world-chase-tag) —— 经济与
  信息层的种子与实例

种子符合标准；形态可以变通，底线具有约束力。

## 验证文件

测试套件是承重的一级：它把文本与一份具有稳定标识符的不变量登记册绑定在一起，
因此文件与登记册一旦彼此偏离，检查就会失败。仅使用标准库，没有任何依赖。

```
python jfa-conformance-suite.py                 # check the document
python jfa-conformance-suite.py --list          # print the invariant registry
python jfa-conformance-suite.py --doc PATH      # check another copy
python jfa-conformance-suite.py --project PATH  # check a repo's open-questions deliverable
```

所有已执行的检查都通过时，退出码为 0，否则为 1。每次编辑正式文件后，都请运行它。

在已登记的 26 项不变量中，有 3 项在此于文件层加以约束，另有 23 项属于**委托**型——
它们约束的是运行中的软件或某项治理文书，只能由与该代码或该文书并存的测试来执行。
它们以稳定标识符载入登记册，并在某个仓库随附引用这些标识符的测试之前，被报告为委托且未约束。
符合规范的仓库会引用这些标识符；在此之前，其符合性仅为自我证明。若从此处把一项委托型
不变量报告为“已检查”，那就是披着测试运行器外衣的自我证明，因此改为对这一替代项加以标注。

## 尚未在此发布

争议机制设计——即[章程](https://github.com/NTARI-RAND/bylaws) §1.5 所定义的“争议机制设计”——
以及结构与机器人相关文章，目前保存在 NTARI 的文件库中，尚未纳入本仓库。

## 许可证

如文件本身的页脚所述，采用两种许可证：

| 内容 | 许可证 |
|---|---|
| 规范——正式文件、其译本以及先前文本 | [CC BY-SA 4.0](LICENSE-SPEC) |
| 软件——符合性测试套件 | [AGPL-3.0](LICENSE) |
