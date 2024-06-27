# LIBRARIES! #

import os, time
import shlex
import json
import random
import string
import webbrowser
import datetime
import subprocess
import socket
import re
import sys
import shutil
import socketserver
import fnmatch
import tkinter

from threading import Thread
from http.server import SimpleHTTPRequestHandler
from pathlib import Path

# END LIBRARIES #


os.system('cls')
os.system(f'title JanSel Command (JSC)')

rmin = 0
rmax = 100

def split(Value):
    lex = shlex.shlex(Value)

    lex.quotes = '"'
    lex.whitespace_split = True
    lex.commenters = ''

    return list(lex)

LINES = 1

CWD = "C:\\"   

def Marg():
    print("\t\tMissing arguements or an error has ocurred.")

def match_split(Table, Keyword):
    for val in Table:
        if val == Keyword:
            return Table.index(val, 0, len(Table))

def DIS_V():
    print("\t\t\t\t# JSC version: Alpha #")

############# COMMANDS #############

def Return(Input, _Input):
    if _Input[0] == "p":
        _char2 = "<$Random>"

        Input.replace('"', "'")
        _out = f"\t\t{_Input[1]}"

        print(f"{_out.replace(_char2, str(random.randint(rmin, rmax)))} ")

        return "$return"
        
def Clear(Input, _Input):
    if _Input[0] in ["cls", "clearscreen", "-"]:
        print("\t\tClearing...")

        time.sleep(0.1)
        os.system('cls')

        DIS_V()
        return "cls"
    
def LoopReturn(Input, _Input):
    if _Input[0] == "lp":
        _out = f"\t\t{_Input[1]}"

        _char1 = "<$Amount>"
        _char2 = "<$Random>"

        amt = 5
        try:
            amt = int(_Input[2])
        except:
            pass

        for i in range(amt + 1):
            e_s = (
                _out.replace(_char2, f"{random.randint(rmin, rmax)}")
                .replace(_char1, str(i))
            )

            print(e_s)

        return "$lreturn"

def ReadFile(Input, _Input):
    try:
        if _Input[0] == "readf":
            try:
                FilePath = _Input[1]
            except:
                Marg()

            
            if os.path.exists(FilePath) == False:
                print("\t\tDirectory dosen't exist")
                return
            with open(FilePath, 'r+') as file:
                print(f"\t\t{file.name}\n")
                
                print(file.read())

            return "$readf" 
    except:
        print("\t\tMissing file location arguement or could not find file")

def Delta(Input, _Input):
    if _Input[0] in ["delta", "del"]:
        FilePath = _Input[1]

        if os.path.exists(FilePath) == False:
            print("\t\tDirectory dosen't exist")
            return
        try:
            if os.path.isfile(FilePath):
                os.remove(FilePath)
            elif os.path.isdir(FilePath):
                shutil.rmtree(FilePath)
            
            print(f"\t\tRemoved file/folder '{FilePath}' sucessfully")
        except:
            print("\t\tCould not remove directory/folder.")

    return "delta"

_LETTERS_ = f"{string.ascii_letters}{string.digits}"

def Namef(Input, _Input):
    if _Input[0] == "namef":
            FilePath = _Input[1]
            DesiredName = str(_Input[2])

            if os.path.exists(FilePath) == False:
                print("\t\tDirectory dosen't exist")
                return
            
            os.rename(FilePath, str(DesiredName))
            print(f"\t\tRenamed '{FilePath}' to '{DesiredName}'")

def Cf(Input, _Input):
    if _Input[0] == "cf":
        try:
            FileName = _Input[1]
        except: Marg()
        Contents = None

        with open(f"{FileName}", "x+") as file:
            print(f"\t\tCreated file: {FileName}")
            pass

def Stiff(a, b):
    if b[0] in ["stf", "stiff", "td"]:
        try:
            File_To_GetData = b[1]
            File_To_TransferTo = b[2]
        except:
            Marg()
    
        if os.path.exists(File_To_GetData) == False or os.path.exists(File_To_TransferTo) == False:
            print("\t\tDirectory dosen't exist")
            return

        with open(File_To_GetData, "r+") as f1:
            with open(File_To_TransferTo, "w+") as f2:
                Contents = str(f1.read())
                try:
                    f2.write(Contents)
                    print(f"\t\tChanged {f1.name}'s data to '{f2.name}'")
                except:
                    print("Could not transfer data")

def Url(a, b):
    www = str(a).startswith("www.")

    if b[0] in ["http", "url"] or www:
        try:
            Link = b[1]
        except:
            if not www:
                Marg()

        if www:
            Link = a

        try:
            webbrowser.open(str(Link))
        except:
            print("\t\tCould not open page.")

