'''
    This is the core of JSC. Don't mess with any of this stuff if you don't know what you're doing!
    This script handles running the functions!

    THIS IS THE JSC SYNTAX COMPILER!
'''


# LIBRARIES #

import os, shlex, random, subprocess

import commands
import sys, io

from commands import Marg
from commands import CommandList
from commands import LINES
#from commands import rmin, rmax

import colorama.ansi
from rich.console import Console
from commands import Title

# END LIBRARIES #

help_messages = {
    "echo": "Usage: echo <message>\nEchoes the given message.",
    "cls": "Usage: cls [-ec]\nClears the screen. Use -ec to keep command history.",
    "lecho": "Usage: lecho <message> <times>\nEchoes the given message multiple times.",
    "readf": "Usage: readf <file_path> [-cc]\nReads the file. Use -cc to copy content to clipboard.",
    "del": "Usage: del <file_path>\nDeletes the given file.",
    "namef": "Usage: namef <file_path> <new_name>\nRenames the given file.",
    "cf": "Usage: cf <file_name>\nCreates a new file with the given name.",
    "stf": "Usage: stf <source_file> <destination_file>\nCopies content from source to destination file.",
    "url": "Usage: url <url>\nOpens the given URL in a web browser.",
    "save": "Usage: save <file_path>\nCreates a hidden save file for the given file.",
    "ip": "Usage: ip\nDisplays IP information.",
    "bomb": "Usage: bomb <directory> <amount>\nCreates dummy files in the given directory.",
    "reg": "Usage: reg <command>\nRuns the given command and displays output.",
    "blank": "Usage: blank <directory> [-del]\nBlanks or deletes files in the given directory.",
    "cor": "Usage: cor <file>\nCorrupts the given file.",
    "c": "Usage: c <directory>\nCreates the given directory.",
    "pearl": "Usage: pearl <directory>\nRemoves empty files and directories.",
    "dir": "Usage: dir <directory>\nChanges the current directory. (USE cd FOR SIMPLICITY.)",
    "run.py": "Usage: run.py <file_path>\nRuns the given Python script.",
    "ski": "Usage: ski <hostname or ip> [-h]\nDisplays IP or hostname information. Use -h to display hostname of the IP.",
    "test": "Usage: test\nRuns a test command.",
    "/hi": "Usage: /hi\nGreets the user.",
    "hif": "Usage: hif <file_path> [/u]\nHides or unhides the given file. Use /u to unhide.",
    "time": "Usage: time\nDisplays the current time.",
    "wif": "Usage: wif\nDisplays Wi-Fi profiles.",
    "jsc": "Usage: jsc\nOpens the JSC website.",
    "randint": "Usage: randint <min> <max>\nGenerates a random integer between min and max.",
    "randstr": "Usage: randstr [characters]\nGenerates a random string from the given characters.",
    "explorer": "Usage: explorer\nOpens File Explorer.",
    "$": "Usage: $<program>\nRuns the given program or command.",
    "readb": "Usage: readb <file>\nReads the file in binary mode.",
    "ms": "Usage: ms <location> <destination>\nCreates a shortcut.",
    "wclone": "Usage: wclone <url> [-cc]\nClones the given URL to a file or clipboard. Use -cc to copy to clipboard.",
    "webstat": "Usage: webstat <url> [-ping]\nDisplays the status of the given URL. Use -ping to ping the URL.",
    "syscan": "Usage: syscan <directory> <name> [-c] [#]\nScans for files or directories with the given name. Use -c to scan C drive, # to scan current working directory.",
    "%": "Usage: % <variable_name> <value> [-math]\nDefines a global variable. Use -math to evaluate the value as a math expression.",
    "globals": "Usage: globals\nDisplays global variables.",
    "listmk": "Usage: listmk <data> [-h header1 header2]\nCreates a list with optional headers.",
    "deltn": "Usage: deltn <directory> <name> [-find]\nDeletes files or directories by name. Use -find to delete files containing the name.",
    "proc": "Usage: proc <process_name> [-t] [-ft] [-list] [-cud]\nManages processes. Use -t to terminate, -ft to force terminate, -list to list processes, -cud to disable CPU usage.",
    "sysinfo": "Usage: sysinfo\nDisplays system information.",
    "pyutil": "Usage: pyutil <file> [-dir] [-sta] [-exe]\nUtilities for Python. Use -dir to create one directory, -sta for standalone file, -exe to convert to exe.",
    "path": "Usage: path <directory> [-list] [-mk]\nManages system PATH. Use -list to list PATH directories, -mk to add directory to PATH.",
    "fort": "Usage: fort <file_path> <sort_type>\nSorts file content. Sort types: -dupes, -reverse.\n-dupes: Removes duplicate lines.\n-reverse: Reverses the file lines.",
    "broot": "Usage: broot <extra_tags> <amount>\nGenerates password lists with variations. Seperate tags with ',',.\nEXAMPLE: broot python,cplus,vscode 10000",
    "xy": "Usage: xy <X> <Y>\nSets terminal window size to X columns and Y rows. May not work in Windows Terminal.",
    "whoami": "Usage: whoami\nDisplays the current user and home directory.",
    "ld": "Usage: ld\nLists directory contents.",
    "qr": "Usage: qr\nRestarts the script.",
    "quit": "Usage: quit\nExits the script.",
    "exists": "Usage: exists <file_path>\nChecks if the given file exists.",
    "stat": "Usage: stat <file_path>\nDisplays file statistics.",
    "shutd": "Usage: shutd\nInitiates the Remote Shutdown Dialog.",
    "ips": "Usage: ips\nDisplays network IPs.",
    "ls": "Usage: ls\nLists files and folders in the current directory. Folders will be marked with a magenta/pruple background.",
    "weather": "Usage: weather [city]\nDisplays weather information for the given city or current location.",
    "unwrap": "Usage: unwrap <url>\nDisplays the final destination of the given URL.",
    "qrcode": "Usage: qrcode <website>\nGenerates a QR code for the given website.",
    "writef": "Usage: writef <file_path> [-n]\nWrites to the given file. Use -n to open in a new window.",
    "crypt": "Usage: crypt <file_path> <password> [-e] [-text] [-passlist]\nEncrypts or decrypts the given file. \nUse -e to encrypt (or don't add -e for decryption), \n-text for text mode, \n-passlist to use password list.",
    "email": "Usage: email <sender_email> <receiver_email> <subject> <body> <password>\nSends an email with the given parameters.",
    "htmv": "Usage: htmv <file_path>\nDisplays HTML file content in a styled manner.",
    "attr": "Usage: attr <file_path> <attributes>\nAdds attributes to the given file. Attributes: +readonly, -readonly, +hidden, -hidden, +system, -system, +archive, -archive, +nci, -nci, +offline, -offline, +temporary, -temporary, +sparsefile, -sparsefile, +reparsepoint, -reparsepoint, +compressed, -compressed, +encrypted, -encrypted."
}

