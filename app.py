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


# ── Page config ───────────────────────────────────────────────────────────────

st.set_page_config(
    page_title="Legal Doc Risk Analyzer",
    page_icon="⚖️",
    layout="centered",
)


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
        return "Low Risk"
    elif score <= 50:
        return "Moderate Risk"
    elif score <= 75:
        return "High Risk"
    else:
        return "Critical Risk"


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
    st.header("📂 Sample Documents")
    st.markdown(
        "Don't have a legal PDF handy? "
        "Download one of these examples to test the analyzer:"
    )

    # Sample 1
    sample1_bytes = load_sample_pdf("sample_nda.pdf")
    if sample1_bytes:
        st.download_button(
            label="⬇️ Safe Agreement",
            data=sample1_bytes,
            file_name="sample_nda.pdf",
            mime="application/pdf",
            use_container_width=True,
            help="A Non-Disclosure Agreement with several notable clauses",
        )
    else:
        st.caption("_sample_nda.pdf not found in sample_pdfs/_")

    # Sample 2
    sample2_bytes = load_sample_pdf("sample_contract.pdf")
    if sample2_bytes:
        st.download_button(
            label="⬇️ Unsafe Agreement",
            data=sample2_bytes,
            file_name="sample_contract.pdf",
            mime="application/pdf",
            use_container_width=True,
            help="A software services contract with various risk clauses",
        )
    else:
        st.caption("_sample_contract.pdf not found in sample_pdfs/_")

    st.divider()
    st.markdown(
        """
        **How it works**
        1. Download a sample above (or use your own PDF)
        2. Upload it using the file uploader
        3. Click **Analyze** and wait a few seconds
        4. Review the risk score, red flags, and summary

        **Supported files:** PDF only (text-based)
        """
    )


# ── Header ────────────────────────────────────────────────────────────────────

st.title("⚖️ Legal Document Risk Analyzer")
st.caption(
    "Upload a contract, NDA, terms of service, or any legal PDF to "
    "identify potential risks and red flags instantly."
)
st.divider()

inference_mode = st.radio(
    "Inference Mode",
    [
        "Groq Cloud",
        "Local Ollama"
    ]
)
if inference_mode == "Groq Cloud":

    use_own_key = st.checkbox(
        "Use my own Groq API key (BYOK)"
    )

    user_api_key = None

    if use_own_key:
        user_api_key = st.text_input(
            "Groq API Key",
            type="password",
            help="Your key is used only for this session."
        )
else:
    user_api_key = None

if inference_mode == "Local Ollama":
    ollama_model = st.selectbox(
        "Local Model",
        [
            "llama3.2",
            "gemma3",
            "mistral",
            "qwen3"
        ]
    )
if inference_mode == "Groq Cloud":
    current_model = "☁️llama-3.3-70b-versatile (Cloud)"
else:
    current_model = f"{ollama_model} (Local)"

st.markdown(
    f"""

    **Current Model:** `🖥️{current_model}`
    """
)
if inference_mode == "Groq Cloud":
    st.success("☁️ Cloud AI Active")
else:
    st.success("🖥️ Local AI Active")


# ── Upload ────────────────────────────────────────────────────────────────────

uploaded_file = st.file_uploader(
    "Upload your legal document (PDF)",
    type=["pdf"],
    help="Max recommended size: ~50 pages. Scanned/image PDFs may not work.",
)

if uploaded_file:
    st.info(f"📄 **{uploaded_file.name}** — {uploaded_file.size / 1024:.1f} KB uploaded")

analyze_btn = st.button(
    "🔍 Analyze Document",
    type="primary",
    disabled=not uploaded_file,
    use_container_width=True,
)

if not uploaded_file:
    st.info("Upload a PDF document above to get started, or download a sample from the sidebar.")


# ── Analysis & Results ────────────────────────────────────────────────────────

if analyze_btn and uploaded_file:
    with st.spinner("Reading document and consulting AI legal analyst…"):
        try:
            file_bytes = uploaded_file.read()
            if inference_mode == "Groq Cloud":
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
            st.error(f"**Configuration Error:** {e}")
            st.stop()
        except ValueError as e:
            st.error(f"**Document Error:** {e}")
            st.stop()
        except Exception as e:
            st.error(f"**API Error:** {e}")
            st.stop()

    # ── Metrics row ──────────────────────────────────────────────────────────
    st.divider()
    st.subheader("📊 Risk Assessment Results")

    score     = result["risk_score"]
    red_flags = result["red_flags"]
    summary   = result["summary"]

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Overall Risk Score",
            value=f"{score} / 100",
            delta=risk_label(score),
            delta_color=risk_delta_color(score),
        )

    with col2:
        st.metric(
            label="Severity",
            value=f"{risk_color(score)} {risk_label(score)}",
        )

    with col3:
        st.metric(
            label="Red Flags Found",
            value=len(red_flags),
            delta="issues identified",
            delta_color="off",
        )

    # ── Progress bar ─────────────────────────────────────────────────────────
    st.progress(score / 100)

    # ── Summary ──────────────────────────────────────────────────────────────
    st.subheader("📝 Document Summary")
    st.info(summary)

    # ── Red flags ────────────────────────────────────────────────────────────
    st.subheader(f"🚩 Red Flags ({len(red_flags)} found)")

    if not red_flags:
        st.success("No significant red flags were identified in this document.")
    else:
        for i, flag in enumerate(red_flags, start=1):
            st.warning(f"**{i}.** {flag}")

    # ── Raw JSON expander ────────────────────────────────────────────────────
    with st.expander("🔧 Raw JSON Response"):
        st.json(result)

    st.divider()
    st.caption(
        "⚠️ This tool is for informational purposes only and does not "
        "constitute legal advice. Consult a qualified attorney for legal guidance."
    )
