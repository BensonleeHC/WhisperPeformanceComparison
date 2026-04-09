# -*- mode: python ; coding: utf-8 -*-
import os
import whisper
# -*- mode: python ; coding: utf-8 -*-
block_cipher = None
whisper_root = os.path.dirname(whisper.__file__)
assets_folder = os.path.join(whisper_root, 'assets')

a = Analysis(
    ['sampleWhisper.py'],
    pathex=[],
    binaries=[],
    datas=[(assets_folder, 'whisper/assets')],    
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='sampleWhisper',
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
    name='sampleWhisper',
)
