> ترجمة مجتمعية (مسوّدة) — سياسة NTARI رقم P2-002، البثّ العالمي المتعدد اللغات. المصدر: README.md (الأصل الإنجليزي، لقطة بتاريخ 2026-10-05). مسوّدة مجتمعية بمساعدة آلية، في انتظار مراجعة مشرف الصيانة الإقليمي وفق P2-002 §3.1. تبقى المواصفات التقنية الأساسية بالإنجليزية وفق §2.2.
>
> تصحيحات الترجمة مساهمات نرحّب بها ونقدّرها كسائر المساهمات، فإذا لاحظت خطأً
> في هذه الترجمة فيمكنك إصلاحه بنفسك عبر إنشاء fork للمستودع وفتح pull
> request: https://github.com/NTARI-RAND/Janus

# العمارة ذات الوجهين (Janus Facing Architecture)

الوثيقة الرسمية للعمارة ذات الوجهين (JFA)، ويتولّى رعايتها
Network Theory Applied Research Institute, Inc. (NTARI) بموجب
[لوائحه الداخلية](https://github.com/NTARI-RAND/bylaws) §1.4(a).

تتيح JFA للمجتمعات معالجة الواقع الاقتصادي للإنتاج-الاستهلاك المشترك، وتوفّر
مساراً من النقد الإلزامي خارجي المنشأ إلى الائتمان المتبادل داخلي المنشأ. وهي
تنتظم في خمس طبقات وظيفية — الركيزة (Substrate)، والسجل (Record)، والعهد
(Covenant)، والحَكامة (Governance)، والاقتصاد والمعلومات (Economy & Information)
— وكلٌّ منها منجَزة في ثلاث مراتب: الواجهة الأمامية، والمنسّق، والبروتوكول.

## الوثيقة

| | |
|---|---|
| **الوثيقة الرسمية** | [janus-facing-architecture.md](janus-facing-architecture.md) |
| **المسائل التي لم تُحسم بعد** | [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) |
| **المفاهيم المنقولة من الوثائق السابقة** | [jfa-concept-triage-2026-08-24.md](jfa-concept-triage-2026-08-24.md) |
| **مجموعة اختبارات المطابقة القابلة للتنفيذ** | [jfa-conformance-suite.py](jfa-conformance-suite.py) |
| **الركيزة في ظل قيود مزوّدي الاتصال (P1-004، ورقة مصاحبة)** | [P1-004_Substrate-Constraints_v0.1.md](P1-004_Substrate-Constraints_v0.1.md) |
| **الوثائق السابقة** | [Historical Docs/](Historical%20Docs/) |

الوثيقة الإنجليزية هي المرجع المعتمد. وتُقدَّم الترجمات لتوسيع نطاق الوصول، لا
لأغراض التفسير.

| اللغة | الملف |
|---|---|
| العربية (Arabic) | [janus-facing-architecture.ar.md](janus-facing-architecture.ar.md) |
| Español (Spanish) | [janus-facing-architecture.es.md](janus-facing-architecture.es.md) |
| Français (French) | [janus-facing-architecture.fr.md](janus-facing-architecture.fr.md) |
| हिन्दी (Hindi) | [janus-facing-architecture.hi.md](janus-facing-architecture.hi.md) |
| Português (Portuguese) | [janus-facing-architecture.pt.md](janus-facing-architecture.pt.md) |
| toki pona | [janus-facing-architecture.tok.md](janus-facing-architecture.tok.md) |
| 中文 (Chinese) | [janus-facing-architecture.zh.md](janus-facing-architecture.zh.md) |

## الخطوط التي لا يجوز تجاوزها

يتضمّن قسم الوثيقة الرسمية المعنون *الخطوط التي لا يجوز تجاوزها* الأحكامَ الاثني
عشر التي لا يجوز لأي تنفيذ مطابق أن ينتهكها. اقرأه قبل البدء في البناء.

## التنفيذات

تقيم التنفيذات المرجعية والنُّسخ العاملة في مستودعاتها الخاصة:

- [Tell](https://github.com/NTARI-RAND/Tell) — طبقة السجل: سجل لكل مُشغِّل،
  مُشهَد عليه، لا يقبل إلا الإضافة
- [Agrinet](https://github.com/NTARI-RAND/Agrinet) — بروتوكول شبكة زراعية
  متّحدة
- [SoHoLINK](https://github.com/NTARI-RAND/SoHoLINK) ·
  [Cloudy](https://github.com/NTARI-RAND/Cloudy) ·
  [sohocloud-protocol](https://github.com/NTARI-RAND/sohocloud-protocol) —
  طبقة الركيزة
- [lighthouse](https://github.com/NTARI-RAND/lighthouse) ·
  [shelter](https://github.com/NTARI-RAND/shelter) ·
  [childcare-trust-network](https://github.com/NTARI-RAND/childcare-trust-network) ·
  [shanina](https://github.com/NTARI-RAND/shanina) ·
  [COER](https://github.com/NTARI-RAND/COER) ·
  [world-chase-tag](https://github.com/NTARI-RAND/world-chase-tag) — بذور ونُسخ
  عاملة لطبقة الاقتصاد والمعلومات

تلتزم البذور بالمعيار؛ فالشكل يلين، والحدود الدنيا مُلزِمة.

## التحقق من الوثيقة

مجموعة الاختبارات هي الدرجة الحاملة للثقل: فهي تربط النص بسجلٍّ من الثوابت
(invariants) ذات معرّفات مستقرة، بحيث لا يمكن أن تتباعد الوثيقة والسجل دون أن
يفشل الفحص. تعتمد على المكتبة القياسية وحدها، بلا أي اعتماديات.

```
python jfa-conformance-suite.py                 # check the document
python jfa-conformance-suite.py --list          # print the invariant registry
python jfa-conformance-suite.py --doc PATH      # check another copy
python jfa-conformance-suite.py --project PATH  # check a repo's open-questions deliverable
```

رمز الخروج 0 عندما ينجح كل فحص مُنفَّذ، و1 خلاف ذلك. شغّلها بعد أي تعديل على
الوثيقة الرسمية.

من بين الثوابت المسجّلة البالغ عددها 26، يُربَط 3 منها هنا على مستوى الوثيقة،
و23 منها **مُفوَّضة** — فهي تُلزِم برمجيات قيد التشغيل أو أداةً من أدوات
الحَكامة، ولا يمكن إنفاذها إلا عبر اختبارات تقيم بجوار تلك الشيفرة أو تلك
الأداة. وهي محمولة في السجل بمعرّفات مستقرة، ويُبلَّغ عنها بوصفها مُفوَّضة وغير
مربوطة إلى أن يُصدر مستودعٌ ما اختبارات تستشهد بتلك المعرّفات. والمستودع
المطابق يستشهد بالمعرّفات؛ وإلى أن يفعل، تبقى مطابقته إقراراً ذاتياً. ولو أُبلغ
من هنا عن ثابت مُفوَّض بأنه "مفحوص" لكان ذلك إقراراً ذاتياً يتنكّر في هيئة مُشغِّل
اختبارات، ولذلك يُوسَم البديل المؤقت بما هو عليه بدلاً من ذلك.

## ما لم يُنشر هنا بعد

تصميم آليات النزاع — "تصميم آليات النزاع" كما تعرّفه
[اللوائح الداخلية](https://github.com/NTARI-RAND/bylaws) §1.5 — ومقالات الهيكل
والروبوتات محفوظة في مستودع وثائق NTARI، وليست في هذا المستودع بعد.

## الترخيص

ترخيصان، كما ينصّ تذييل الوثيقة نفسها:

| ما يشمله | الترخيص |
|---|---|
| المواصفة — الوثيقة الرسمية وترجماتها والوثائق السابقة | [CC BY-SA 4.0](LICENSE-SPEC) |
| البرمجية — مجموعة اختبارات المطابقة | [AGPL-3.0](LICENSE) |
