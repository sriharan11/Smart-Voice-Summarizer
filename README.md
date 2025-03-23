# 🧠 Smart Voice Summarizer

An intelligent audio processing pipeline that cleans noisy voice recordings, transcribes them, summarizes the content, and generates natural speech playback — all powered by AI.

## 🚀 Features

- ✅ **Noise Reduction**: Clean up background noise like wind, chatter, and taps
- 🗣️ **Transcription**: Converts speech to text using Whisper
- 📄 **Summarization**: Extracts meaningful summaries from conversations or lectures
- 🔊 **Text-to-Speech (TTS)**: Converts the summary back to clear, human-like speech using the Neuphonic API
- 🧩 **Modular Design**: Easily customize for different use cases (e.g., security, meetings, lectures)

## 🎯 Use Cases

- 🛡️ **Border Security**: Detect keywords like “bomb”, “attack”, “drugs” in voice messages and flag alerts
- 🎓 **Students**: Upload lecture recordings and receive a quick spoken summary
- 🧑‍💼 **Professionals**: Summarize noisy meetings and hear back action items

## 🛠️ Tech Stack

- Python
- Google Colab / VS Code
- [Whisper](https://github.com/openai/whisper) for transcription
- [Neuphonic](https://neuphonic.com/) for voice synthesis
- `noisereduce` / DeepFilterNet for noise cleaning
- Streamlit

## 🧑‍💻 Team Members

- **Orunika** – Noise Removal, TTS Integration (Neuphonic), Project Integration
- **Meghana** – Transcription using Whisper
- **Sriharan** – Summarization and LLM-based logic

## 📁 File Structure

