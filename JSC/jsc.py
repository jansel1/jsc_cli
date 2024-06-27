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
    Input = input(f"\n\tjsc $~ {CHARACTER} ")
    _Input = shlex.split(Input)

    il = Input.lower()

    if il in ["qr", "restart", "r", "upt", "latest", "reset"]:
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        os.system("python jsc.py")

        quit()

    il.replace("<$Random>", str(random.randint(rmin, rmax)))

    if il in ["q", "quit", "bye", "!!", "close"]:
        print("Qutting program")
        quit()

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
    for i in CommandList:
        Cmd = i(Input, _Input)

        if Cmd == "cls":
            LINES = 1
    #except: pass


############# END MAIN STUFF #############