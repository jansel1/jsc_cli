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

while True:
    try:

        global_vars = commands.CURRENT_GLOBAL_VARIABLES

        Input = input(f" {C_RESET}{os.getcwd()} {C_PURPLE}$~ {C_WHITE} ")
        
        for sublist in global_vars:     # Variable handling
            vname = sublist[0]
            vval = sublist[1]

            CFG_VARIABLE_SYNTAX = f"%{vname}"

            if f"%{vname}" in Input:
                Input = str(Input.replace(CFG_VARIABLE_SYNTAX, str(vval)))

        _Input = shlex.split(Input, posix=False)

        il = Input.lower()

        print(colorama.Fore.RESET)

        # FLAGS #
        QUIT_AFTER_FLAG = False

        LOOPCMD_FLAG = False
        LOOPCMD_FLAG_INDEX = 0

        ### WHRE TO PLACE FLAGS#####

        if ("-$q" in _Input): QUIT_AFTER_FLAG = True
        if (il == "lc"):
            print(str(LINES))
            
        ### BUILT IN COMMANDS END ###


        LINES += 1

        ################################### mainn 

        # This handles the command '#', used for listing the current direcotry.

        if _Input[0] in ["#"]:
            print(f" Current directory: '{os.getcwd()}'")
        try:
            LAST_CMD = None

            for i in CommandList:
                Cmd = i(Input, _Input)

                if Cmd is False:
                    print(" Command does not exist! Please input a valid command.")
                    break
                else:   
                    LAST_CMD = i
                
                if (QUIT_AFTER_FLAG == True): quit()


        except Exception as e: 
            if (isinstance(e, IndexError)):
                Marg()
            else:
                print(e)

    except Exception as e:
        print(f"{e}")

    Title.Reset()