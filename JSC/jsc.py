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
from commands import rmin, rmax

# END LIBRARIES #


os.system('cls')
os.system('color 3f')

CHARACTER = ""

os.system(f"cd {os.getcwd()}")

while True:
    Input = input(f"\nJSC @ {os.getcwd()} $~ {CHARACTER} ")
    _Input = shlex.split(Input)

    il = Input.lower()

    # FLAGS #
    QUIT_AFTER_FLAG = False

    LOOPCMD_FLAG = False
    LOOPCMD_FLAG_INDEX = 0

    # CORE #
    if il in ["qr", "restart", "r", "upt", "latest", "reset"]:
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        os.system("python jsc.py")

        quit()

    il.replace("<$Random>", str(random.randint(rmin, rmax)))

    if il in ["q", "quit", "bye", "!!", "close"]:
        print("Qutting program")
        quit()
    
    if ("-$q" in _Input): QUIT_AFTER_FLAG = True
    if ("-$l" in _Input): 
        LOOPCMD_FLAG = True
        LOOPCMD_FLAG_INDEX = _Input.index("-$l")

    LINES += 1

    # This handles the /range function - used for <$Random>.

    if _Input[0] == "/range":
        try:
            min = _Input[1]
            max = _Input[2]

            if min < max:
                rmin = int(min)
                rmax = int(max)
            
                print("\t\tChanged random range sucessfully.")

            else:
                print("\t\tMinimum number cannot be bigger than maximum.")

        except: 
            Marg()

    ###################################

    # This handles the command '#', used for listing the current direcotry.
    elif _Input[0] in ["#"]:
        print(f"\t\tCurrent directory: '{os.getcwd()}'")

    #try:
    LAST_CMD = None

    for i in CommandList:
        Cmd = i(Input, _Input)

        if Cmd == "cls":
            LINES = 1
        
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

    #except: pass


############# END MAIN STUFF #############

# Notes:

# My if statements might sometimes have () and not. My style changed idk why.
# What I plan to achieve for JSC A. 1:
    # Tons of commands

# Current bugs:
    # 1. commands crashing if Marg
    # 2. some commands arent working (new ones)
    # 3. not a bug but i gotta change the default window size to a square