def Save(a, b):
    if b[0] in ["save", "sv"]:
        try:
            FileToSave = Path(b[1])
        except:
            Marg()
        
        if os.path.exists(FileToSave) == False:
            print("\t\tDirectory dosen't exist")
            return
        
        try:
            with open(FileToSave, "r+", encoding="utf8") as f1:
                Text = f1.read()
                FName = f"{FileToSave.parent.absolute()}/{FileToSave.name}.sv"

                with open(FName, "a") as f2:
                    f2.write(f'File saved: {FileToSave.name}\n')
                    f2.write(f'Time saved: {datetime.datetime.now()}\n\n\n') 

                    f2.write(Text)

                subprocess.check_call(["attrib", "+H", FName])

                print(f"\t\tMade a save file for {FileToSave.name}")
        except:
            print("An error has occured and cannot create .sv (save) file.")

def Ip(a, b):
    dat_hn = f"\t\t{socket.gethostname()}"
    dat_ip = f"\t\t{socket.gethostbyname(socket.gethostname())}"

    dat = f"{dat_hn}\n{dat_ip}"

    if b[0] == "ip":
        try:
            if b[1] == "-L":
                Dir = ""

                try: 
                    Dir = b[2]
                except: pass

                with open(f"{Dir}", "x+") as file:
                    file.write(dat.replace("\t", ""))

                print(f"\t\tSaved your IP adress to '{Dir}'.\n")
        except: pass
        
        print(dat)


def Bomb(a, b):
    if b[0] == "bomb":
        Dir = b[1]
        Amount = int(b[2])
        
        if os.path.exists(Dir) == False:
            print("\t\tDirectory dosen't exist")
            return
        
        for i in range(Amount):
            with open(f"{Dir}/{random.randint(20000,2000000000)}.b", 'x+') as f:

                for z in range(1024*100):
                    f.write(" ")
                print(f"\t\tMade file {f.name}: {i+1}")

        print(f"\t\tSucessfully bomb'ed {Dir}")

def Reg(a, b):
    if b[0] == "reg":
        try:
            Command = b[1]
        except:
            Marg()

        print(f"{os.popen(Command).read()}")

def Blank(a, b):
    if b[0] == "blk":
        try:
            Directory = b[1]
        except:
            Marg()

        
        if os.path.exists(Directory) == False:
            print("\t\tDirectory dosen't exist")
            return
        
        try:
            for root, _, files in os.walk(Directory):
                for _f in files:
                    path = os.path.join(root, _f)

                    with open(path, "w+") as f:
                        f.write("") # lmao
                    
                    print(f"\t\tBlank'ed {path}!")
        except:
            print(f"Could not blank {Directory}")

def Corrupt(a, b):
    if b[0] == "cor":
        try:
            File = b[1]
        except: 
            Marg()
            return

        if os.path.exists(File) == False:
            print("\t\tDirectory dosen't exist")
            return
        
        try:
            with open(File, 'wb') as file:
                for i in range(255):
                    file.write(chr(random.randbytes(255)))

            print(f"Corrupted '{File}'")
        except:
            print("Could not corrupt file.")

def C(a, b):
    if b[0] in ["c", "cff"]:
        try:
            Directory = b[1]
        except:
            Marg()
            return
        try:
            os.mkdir(Directory)
            print(f"\t\tMade directory/folder: (CD) - {Directory}")
        except:
            print("\t\tCould not make directory/folder.")

def Pearl(a, b):
    RMVD = 0
    if b[0] in ["pearl", "prl", "cln", "clean"]:
        try: 
            Dir = b[1]
        except:
            Marg()
            return
        
        if os.path.exists(Dir) == False:
            print("\t\tDirectory dosen't exist")
            return
        
        for root, _, files in os.walk(Dir):
            for _f in files:
                path = os.path.join(root, _f)
                Size = os.path.getsize(path)

                if Size == 0 and os.path.isfile(path):
                    os.remove(path)
                    RMVD += 1

                    print(f"\t\tRemoved file {path}")
                elif Size != 0:
                    print(f"\t\tCould not delete file '{path}' because it is not empty.")
        if RMVD == 0:
            print("\t\tCould not find files to remove.")
        else:
            print(f"\n\t\tRemoved {RMVD} file(s)!")

def Dir(a, b):
    if b[0] in ["dir", "cd"]:
        try:
            Desired = b[1]
            
            if Desired == "-":
                Desired = os.path.dirname(os.path.realpath(__file__))

            os.chdir(Desired)
            print(f"\t\t Changed working directory to '{Desired}'")
        except: Marg()

def Run(a, b):
    if b[0] == "run.py":
        try:
            FilePath = b[1]
            os.system(f"python {FilePath}")
        except:
            Marg()

    elif b[0] == "run.t":
        try:
            FilePath = b[1]
            os.system(f"{FilePath}")
        except:
            Marg()
            return

