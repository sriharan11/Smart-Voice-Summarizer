import whisper
from transformers import pipeline

summarizer = pipeline("summarization")
def summarize_text(transcript, mode):
    preface = {
        "Student": "Lecture Summary:",
        "Professional": "Meeting Summary:",
        "Security Agent": "Intercept Report:"
    }.get(mode, "Summary:")

    if len(transcript.split()) < 12:
        transcript += " Please expand this text for better summarization."

    summary = summarizer(transcript, max_length=60, min_length=15, do_sample=False)
    return preface + " " + summary[0]['summary_text']


def summarize_text_security(transcript):
    # Add context to guide the summarizer
    security_prompt = (
        "Intercepted audio transcript:\n"
        + transcript +
        "\n\nSummarize this intercepted message clearly. "
        "Highlight anything suspicious or sensitive in nature."
    )

    if len(transcript.split()) < 12:
        transcript += " Please expand this for analysis."

    summary = summarizer(security_prompt, max_length=60, min_length=15, do_sample=False)
    return "Intercept Report: " + summary[0]['summary_text']
def keyword_alert(transcript):
    alert_words = ["bomb", "drugs", "smuggle", "explosive", "shipment", "border"]
    found = [word for word in alert_words if word in transcript.lower()]
    if found:
        return f"🚨 ALERT: Suspicious words detected: {', '.join(found)}"
    return None

def transcribe_audio(file_path):
    model = whisper.load_model("medium")  # Or use "small" for faster but less accurate
    result = model.transcribe(file_path)
    return result['text']