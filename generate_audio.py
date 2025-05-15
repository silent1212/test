import numpy as np
from scipy.io import wavfile
import os

def generate_test_audio(filename, duration=10, sample_rate=44100):
    # Create a simple sine wave
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    # Generate different frequencies for different sounds
    if 'rain' in filename:
        # Rain-like sound (white noise)
        audio = np.random.normal(0, 1, len(t))
    elif 'waves' in filename:
        # Ocean waves (modulated sine wave)
        audio = np.sin(2 * np.pi * 0.5 * t) * np.sin(2 * np.pi * 0.1 * t)
    else:
        # Meditation music (multiple sine waves)
        audio = np.sin(2 * np.pi * 440 * t) + 0.5 * np.sin(2 * np.pi * 880 * t)
    
    # Normalize audio
    audio = audio / np.max(np.abs(audio))
    # Convert to 16-bit PCM
    audio = (audio * 32767).astype(np.int16)
    
    # Create directory if it doesn't exist
    os.makedirs('static/audio', exist_ok=True)
    
    # Save as WAV file
    wavfile.write(f'static/audio/{filename}.wav', sample_rate, audio)
    print(f'Generated {filename}.wav')

if __name__ == '__main__':
    # Generate test audio files
    generate_test_audio('rain', duration=10)
    generate_test_audio('waves', duration=10)
    generate_test_audio('meditation', duration=15) 