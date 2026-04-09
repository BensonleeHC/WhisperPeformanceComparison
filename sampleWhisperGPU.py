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
import torch
# Load audio without ffmpeg using librosa
def load_audio_with_librosa(file_path, sr=16000):
    """Load audio file using librosa instead of ffmpeg"""
    audio, _ = librosa.load(file_path, sr=sr)
    return audio

model = "turbo" #tiny, base, small, medium, large, turbo
# Check if CUDA is actually available
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")
model = whisper.load_model(model, device=device)

print(f"LOAD Start time: {datetime.now()}")
# Load audio manually
audio = load_audio_with_librosa("Sample.mp3")
print(f"LAOD END time: {datetime.now()}")

# Transcribe using the loaded audio array
print(f"Start time: {datetime.now()}")
result = model.transcribe(audio)
print(f"END time: {datetime.now()}")
print(result["text"])