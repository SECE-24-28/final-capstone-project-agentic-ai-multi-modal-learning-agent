import os
import tempfile
import traceback

import streamlit as st

from core.agent import EduAgent
from processors.doc_processor import DocProcessor
from processors.image_processor import ImageProcessor
from processors.voice_processor import VoiceProcessor
 
st.set_page_config(
    page_title="EduBridge AI",
    page_icon="🎓",
    layout="wide"
)
 
@st.cache_resource
def load_agent():
    return EduAgent()
 
st.markdown("""
<style>
.header {
    text-align: center;
    color: #1E88E5;
    font-size: 2.5rem;
    font-weight: bold;
}
.subheader {
    text-align: center;
    color: #888;
    font-size: 1rem;
    margin-bottom: 1rem;
}
</style>
""", unsafe_allow_html=True)
 
st.markdown('<p class="header">🎓 EduBridge AI</p>',
    unsafe_allow_html=True)
st.markdown('<p class="subheader">Autonomous Multi-Modal Early Childhood Education Assistant</p>',
    unsafe_allow_html=True)
st.divider()
 
with st.sidebar:
    st.header("⚙️ Settings")
    role = st.selectbox(
        "👤 Your Role",
        ["teacher", "parent", "admin"]
    )
    st.divider()
    st.info("""
    **🤖 Powered by:**
    - 🦙 Llama 3.1 (Local)
    - 📚 ChromaDB (RAG)
    - 🎤 Whisper (Voice)
    - 👁️ EasyOCR (Image)
    """)
 
col1, col2 = st.columns([1, 1])
 
with col1:
    st.header("📤 Input")
 
    input_type = st.radio(
        "Select Input Type",
        ["Text", "Voice", "Document", "Image"]
    )
 
    uploaded_file = None
 
    if input_type == "Voice":
        uploaded_file = st.file_uploader(
            "Upload audio",
            type=["mp3", "wav", "m4a"]
        )
        if uploaded_file:
            st.audio(uploaded_file)
 
    elif input_type == "Document":
        uploaded_file = st.file_uploader(
            "Upload PDF/Text",
            type=["pdf", "txt"]
        )
 
    elif input_type == "Image":
        uploaded_file = st.file_uploader(
            "Upload image",
            type=["jpg", "jpeg", "png"]
        )
        if uploaded_file:
            st.image(uploaded_file, width=300)
 
    query = st.text_area(
        "💭 Your Question",
        placeholder="Ask anything...",
        height=120
    )
 
    submit = st.button(
        "🚀 Ask AI",
        type="primary",
        use_container_width=True
    )
 
with col2:
    st.header("📥 AI Response")
 
    if submit:
        if not query:
            st.warning("Please enter a question!")
        else:
            with st.spinner("🤖 AI thinking..."):
                try:
                    agent = load_agent()
                    file_path = None
                    text = ""
 
                    if uploaded_file:
                        ext = uploaded_file.name.split('.')[-1]
                        with tempfile.NamedTemporaryFile(
                            delete=False,
                            suffix=f".{ext}"
                        ) as tmp:
                            tmp.write(uploaded_file.getvalue())
                            file_path = tmp.name
 
                    if file_path:
                        if input_type == "Document":
                            extracted = DocProcessor().process(file_path)
                            text = extracted.get("text", "")
                            if text and text.strip():
                                agent.rag.add_document(text)
                                st.info("📄 Document text extracted and stored.")
                                st.text_area("Exact extracted text", text, height=180)
                            else:
                                st.warning("No text could be extracted from the document.")

                        elif input_type == "Image":
                            extracted = ImageProcessor().extract_text(file_path)
                            text = extracted.get("text", "")
                            if text and text.strip():
                                agent.rag.add_document(text)
                                st.info("🖼️ Image text extracted and stored.")
                                st.text_area("Exact extracted text", text, height=180)
                            else:
                                st.warning("No text could be extracted from the image.")

                        elif input_type == "Voice":
                            extracted = VoiceProcessor().transcribe(file_path)
                            text = extracted.get("text", "")
                            if text and text.strip():
                                agent.rag.add_document(text)
                                st.info("🎤 Voice transcription stored.")
                                st.text_area("Exact transcription", text, height=180)
                            else:
                                st.warning("No speech text could be transcribed from the audio.")
 
                    response = agent.ask(query, role)
                    st.success("✅ Done!")
 
                    role_emoji = {
                        "teacher": "👩‍🏫",
                        "parent": "👨‍👩‍👧",
                        "admin": "👨‍💼"
                    }
 
                    st.markdown(
                        f"**{role_emoji[role]} Response for {role.title()}:**"
                    )
                    st.markdown(f"""
                    <div style='background:#1a1a2e;
                    padding:1.5rem;
                    border-radius:10px;
                    border-left:4px solid #1E88E5;
                    line-height:1.8;'>
                    {response}
                    </div>
                    """, unsafe_allow_html=True)
 
                    try:
                        if file_path and os.path.exists(file_path):
                            os.unlink(file_path)
                    except Exception:
                        pass
 
                except Exception as e:
                    st.error(f"❌ Error: {str(e)}")
                    st.code(traceback.format_exc())
 
st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.metric("🤖 Model", "Llama 3.1")
with c2:
    st.metric("📚 DB", "ChromaDB")
with c3:
    st.metric("🔒 Privacy", "100% Local")
 
st.caption("🎓 EduBridge AI — Final Year Project")