import os
from pyneuphonic import Neuphonic, TTSConfig
from pyneuphonic.player import AudioPlayer

def generate_summary_audio(summary_text, output_path="summary_audio/summary.wav"):
    # Ensure output directory exists
    os.makedirs("summary_audio", exist_ok=True)

    # Set your API key
    api_key = "565469bc33e7aaaef2834639d89a4b8f3881f0f69c8a9e0b06312cc45e03241f.8deff4b3-9a18-46bb-a3ee-049d22734f16"
    client = Neuphonic(api_key=api_key)

    # TTS configuration
    tts_config = TTSConfig(
        speed=1.05,
        lang_code='en',
        voice_id='e564ba7e-aa8d-46a2-96a8-8dffedade48f'
    )

    # Stream audio and save
    sse = client.tts.SSEClient()
    with AudioPlayer() as player:
        response = sse.send(summary_text, tts_config=tts_config)
        player.play(response)
        player.save_audio(output_path)

    return output_path
