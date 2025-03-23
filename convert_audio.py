import os

def convert_mp4_to_wav(input_path, output_dir="input_audio"):
    from moviepy.editor import VideoFileClip

    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}.wav")

    video = VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_path)

    return output_path
