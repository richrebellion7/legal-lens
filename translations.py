TRANSLATIONS = {
    "en": {
        # Page
        "page_title": "Legal Doc Risk Analyzer",

        # Sidebar
        "sample_docs_header": "📂 Sample Documents",
        "sample_docs_desc": (
            "Don't have a legal PDF handy? "
            "Download one of these examples to test the analyzer:"
        ),
        "safe_agreement": "⬇️ Safe Agreement",
        "unsafe_agreement": "⬇️ Unsafe Agreement",
        "safe_help": "A Non-Disclosure Agreement with several notable clauses",
        "unsafe_help": "A software services contract with various risk clauses",
        "sample_nda_missing": "_sample_nda.pdf not found in sample_pdfs/_",
        "sample_contract_missing": "_sample_contract.pdf not found in sample_pdfs/_",

        "how_it_works": """
**How it works**
1. Download a sample above (or use your own PDF)
2. Upload it using the file uploader
3. Click **Analyze** and wait a few seconds
4. Review the risk score, red flags, and summary

**Model:** `llama-3.3-70b-versatile`

**Supported files:** PDF only (text-based)
""",

        # Header
        "title": "⚖️ Legal Document Risk Analyzer",
        "caption": (
            "Upload a contract, NDA, terms of service, or any legal PDF "
            "to identify potential risks and red flags instantly."
        ),

        # Inference
        "inference_mode": "Inference Mode",
        "groq_cloud": "Groq Cloud",
        "local_ollama": "Local Ollama",
        "local_model": "Local Model",

        # Upload
        "upload_label": "Upload your legal document (PDF)",
        "upload_help": (
            "Max recommended size: ~50 pages. "
            "Scanned/image PDFs may not work."
        ),
        "analyze_button": "🔍 Analyze Document",
        "upload_info": (
            "Upload a PDF document above to get started, "
            "or download a sample from the sidebar."
        ),

        # Spinner
        "spinner": "Reading document and consulting AI legal analyst…",

        # Errors
        "configuration_error": "Configuration Error",
        "document_error": "Document Error",
        "api_error": "API Error",

        # Results
        "results_header": "📊 Risk Assessment Results",
        "overall_risk_score": "Overall Risk Score",
        "severity": "Severity",
        "red_flags_found": "Red Flags Found",
        "issues_identified": "issues identified",

        "summary_header": "📝 Document Summary",

        "red_flags_header": "🚩 Red Flags",
        "no_red_flags": (
            "No significant red flags were identified in this document."
        ),

        "raw_json": "🔧 Raw JSON Response",

        "legal_disclaimer": (
            "⚠️ This tool is for informational purposes only and does not "
            "constitute legal advice. Consult a qualified attorney "
            "for legal guidance."
        ),

        # Risk Labels
        "low_risk": "Low Risk",
        "moderate_risk": "Moderate Risk",
        "high_risk": "High Risk",
        "critical_risk": "Critical Risk",
        "byok_checkbox": "Use my own Groq API key (BYOK)",
        "groq_api_key": "Groq API Key",
        "groq_api_help": "Your key is used only for this session.",

        "current_model": "Current Model:",
        "cloud_active": "☁️ Cloud AI Active",
        "local_active": "🖥️ Local AI Active",
        "upload_success": "📄 **{name}** — {size:.1f} KB uploaded",
    },
    "te": {
      # Page
        "page_title": "లీగల్ డాక్ రిస్క్ అనలైజర్",

     # Sidebar
     "sample_docs_header": "📂 నమూనా పత్రాలు",
     "sample_docs_desc": (
         "మీ వద్ద చట్టపరమైన PDF లేకపోతే, "
        "అనలైజర్‌ను పరీక్షించడానికి ఈ ఉదాహరణలను డౌన్‌లోడ్ చేయండి:"
    ),
    "safe_agreement": "⬇️ సురక్షిత ఒప్పందం",
    "unsafe_agreement": "⬇️ ప్రమాదకర ఒప్పందం",
    "safe_help": "కొన్ని ముఖ్యమైన నిబంధనలు కలిగిన గోప్యతా ఒప్పందం (NDA)",
    "unsafe_help": "వివిధ ప్రమాదకర నిబంధనలు కలిగిన సాఫ్ట్‌వేర్ సేవల ఒప్పందం",
    "sample_nda_missing": "_sample_nda.pdf ఫైల్ sample_pdfs లో కనుగొనబడలేదు_",
    "sample_contract_missing": "_sample_contract.pdf ఫైల్ sample_pdfs లో కనుగొనబడలేదు_",

    "how_it_works": """
**ఇది ఎలా పనిచేస్తుంది**
1. పై ఉన్న నమూనాను డౌన్‌లోడ్ చేయండి (లేదా మీ స్వంత PDF ఉపయోగించండి)
2. ఫైల్ అప్‌లోడర్ ద్వారా PDF ను అప్‌లోడ్ చేయండి
3. **విశ్లేషించు** బటన్‌ను నొక్కి కొన్ని సెకన్లు వేచి ఉండండి
4. ప్రమాద స్కోర్, హెచ్చరికలు మరియు సారాంశాన్ని పరిశీలించండి

**మోడల్:** `llama-3.3-70b-versatile`

**మద్దతు ఉన్న ఫైళ్లు:** PDF మాత్రమే (టెక్స్ట్ ఆధారిత)
""",

    # Header
    "title": "⚖️ లీగల్ డాక్యుమెంట్ రిస్క్ అనలైజర్",
    "caption": (
        "ఒప్పందం, NDA, సేవా నిబంధనలు లేదా ఏదైనా చట్టపరమైన PDF ను "
        "అప్‌లోడ్ చేసి సంభావ్య ప్రమాదాలు మరియు హెచ్చరికలను వెంటనే గుర్తించండి."
    ),

    # Inference
    "inference_mode": "ఇన్‌ఫరెన్స్ విధానం",
    "groq_cloud": "గ్రోక్ క్లౌడ్",
    "local_ollama": "లోకల్ ఒల్లామా",
    "local_model": "లోకల్ మోడల్",

    # Upload
    "upload_label": "మీ చట్టపరమైన పత్రం (PDF) ను అప్‌లోడ్ చేయండి",
    "upload_help": (
        "సిఫార్సు చేసిన గరిష్ట పరిమాణం: సుమారు 50 పేజీలు. "
        "స్కాన్ చేసిన లేదా చిత్ర ఆధారిత PDFలు పని చేయకపోవచ్చు."
    ),
    "analyze_button": "🔍 పత్రాన్ని విశ్లేషించు",
    "upload_info": (
        "ప్రారంభించడానికి పై PDF పత్రాన్ని అప్‌లోడ్ చేయండి "
        "లేదా సైడ్‌బార్ నుండి ఒక నమూనాను డౌన్‌లోడ్ చేయండి."
    ),
    "upload_success": "📄 **{name}** — {size:.1f} KB అప్‌లోడ్ చేయబడింది",

    # Spinner
    "spinner": "పత్రాన్ని చదువుతూ AI చట్ట విశ్లేషకుడిని సంప్రదిస్తోంది…",

    # Errors
    "configuration_error": "కాన్ఫిగరేషన్ లోపం",
    "document_error": "పత్రం లోపం",
    "api_error": "API లోపం",

    # Results
    "results_header": "📊 ప్రమాద అంచనా ఫలితాలు",
    "overall_risk_score": "మొత్తం ప్రమాద స్కోర్",
    "severity": "తీవ్రత",
    "red_flags_found": "కనుగొనబడిన హెచ్చరికలు",
    "issues_identified": "సమస్యలు గుర్తించబడ్డాయి",

    "summary_header": "📝 పత్రం సారాంశం",

    "red_flags_header": "🚩 హెచ్చరికలు",
    "no_red_flags": (
        "ఈ పత్రంలో ముఖ్యమైన హెచ్చరికలు ఏవీ గుర్తించబడలేదు."
    ),

    "raw_json": "🔧 అసలు JSON ప్రతిస్పందన",

    "legal_disclaimer": (
        "⚠️ ఈ సాధనం సమాచారం కోసం మాత్రమే. "
        "ఇది చట్టపరమైన సలహాగా పరిగణించబడదు. "
        "చట్టపరమైన మార్గదర్శకత్వం కోసం అర్హత కలిగిన న్యాయవాదిని సంప్రదించండి."
    ),

    # Risk Labels
    "low_risk": "తక్కువ ప్రమాదం",
    "moderate_risk": "మధ్యస్థ ప్రమాదం",
    "high_risk": "అధిక ప్రమాదం",
    "critical_risk": "తీవ్ర ప్రమాదం",

    # BYOK
    "byok_checkbox": "నా స్వంత Groq API కీని ఉపయోగించు (BYOK)",
    "groq_api_key": "Groq API కీ",
    "groq_api_help": "మీ కీ ఈ సెషన్‌లో మాత్రమే ఉపయోగించబడుతుంది.",

    # Model Status
    "current_model": "ప్రస్తుత మోడల్:",
    "cloud_active": "☁️ క్లౌడ్ AI సక్రియంగా ఉంది",
    "local_active": "🖥️ లోకల్ AI సక్రియంగా ఉంది",
    },
"ur": {
    # Page
    "page_title": "قانونی دستاویز خطرہ تجزیہ کار",

    # Sidebar
    "sample_docs_header": "📂 نمونہ دستاویزات",
    "sample_docs_desc": (
        "اگر آپ کے پاس کوئی قانونی PDF موجود نہیں ہے، "
        "تو تجزیہ کار کو آزمانے کے لیے ان مثالوں کو ڈاؤن لوڈ کریں:"
    ),
    "safe_agreement": "⬇️ محفوظ معاہدہ",
    "unsafe_agreement": "⬇️ خطرناک معاہدہ",
    "safe_help": "چند اہم شقوں کے ساتھ ایک عدم انکشاف معاہدہ (NDA)",
    "unsafe_help": "مختلف خطرناک شقوں کے ساتھ سافٹ ویئر سروسز کا معاہدہ",
    "sample_nda_missing": "_sample_nda.pdf فائل sample_pdfs میں نہیں ملی_",
    "sample_contract_missing": "_sample_contract.pdf فائل sample_pdfs میں نہیں ملی_",

    "how_it_works": """
**یہ کیسے کام کرتا ہے**
1. اوپر موجود نمونہ ڈاؤن لوڈ کریں (یا اپنی PDF استعمال کریں)
2. فائل اپ لوڈر کے ذریعے PDF اپ لوڈ کریں
3. **تجزیہ کریں** بٹن پر کلک کریں اور چند سیکنڈ انتظار کریں
4. خطرے کا اسکور، انتباہات اور خلاصہ کا جائزہ لیں

**ماڈل:** `llama-3.3-70b-versatile`

**معاون فائلیں:** صرف PDF (متنی بنیاد پر)
""",

    # Header
    "title": "⚖️ قانونی دستاویز خطرہ تجزیہ کار",
    "caption": (
        "معاہدہ، NDA، شرائطِ خدمت یا کسی بھی قانونی PDF کو "
        "اپ لوڈ کریں تاکہ ممکنہ خطرات اور انتباہات فوراً شناخت کیے جا سکیں۔"
    ),

    # Inference
    "inference_mode": "استدلال کا طریقہ",
    "groq_cloud": "گروک کلاؤڈ",
    "local_ollama": "لوکل اولاما",
    "local_model": "لوکل ماڈل",

    # Upload
    "upload_label": "اپنی قانونی دستاویز (PDF) اپ لوڈ کریں",
    "upload_help": (
        "تجویز کردہ زیادہ سے زیادہ حجم: تقریباً 50 صفحات۔ "
        "اسکین شدہ یا تصویری PDF کام نہ کر سکیں۔"
    ),
    "analyze_button": "🔍 دستاویز کا تجزیہ کریں",
    "upload_info": (
        "شروع کرنے کے لیے اوپر PDF اپ لوڈ کریں "
        "یا سائیڈ بار سے نمونہ ڈاؤن لوڈ کریں۔"
    ),
    "upload_success": "📄 **{name}** — {size:.1f} KB اپ لوڈ ہو گئی",

    # Spinner
    "spinner": "دستاویز پڑھی جا رہی ہے اور AI قانونی تجزیہ کار سے مشورہ لیا جا رہا ہے…",

    # Errors
    "configuration_error": "ترتیب کی خرابی",
    "document_error": "دستاویز کی خرابی",
    "api_error": "API کی خرابی",

    # Results
    "results_header": "📊 خطرے کی تشخیص کے نتائج",
    "overall_risk_score": "مجموعی خطرہ اسکور",
    "severity": "شدت",
    "red_flags_found": "پائے گئے انتباہات",
    "issues_identified": "مسائل کی نشاندہی ہوئی",

    "summary_header": "📝 دستاویز کا خلاصہ",

    "red_flags_header": "🚩 انتباہات",
    "no_red_flags": (
        "اس دستاویز میں کوئی اہم انتباہات شناخت نہیں ہوئیں۔"
    ),

    "raw_json": "🔧 اصل JSON جواب",

    "legal_disclaimer": (
        "⚠️ یہ ٹول صرف معلوماتی مقاصد کے لیے ہے۔ "
        "یہ قانونی مشورہ نہیں ہے۔ "
        "قانونی رہنمائی کے لیے کسی مستند وکیل سے مشورہ کریں۔"
    ),

    # Risk Labels
    "low_risk": "کم خطرہ",
    "moderate_risk": "درمیانہ خطرہ",
    "high_risk": "زیادہ خطرہ",
    "critical_risk": "انتہائی خطرہ",

    # BYOK
    "byok_checkbox": "میری اپنی Groq API کلید استعمال کریں (BYOK)",
    "groq_api_key": "Groq API کلید",
    "groq_api_help": "آپ کی کلید صرف اس سیشن کے لیے استعمال ہوگی۔",

    # Model Status
    "current_model": "موجودہ ماڈل:",
    "cloud_active": "☁️ کلاؤڈ AI فعال ہے",
    "local_active": "🖥️ لوکل AI فعال ہے",
}



    
}