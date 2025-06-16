# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=['E:\\c++3\\Python应用学习\\game'],
    binaries=[],
    datas=[
        ('E:\\c++3\\Python应用学习\\game\\images\\*', 'images'),  # 包含 images 文件夹
        ('E:\\c++3\\Python应用学习\\game\\fonts\\*', 'fonts'),  # 包含 fonts 文件夹
        ('E:\\c++3\\Python应用学习\\game\\videos\\*', 'videos')  # 包含 videos 文件夹
    ],
    hiddenimports=[
        'button',
        'constants',
        'enemy',
        'game',
        'maze',
        'menu',
        'player',
        'video_loader'
    ],
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
    a.binaries,
    a.datas,
    [],
    name='MGAME',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
