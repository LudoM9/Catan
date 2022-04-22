# Windows : 
# python setup.py build
# Ou build.bat
# Mac : 
# python3 setup.py bdist_mac
# codesign --remove-signature build/Esterel.App/Contents/MacOS/lib/Python
# Ou build.command

import sys, os
from cx_Freeze import setup, Executable

base = None
appName = "Catan"

if sys.platform == "win32":
    base = "Win32GUI"

executables = [Executable("main.py", icon = os.path.join('images', 'catan.ico'), base = base, copyright = "Copyright © 2022 MUSTIERE-LAURENT")]

buildOptions = {"packages": ["os", "pygame", "sys", "random", "numpy"], 
                "includes": ["pygame.locals", "Catan", "Joueur", "Plateau"],
                "excludes": ["tkinter"],
                #"include_files": ["images", "SONS"]
                }

buildOptionsMac = {#"include_resources": [("images", "images"), ("SONS", "SONS")],
                "iconfile": os.path.join('images', 'catan.icns'),
                "bundle_name": appName
                }

setup(
    name = appName,
    version = "1.0",
    description = "Projet informatique sur le jeu Catan",
    author = "Ludovic Mustière - Tom Laurent",
    executables = executables,
    options = {"build_exe": buildOptions, "bdist_mac": buildOptionsMac}
)