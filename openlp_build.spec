# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_submodules

block_cipher = None

added_files = [
    ('openlp/core/ui/fonts', 'core/ui/fonts'),
    ('openlp/core/display/html', 'core/display/html'),
    ('openlp/plugins', 'plugins'),
    ('openlp/core/lib/json', 'core/lib/json'),
    ('resources', 'resources'),
    ('.env', '.'),
]

a = Analysis(
    ['run_openlp.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[
        'openlp.core.app',
        'openlp.__main__',
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
        'openlp.plugins.alerts.alertsplugin',
        'openlp.plugins.bibles.bibleplugin',
        'openlp.plugins.custom.customplugin',
        'openlp.plugins.images.imageplugin',
        'openlp.plugins.media.mediaplugin',
        'openlp.plugins.obs_studio.obs_studio_plugin',
        'openlp.plugins.planningcenter.planningcenterplugin',
        'openlp.plugins.presentations.presentationplugin',
        'openlp.plugins.songs.songsplugin',
        'openlp.plugins.songusage.songusageplugin',
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
    icon='resources/images/OpenLP.ico',
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
