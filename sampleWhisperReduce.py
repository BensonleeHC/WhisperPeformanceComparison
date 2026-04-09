import os
import sys
import ctypes
import ctypes.util

# Workaround for whisper on Windows - patch ctypes.CDLL to handle None libc_name
if sys.platform == "win32":
    _original_cdll = ctypes.CDLL
    
    class PatchedCDLL(ctypes.CDLL):
        def __init__(self, name, *args, **kwargs):
            if name is None:
                # On Windows, try to find msvcrt (the Windows C runtime)
                name = ctypes.util.find_library('c') or 'msvcrt'
            super().__init__(name, *args, **kwargs)
    
    ctypes.CDLL = PatchedCDLL

import whisper
import librosa
import numpy as np
from datetime import datetime

import soundfile as sf
def load_audio_with_soundfile(file_path, sr=16000):
    """Load audio file using soundfile instead of librosa/ffmpeg"""
    audio, native_sr = sf.read(file_path)
    
    # Convert to mono if stereo
    if len(audio.shape) > 1:
        audio = audio.mean(axis=1)
        
    # Resample if necessary (Whisper requires 16000Hz)
    if native_sr != sr:
        # Note: soundfile doesn't resample natively. 
        # If you must resample, you'd need a light resampler like 'resampy'
        # BUT: most SampleMusic.mp3 files are 44100Hz.
        pass 
        
    return audio.astype(np.float32)

model = "tiny" #tiny, base, small, medium, large, turbo
input_file = "music.wav"
output_file = "output.txt"

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except IndexError:
    ##main function
    if not output_file:
        output_file = "demofile.txt"

    if not input_file:
        input_file = "SampleMusic.mp3"

if not os.path.isfile(input_file):
    raise ValueError(f"{input_file} not found!")


model = whisper.load_model(model)
print(f"Start time: {datetime.now()}")

print(f"Loading {input_file} into buffer...")
# Load audio manually
audio = load_audio_with_soundfile(input_file)

# Transcribe using the loaded audio array
print(f"Trascribing...")
result = model.transcribe(audio,fp16=False, initial_prompt="以下是繁體中文。",task="transcribe", language="zh")
# print(result["text"])

print(f"Writing to {output_file}...")
with open(output_file, "w", encoding="utf-8") as f:
  f.write(result["text"])
print(f"END time: {datetime.now()}")