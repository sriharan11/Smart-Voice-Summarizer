import streamlit as st
from convert_audio import convert_mp4_to_wav
import os
from audio_cleaner import clean_audio
from neuphonic_tts import generate_summary_audio
from transcribe import transcribe_audio, summarize_text, summarize_text_security, keyword_alert
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


if "transcript" not in st.session_state:
    st.session_state.transcript = None


st.markdown("<h1 style='text-align: center; color: grey;'>Smart Voice Summarizer</h1>", unsafe_allow_html=True)
option = st.selectbox(
    "Who are you?",
    ("Student", "Professional", "Security agent"),
)
st.markdown("<br>", unsafe_allow_html=True)
uploaded_file = st.file_uploader(
    "🎙️ Upload your audio file", 
    type=["mp3", "wav","mp4"], 
    accept_multiple_files=False
)
# Reset app state if file is removed
if uploaded_file is None:
    st.session_state.transcript = None
    st.session_state.cleaned_audio_path = None

if uploaded_file is not None:
    file_name = uploaded_file.name.lower()
    st.success(f"✅ File '{file_name}' uploaded successfully!")

    save_dir = "input_audio"
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, file_name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # CLEAN AUDIO
    if st.button("🧹 Clean Audio"):
        cleaned_path = clean_audio(file_path)
        st.session_state.cleaned_audio_path = cleaned_path
        st.success("✅ Audio cleaned successfully!")

    # Play cleaned audio if available, else play original
    if (
    "cleaned_audio_path" in st.session_state and 
    st.session_state.cleaned_audio_path is not None):
        st.subheader("✨ Cleaned Audio")
        st.audio(st.session_state.cleaned_audio_path)

    else:
        st.subheader("🔊 Original Uploaded Audio")
        st.audio(file_path)

    # TRANSCRIBE
    if st.button("📝 Transcribe"):
        source_path = st.session_state.get("cleaned_audio_path", file_path)
        st.session_state.transcript = transcribe_audio(source_path)

    # SHOW TRANSCRIPT
    if st.session_state.transcript:
        st.subheader("📄 Transcript")
        st.write(st.session_state.transcript)
if st.session_state.transcript and st.button("🧠 Summarize Transcript"):
    if option == "Security agent":
        summary = summarize_text_security(st.session_state.transcript)
        alert = keyword_alert(st.session_state.transcript)


        st.subheader("🔐 Summary for Security Agent")
        st.write(summary)

        if alert:
            st.error(f"⚠️ Alert: {alert}")
        else:
            st.success("✅ No suspicious keywords detected.")
    else:
        summary = summarize_text(st.session_state.transcript, option)
        st.subheader(f"🧠 Summary for {option}")
        st.write(summary)
    audio_path = generate_summary_audio(summary)
    st.audio(audio_path)


    
