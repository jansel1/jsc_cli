import os, sys

print("Installing ` winshell `... (REQUIRED FOR THE SHORTCUT FILE)\n")


os.system('pip install winshell')

WINSHELL_INSTALLED = False

try:
    import winshell
    WINSHELL_INSTALLED = True
except:
    print("Cannot find module ` winshell `")
    WINSHELL_INSTALLED = False

    raise ModuleNotFoundError

print("Making shortcut file...")


def Shortcut():
    script_dir = os.path.dirname(os.path.abspath(__file__))

    target_path = os.path.join(script_dir, 'APP.bat')
    shortcut_name = 'JSC'

    desktop = winshell.desktop()

    shortcut = winshell.shortcut(os.path.join(desktop, f'{shortcut_name}.lnk'))
    shortcut.path = target_path
    shortcut.write()

try:
    Shortcut()
except:
    print("Could not make shortcut...")