def SocketInfo(a, b):
    _h = False
    if b[0] == "ski":
        try:
            Socket_HN = b[1]
        except:
            Marg()
            return

        if b[1] == "-H":
            Socket_HN = b[2]
            
            try:
                try:
                    hn = socket.gethostbyaddr(Socket_HN)
                except: print("\t\tCould not get IP.")

                print(f"\t\tHost name: {hn}")
            except:
                print("\t\tCould not resolve host name.")

            _h = True

        try:
            if _h == True: return

            try:
                ip = socket.gethostbyname(Socket_HN)
            except: print("\t\tCould not get host.")

            print(f"\t\tIP: {ip}")
        except: print("\t\tCould not resolve IP.")

def working(a, b):
    if b[0] in ["working", "test"]:
        for i in range(random.randint(1200, 9000)):
            print(f"TESTING.... {i}")
            print(f"WARMING UP... {random.choice(_LETTERS_)}")
def hello(full, split):
    if split[0] == "/hi":
      print("Halloes!")
      
def Hide(a, b):
    def attr(c, d):
        try:
            subprocess.check_call(["attrib", d, c])
        except: 
            print(f"Could not hide file/folder '{FName.name}'.")


    if b[0] == "hif":
        try:
            FName = Path(str(b[1]))

            try:
                if b[1] == "/u":
                    try:
                        FName = Path(str(b[2]))
                    except: 
                        Marg()
                        return

                    attr(FName, "-H")
                    print(f"\t\tMade {FName.name} visible. (Changes might take some seconds to show)")

                    return
            except: pass

            attr(FName, "+H")
            
            print(f"\t\tMade {FName.name} hidden. (Changes might take some seconds to show)")
        except:
            Marg()
            return

def _Time(a, b):
    if b[0] in ["time", "t"]:
        print(f"\t\t{datetime.datetime.now()}")

def wifi(a, b):
    if b[0] == "wif":
        print(str(subprocess.check_output("netsh wlan show profiles name=*")).replace("\\n", "\n").replace("\\r", "\r"))

def jsc(a, b):
    if b[0] == "jsc":
        webbrowser.open('jansel.pages.dev')
        print("\t\tThanks for using JSC!")

PRINTABLE = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

def Random(a, b):
    if b[0] == "randint":
        try:
            MIN_NUMBER = int(b[1])
            MAX_NUMBER = int(b[2])

        except: 
            Marg()
            return
        
        try:
            if not MIN_NUMBER > MAX_NUMBER:
                RESULT = random.randint(MIN_NUMBER, MAX_NUMBER)

                print(f"\t\t{RESULT}")
            else:
                print(f"\t\tCannot have the minimum number bigger than the maximum. Did you mean: randint {MAX_NUMBER} {MIN_NUMBER} ?")
        except:
            print("\t\tCould not get random number.")

    elif b[0] == "randstr":
        CanUseLetters = True

        try:
            LETTERS = b[1]
        except: 
            CanUseLetters = False

        if CanUseLetters:
            RESULT = random.choice(list(LETTERS))

            print(f"\t\t{RESULT}")
        else:
            RESULT = random.choice(PRINTABLE)

            print(f"\t\t{RESULT}")

def Explorer(a, b): # simple function, but ya' never know ;)
    if b[0] in ["explorer.exe", "explorer", "exp", "exp.exe"]:
        os.system("explorer.exe")

def Open(a, b):
    if b[0] == "$":
        try:
            PROGRAM_TO_OPEN = b[1]
        except: Marg()

        try:
            os.system(f"{PROGRAM_TO_OPEN}.exe")
        except: 
            print("\t\tCould not open program, make sure the program name is correct.")

def ByteView(a, b):
    if b[0] == "readb":
        try:
            FILE_TO_READ = b[1]
        except: 
            Marg()

            return

        try:
            with open(FILE_TO_READ, 'rb') as file:
                print(file.read())
        except:
            print("\t\tCould not read the byte data for file.")

def Window(a, b):
    if b[0] == "window":
        def tk(title="No title yet..", size="500x500", text="Hello"):
            tkroot = tkinter.Tk()

            tkroot.title(title)
            tkroot.geometry(size)

            tkinter.Label(tkroot, text=text).pack()

            tkinter.mainloop()

        try:
            title = b[1]
            size = b[2]
            text= b[3]
        except:
            Marg()
            return
        
        print("\t\tOpening window...")
        tk(title=title, size=size, text=text)

def MkShortcut(a, b):
    if b[0] in ["ms", "mks", "short", "portal", "witch"]:
        try:
            Location = b[1]
            Destination = b[2]
            Name = b[3]
        except:
            Marg()
            return
        

############# COMMANDS END #############

CommandList = [ # Once you make a new function, add it here!
    Return,
    Clear,
    LoopReturn,
    ReadFile,
    Delta,
    Namef,
    Cf,
    Stiff,
    Url,
    Save,
    Ip,
    Bomb,
    Reg,
    Blank,
    Corrupt,
    C,
    Pearl,
    Dir,
    Run,
    SocketInfo,
    working,
    Hide,
    _Time,
    wifi,
    jsc,
    Random,
    Explorer,
    Open,
    ByteView,
    Window
]