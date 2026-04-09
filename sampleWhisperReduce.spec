import os
import whisper
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None
whisper_root = os.path.dirname(whisper.__file__)
assets_folder = os.path.join(whisper_root, 'assets')

a = Analysis(
    ['sampleWhisperReduce.py'],
    pathex=[],
    binaries=[],
    datas=[(assets_folder, 'whisper/assets')],    
    hiddenimports=['soundfile'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tensorflow', 
        'tensorboard', 
        'matplotlib', 
        'scipy', 
        'sklearn', 
        'pandas', 
        'IPython',
        'librosa',
        'PIL'
    ],    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='sampleWhisperReduce',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='sampleWhisperReduce',
)

unwanted_dlls = ['torch_cuda', 'cublas', 'cudnn', 'mkl_intel_thread']
a.binaries = [x for x in a.binaries if not any(d in x[0].lower() for d in unwanted_dlls)]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='sampleWhisper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True, # Set to True if you have UPX installed
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)