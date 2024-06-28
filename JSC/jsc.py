'''
    This is the core of JSC. Don't mess with any of this stuff if you don't know what you're doing!
    This script handles running the functions!
'''


# LIBRARIES #

import os, shlex, random

import commands

from commands import Marg
from commands import CommandList
from commands import LINES
#from commands import rmin, rmax

import colorama.ansi
from commands import Title

# END LIBRARIES #


os.system('cls')
os.system('color 3f')

CHARACTER = ""

os.system(f"cd {os.getcwd()}")
os.system('mode 75,45')

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

while True:
    global_vars = commands.CURRENT_GLOBAL_VARIABLES

    Input = input(f" {C_RESET}{os.getcwd()} {C_PURPLE}$~  {C_WHITE} ")
    _Input = shlex.split(Input)

    il = Input.lower()

    print(colorama.Fore.RESET)

    # FLAGS #
    QUIT_AFTER_FLAG = False

    LOOPCMD_FLAG = False
    LOOPCMD_FLAG_INDEX = 0

    # CORE #
    if il in ["qr", "restart", "r", "upt", "latest", "reset"]:
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        os.system("python jsc.py")

        quit()

    #il.replace("<$Random>", str(random.randint(rmin, rmax)))

    if il in ["q", "quit", "bye", "!!", "close"]:
        print("Qutting program")
        quit()
    
    # Handles flags etc
    if ("-$q" in _Input): QUIT_AFTER_FLAG = True
    if ("-$l" in _Input): 
        LOOPCMD_FLAG = True
        LOOPCMD_FLAG_INDEX = _Input.index("-$l")

    if (il == "lc"):
        print(str(LINES))
    elif (il == "listcmds"):
        print(CommandList)
    elif (_Input[0] == "xy"):
        X = int(_Input[1])
        Y = int(_Input[2])

        confirm = input(" This command will clear all the text! Y/n to proceed:")

        if (confirm.lower() == "y"):
            os.system(f'mode {X},{Y}')
        else:
            pass
        
    LINES += 1

    ###################################

    # This handles the command '#', used for listing the current direcotry.

    if _Input[0] in ["#"]:
        print(f" Current directory: '{os.getcwd()}'")

    try:
        LAST_CMD = None

        for i in CommandList:
            Cmd = i(Input, _Input)

            if Cmd == "cls":
                LINES = 1
            
            #if not Cmd == True:
                #print(f" Could not find command {_Input}, re-check spelling or make sure you added it to the `CommandList` array!")
                #break # buggy shit
            
            LAST_CMD = i
            
        if (QUIT_AFTER_FLAG == True): quit()
        if (LOOPCMD_FLAG == True): 
            try:
                AMNT = _Input[LOOPCMD_FLAG_INDEX + 1]
            except: 
                Marg()
            
            for i in range(int(AMNT)):
                LAST_CMD(Input, _Input)
                print(LAST_CMD)

    except Exception as e: 
        if (isinstance(e, IndexError)):
            Marg()
        else:
            print(e)

    Title.Reset()

############# END MAIN STUFF #############

# Notes:

# My if statements might sometimes have () and not. My style changed idk why.
# What I plan to achieve for JSC A. 1:
    # Tons of commands

# Current bugs:
    # 1. some commands arent working (new ones)
    # 2. gotta fix some other commands
    # 3. print statements are 1 line under 