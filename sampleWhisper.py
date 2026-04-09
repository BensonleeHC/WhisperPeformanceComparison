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

# Load audio without ffmpeg using librosa
def load_audio_with_librosa(file_path, sr=16000):
    """Load audio file using librosa instead of ffmpeg"""
    audio, _ = librosa.load(file_path, sr=sr)
    return audio


model = "tiny"
input_file = "music.mp3"
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
audio = load_audio_with_librosa(input_file)

# Transcribe using the loaded audio array
print(f"Trascribing...")
result = model.transcribe(audio,fp16=False, initial_prompt="以下是繁體中文。",task="transcribe", language="zh")
# print(result["text"])

print(f"Writing to {output_file}...")
with open(output_file, "w", encoding="utf-8") as f:
  f.write(result["text"])
print(f"END time: {datetime.now()}")