os.system('cls')

CHARACTER = ""

os.system(f"cd {os.getcwd()}")

def CUSTOM_COLOR(red, green, blue):
    return f'\033[38;2;{red};{green};{blue}m'

C_GREEN = CUSTOM_COLOR(17, 236, 52)
C_PURPLE = CUSTOM_COLOR(128, 0, 128)
C_RED = CUSTOM_COLOR(234, 43, 21)
C_RESET = CUSTOM_COLOR(242, 242, 242)
C_WHITE = CUSTOM_COLOR(255, 255, 255)

Title.Reset()

min_ = 0
max_ = 100

inp =  f" {C_RESET}{os.getcwd()} {C_PURPLE}$~ {C_WHITE} "

while True:
    command_found = False

    try:

        global_vars = commands.CURRENT_GLOBAL_VARIABLES
        inp =  f" {C_RESET}{os.getcwd()} {C_PURPLE}$~ {C_WHITE} "
        print()

        Input = input(inp)
        Input = Input.replace("\\", "\\\\")
                              
        for sublist in global_vars:     # Variable handling
            vname = sublist[0]
            vval = sublist[1]

            CFG_VARIABLE_SYNTAX = f"%{vname}"

            if f"%{vname}" in Input:
                Input = str(Input.replace(CFG_VARIABLE_SYNTAX, str(vval)))

        _Input = shlex.split(Input)

        il = Input.lower()

        print(colorama.Fore.RESET, end="\r")

        # FLAGS #
        QUIT_AFTER_FLAG = False

        LOOPCMD_FLAG = False
        LOOPCMD_FLAG_INDEX = 0


        if ("-$q" in _Input): QUIT_AFTER_FLAG = True
        if (il == "lc"):
            print(str(LINES))

        if il == "help":
            for cmd in help_messages:
                print(f"{C_PURPLE}{cmd}{C_RESET}: {help_messages[cmd]}\n")
                command_found = True

        LINES += 1

        if _Input[0] in ["#"]:
            print(f" Current directory: '{os.getcwd()}'")

        EXIT = False

        try:
            LAST_CMD = None

            for i in CommandList:
                try:
                    if "/?" in _Input:
                        for cmds in help_messages:
                            if _Input[0] in help_messages:
                                print(help_messages[_Input[0]])

                                EXIT = True
                                command_found = True

                                break

                    if EXIT: break
                except Exception as e: print(f"HELPER (/?) - Command not found within documentation. {e}")
                
                Cmd = i(Input, _Input)

                if Cmd is None:
                    continue
                else:
                    command_found = True
                    commands._line_data.append(f"{inp}{Input}")

                    break
                
            if (QUIT_AFTER_FLAG == True): quit()
            

            if not command_found:
                print(" Command does not exist! Please input a valid command.")

        except Exception as e: 
            if (isinstance(e, IndexError)):
                Marg()
                print(f"ErrorName: <{e}>")
            else:
                print(e)

    except Exception as e:
        print(f"{e}")

    Title.Reset()