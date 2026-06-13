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
    }
}