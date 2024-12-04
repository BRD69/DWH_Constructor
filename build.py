import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',
    '--onefile',
    '--windowed',
    '--name=dwhc',
    '--icon=icon512.ico',
    '--distpath=build',
])

# PyInstaller.__main__.run(['main.spec'])