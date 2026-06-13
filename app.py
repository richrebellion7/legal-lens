"""
app.py — Streamlit UI for the Legal Document Risk Analyzer.
All API and processing logic lives in analyzer.py — this file is UI only.
"""

import os
import streamlit as st
from analyzer import analyze_document

from analyzer import (
    analyze_document,
    analyze_document_ollama
)
from translations import TRANSLATIONS

# ── Page config ───────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Legal Lens AI",
    page_icon="⚖️",
    layout="centered",
)

LANGUAGES = {
    "English": "en",
    "اردو": "ur",
    "తెలుగు": "te"
}

with st.sidebar:
    lang = st.selectbox(
        "Language",
        list(LANGUAGES.keys()),
        key="language_selector"
    )

lang_code = LANGUAGES[lang]

t = TRANSLATIONS[lang_code]


# ── Helpers ───────────────────────────────────────────────────────────────────

def risk_color(score: int) -> str:
    if score <= 25:
        return "🟢"
    elif score <= 50:
        return "🟡"
    elif score <= 75:
        return "🟠"
    else:
        return "🔴"


def risk_label(score: int) -> str:
    if score <= 25:
        return t["low_risk"]
    elif score <= 50:
        return t["moderate_risk"]
    elif score <= 75:
        return t["high_risk"]
    else:
        return t["critical_risk"]


def risk_delta_color(score: int) -> str:
    return "normal" if score <= 25 else "inverse"


def load_sample_pdf(filename: str) -> bytes | None:
    """Load a sample PDF from the sample_pdfs/ folder. Returns None if missing."""
    path = os.path.join("sample_pdfs", filename)
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    return None


# ── Sidebar — Sample PDFs ─────────────────────────────────────────────────────

with st.sidebar:
    st.header(t["sample_docs_header"])
    st.markdown(t["sample_docs_desc"])

    # Sample 1
    sample1_bytes = load_sample_pdf("sample_nda.pdf")
    if sample1_bytes:
        st.download_button(
           label=t["safe_agreement"],
            data=sample1_bytes,
            file_name="sample_nda.pdf",
            mime="application/pdf",
            use_container_width=True,
            help=t["safe_help"],
        )
    else:
        st.caption(t["sample_contract_missing"])

    # Sample 2
    sample2_bytes = load_sample_pdf("sample_contract.pdf")
    if sample2_bytes:
        st.download_button(
            label=t["unsafe_agreement"],
            data=sample2_bytes,
            file_name="sample_contract.pdf",
            mime="application/pdf",
            use_container_width=True,
           help=t["unsafe_help"],
        )
    else:
        st.caption(t["sample_nda_missing"])

    st.divider()
    st.markdown(t["how_it_works"])

# ── Header ────────────────────────────────────────────────────────────────────

st.title(t["title"])
st.caption(t["caption"])
st.divider()

inference_mode = st.radio(
    t["inference_mode"],
    [
        t["groq_cloud"],
        t["local_ollama"]
    ]
)
if inference_mode == t["groq_cloud"]:

    use_own_key = st.checkbox(
    t["byok_checkbox"]
)
    user_api_key = None

    if use_own_key:
      user_api_key = st.text_input(
    t["groq_api_key"],
    type="password",
    help=t["groq_api_help"]
)
else:
    user_api_key = None

if inference_mode == t["local_ollama"]:
    ollama_model =st.selectbox(
    t["local_model"],
        [
            "llama3.2",
            "gemma3",
            "mistral",
            "qwen3"
        ]
    )
if inference_mode == t["groq_cloud"]:
    current_model = "☁️llama-3.3-70b-versatile (Cloud)"
else:
    current_model = f"{ollama_model} (Local)"

st.markdown(
    f"""

    **{t["current_model"]}** `🖥️{current_model}`
    """
)
if inference_mode == t["groq_cloud"]:
    st.success(t["cloud_active"])
else:
    st.success(t["local_active"])

# ── Upload ────────────────────────────────────────────────────────────────────

uploaded_file = st.file_uploader(
    t["upload_label"],
    type=["pdf"],
    help=t["upload_help"],
)
if uploaded_file:
    st.info(f"📄 **{uploaded_file.name}** — {uploaded_file.size / 1024:.1f} KB uploaded")

analyze_btn = st.button(
    t["analyze_button"],
    type="primary",
    disabled=not uploaded_file,
    use_container_width=True,
)

if not uploaded_file:
   st.info(t["upload_info"])


# ── Analysis & Results ────────────────────────────────────────────────────────

if analyze_btn and uploaded_file:
    with st.spinner(t["spinner"]):
        try:
            file_bytes = uploaded_file.read()
            if inference_mode == t["groq_cloud"]:
                result = analyze_document(
                file_bytes=file_bytes,
                api_key=user_api_key
                )
            else:
                result = analyze_document_ollama(
                    file_bytes=file_bytes,
                    model=ollama_model
                )

        except RuntimeError as e:
            st.error(f"**{t['configuration_error']}:** {e}")
            st.stop()
        except ValueError as e:
            st.error(f"**{t['document_error']}:** {e}")
            st.stop()
        except Exception as e:
            st.error(f"**{t['api_error']}:** {e}")
            st.stop()

    # ── Metrics row ──────────────────────────────────────────────────────────
    st.divider()
    st.subheader(t["results_header"])

    score     = result["risk_score"]
    red_flags = result["red_flags"]
    summary   = result["summary"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label=t["overall_risk_score"],
            value=f"{score} / 100",
            delta=risk_label(score),
            delta_color=risk_delta_color(score),
        )

    with col2:
        st.metric(
           label=t["severity"],
            value=f"{risk_color(score)} {risk_label(score)}",
        )

    with col3:
        st.metric(
            label=t["red_flags_found"],
            value=len(red_flags),
            delta=t["issues_identified"],
            delta_color="off",
        )

    # ── Progress bar ─────────────────────────────────────────────────────────
    st.progress(score / 100)

    # ── Summary ──────────────────────────────────────────────────────────────
    st.subheader(t["summary_header"])
    st.info(summary)

    # ── Red flags ────────────────────────────────────────────────────────────
    st.subheader(
    f"{t['red_flags_header']} ({len(red_flags)} found)"
)

    if not red_flags:
        st.success(t["no_red_flags"])
    else:
        for i, flag in enumerate(red_flags, start=1):
            st.warning(f"**{i}.** {flag}")

    # ── Raw JSON expander ────────────────────────────────────────────────────
    with st.expander(t["raw_json"]):
        st.json(result)

    st.divider()
    st.caption(t["legal_disclaimer"])
    st.info(
    t["upload_success"].format(
        name=uploaded_file.name,
        size=uploaded_file.size / 1024
    )
)