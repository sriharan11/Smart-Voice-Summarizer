import os
import noisereduce as nr
import scipy.io.wavfile as wavfile
import numpy as np

def clean_audio(input_path, output_dir="input_audio"):
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(input_path))[0]
    output_path = os.path.join(output_dir, f"{base_name}_cleaned.wav")

    rate, noisy_data = wavfile.read(input_path)

    # ✅ Convert stereo to mono if needed
    if len(noisy_data.shape) == 2:
        noisy_data = np.mean(noisy_data, axis=1).astype(noisy_data.dtype)

    cleaned_data = nr.reduce_noise(y=noisy_data, sr=rate)
    wavfile.write(output_path, rate, cleaned_data.astype(noisy_data.dtype))

    return output_path
