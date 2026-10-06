> सामुदायिक अनुवाद (प्रारूप) — NTARI नीति P2-002, Global Multilingual Broadcast। स्रोत: README.md (अंग्रेज़ी मूल, स्नैपशॉट 2026-10-05)। P2-002 §3.1 के अनुसार क्षेत्रीय मेंटेनर की समीक्षा हेतु लंबित, मशीन-सहायता से तैयार सामुदायिक प्रारूप। मूल तकनीकी विनिर्देश §2.2 के अनुसार अंग्रेज़ी में ही रहते हैं।
>
> अनुवाद में कोई त्रुटि दिखे तो कृपया उसे स्वयं सुधारने में मदद करें:
> रिपॉज़िटरी को फ़ॉर्क (fork) करें और अपना सुधार पुल रिक्वेस्ट (pull request)
> के रूप में भेजें — https://github.com/NTARI-RAND/Janus। अनुवाद-सुधार हमारे
> लिए किसी भी अन्य योगदान जितने ही मूल्यवान हैं, और उनका सदा स्वागत है।

# द्विमुखी संरचना (Janus Facing Architecture)

द्विमुखी संरचना (JFA) का आधिकारिक दस्तावेज़, जिसका न्यास
Network Theory Applied Research Institute, Inc. (NTARI) के पास
[उसकी उपविधियों](https://github.com/NTARI-RAND/bylaws) की §1.4(a) के अंतर्गत है।

JFA समुदायों को प्रोज़्यूमरशिप की आर्थिक वास्तविकता से निपटने में समर्थ बनाती है
और बहिर्जात, चार्टल मुद्रा से अंतर्जात पारस्परिक ऋण की ओर एक मार्ग प्रस्तुत करती है।
यह पाँच कार्यात्मक स्तरों में संगठित है — आधार (Substrate), अभिलेख (Record),
प्रतिज्ञा (Covenant), अभिशासन (Governance), तथा अर्थव्यवस्था एवं सूचना — और
प्रत्येक स्तर तीन श्रेणियों में कार्यान्वित होता है: फ़्रंटएंड, ऑर्केस्ट्रेटर
और प्रोटोकॉल।

## दस्तावेज़

| | |
|---|---|
| **आधिकारिक दस्तावेज़** | [janus-facing-architecture.md](janus-facing-architecture.md) |
| **अनसुलझे प्रश्न** | [OPEN-QUESTIONS.md](OPEN-QUESTIONS.md) |
| **पूर्ववर्ती पाठों से आगे लाई गई संकल्पनाएँ** | [jfa-concept-triage-2026-08-24.md](jfa-concept-triage-2026-08-24.md) |
| **निष्पादन-योग्य अनुरूपता समुच्चय** | [jfa-conformance-suite.py](jfa-conformance-suite.py) |
| **वाहक बाधाओं के अधीन आधार (P1-004, सहचर पत्र)** | [P1-004_Substrate-Constraints_v0.1.md](P1-004_Substrate-Constraints_v0.1.md) |
| **पूर्ववर्ती पाठ** | [Historical Docs/](Historical%20Docs/) |

अंग्रेज़ी दस्तावेज़ ही प्रामाणिक है। अनुवाद पहुँच बढ़ाने के लिए उपलब्ध कराए गए हैं,
व्याख्या के लिए नहीं।

| भाषा | फ़ाइल |
|---|---|
| العربية (अरबी) | [janus-facing-architecture.ar.md](janus-facing-architecture.ar.md) |
| Español (स्पेनी) | [janus-facing-architecture.es.md](janus-facing-architecture.es.md) |
| Français (फ़्रांसीसी) | [janus-facing-architecture.fr.md](janus-facing-architecture.fr.md) |
| हिन्दी (हिन्दी) | [janus-facing-architecture.hi.md](janus-facing-architecture.hi.md) |
| Português (पुर्तगाली) | [janus-facing-architecture.pt.md](janus-facing-architecture.pt.md) |
| toki pona | [janus-facing-architecture.tok.md](janus-facing-architecture.tok.md) |
| 中文 (चीनी) | [janus-facing-architecture.zh.md](janus-facing-architecture.zh.md) |

## वे रेखाएँ जिन्हें पार नहीं किया जा सकता

आधिकारिक दस्तावेज़ का *वे रेखाएँ जिन्हें पार नहीं किया जा सकता* शीर्षक वाला खंड
उन बारह प्रावधानों को धारण करता है जिनका कोई भी अनुरूप कार्यान्वयन उल्लंघन नहीं
कर सकता। निर्माण से पहले इसे पढ़ें।

## कार्यान्वयन

संदर्भ कार्यान्वयन और उदाहरण अपने-अपने रिपॉज़िटरी में रहते हैं:

- [Tell](https://github.com/NTARI-RAND/Tell) — अभिलेख स्तर: प्रति-संचालक,
  साक्षी-प्रमाणित, केवल-संवर्धी अभिलेख
- [Agrinet](https://github.com/NTARI-RAND/Agrinet) — संघीय कृषि
  नेटवर्क प्रोटोकॉल
- [SoHoLINK](https://github.com/NTARI-RAND/SoHoLINK) ·
  [Cloudy](https://github.com/NTARI-RAND/Cloudy) ·
  [sohocloud-protocol](https://github.com/NTARI-RAND/sohocloud-protocol) —
  आधार स्तर
- [lighthouse](https://github.com/NTARI-RAND/lighthouse) ·
  [shelter](https://github.com/NTARI-RAND/shelter) ·
  [childcare-trust-network](https://github.com/NTARI-RAND/childcare-trust-network) ·
  [shanina](https://github.com/NTARI-RAND/shanina) ·
  [COER](https://github.com/NTARI-RAND/COER) ·
  [world-chase-tag](https://github.com/NTARI-RAND/world-chase-tag) — अर्थव्यवस्था एवं
  सूचना स्तर के बीज और उदाहरण

बीज मानक के अनुरूप होते हैं; आकार लचीला है, न्यूनतम सीमाएँ बाध्यकारी हैं।

## दस्तावेज़ का सत्यापन

समुच्चय भार वहन करने वाला पायदान है: यह गद्य को स्थिर आईडी वाले अपरिवर्तनीयों की
एक पंजी से आबद्ध करता है, ताकि जाँच के विफल हुए बिना दस्तावेज़ और पंजी एक-दूसरे से
अलग न हो सकें। केवल मानक लाइब्रेरी, कोई निर्भरता नहीं।

```
python jfa-conformance-suite.py                 # check the document
python jfa-conformance-suite.py --list          # print the invariant registry
python jfa-conformance-suite.py --doc PATH      # check another copy
python jfa-conformance-suite.py --project PATH  # check a repo's open-questions deliverable
```

जब प्रत्येक निष्पादित जाँच उत्तीर्ण हो तो निकास कोड 0, अन्यथा 1। आधिकारिक दस्तावेज़
में किसी भी संपादन के बाद इसे चलाएँ।

26 पंजीकृत अपरिवर्तनीयों में से 3 यहाँ दस्तावेज़ स्तर पर आबद्ध हैं और 23
**प्रत्यायोजित** हैं — वे चल रहे सॉफ़्टवेयर या किसी अभिशासन-लिखत को आबद्ध करते हैं,
और उन्हें केवल उस कोड या उस लिखत के साथ रहने वाले टेस्ट द्वारा ही प्रवर्तित किया जा
सकता है। वे पंजी में स्थिर आईडी के साथ रखे जाते हैं और तब तक प्रत्यायोजित तथा अनाबद्ध
के रूप में रिपोर्ट किए जाते हैं जब तक कोई रिपॉज़िटरी उन आईडी का उल्लेख करने वाले टेस्ट
जारी न करे। एक अनुरूप रिपॉज़िटरी उन आईडी का उल्लेख करती है; जब तक वह ऐसा नहीं करती,
उसकी अनुरूपता स्व-प्रमाणित है। किसी प्रत्यायोजित अपरिवर्तनीय को यहाँ से "जाँचा गया"
के रूप में रिपोर्ट करना टेस्ट रनर का वेश धारण किया हुआ स्व-प्रमाणन होगा, इसलिए
उस स्थानापन्न पर इसके बजाय लेबल लगाया गया है।

## अभी यहाँ प्रकाशित नहीं

विवाद-तंत्र अभिकल्पना — "विवाद-तंत्र अभिकल्पना" जैसा कि
[उपविधियाँ](https://github.com/NTARI-RAND/bylaws) §1.5 में इसे परिभाषित करती हैं — तथा
संरचना और रोबोटिक्स संबंधी लेख NTARI के दस्तावेज़ भंडार में रखे हैं और अभी इस
रिपॉज़िटरी में नहीं हैं।

## लाइसेंस

दो लाइसेंस, जैसा कि दस्तावेज़ का अपना पादलेख कहता है:

| क्या | लाइसेंस |
|---|---|
| विनिर्देश — आधिकारिक दस्तावेज़, उसके अनुवाद, और पूर्ववर्ती पाठ | [CC BY-SA 4.0](LICENSE-SPEC) |
| सॉफ़्टवेयर — अनुरूपता समुच्चय | [AGPL-3.0](LICENSE) |
