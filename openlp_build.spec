# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

added_files = [
    ('openlp/plugins/bibles/resources', 'openlp/plugins/bibles/resources'),
    ('resources', 'resources'),
    ('.env', '.'),
]

a = Analysis(
    ['run_openlp.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        'sqlalchemy.ext.baked',
        'pyside6.qtwidgets',
        'pyside6.qtgui',
        'pyside6.qtcore',
        'pyside6.qtprintsupport',
        'pyside6.qtsvg',
        'pyside6.qtxml',
        'pyside6.qtnetwork',
        'pyside6.qtmultimedia',
        'pyside6.qtmultimediawidgets',
        'pyside6.qtwebenginecore',
        'pyside6.qtwebenginewidgets',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='OpenLP-Custom',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['resources/images/openlp-logo-64.png'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='OpenLP-Custom',
)
