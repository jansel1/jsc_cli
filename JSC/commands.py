# LIBRARIES!

import os, time
import shlex
import random
import string
import webbrowser
import datetime
import subprocess
import socket
import shutil
import tkinter
import win32com.client
import pythoncom
import colorama.ansi
import requests
import pyperclip

from tabulate import tabulate
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from threading import Thread
from http.server import SimpleHTTPRequestHandler
from pathlib import Path

# END LIBRARIES #

BLUE = colorama.Fore.BLUE
GREEN = colorama.Fore.GREEN
RED = colorama.Fore.RED

os.system('cls')

global rmin
global rmax

def split(Value):
    lex = shlex.shlex(Value)

    lex.quotes = '"'
    lex.whitespace_split = True
    lex.commenters = ''

    return list(lex)

LINES = 1

CWD = "C:\\"   

def Marg():
    print(" Missing arguements or an error has ocurred.")

def match_split(Table, Keyword):
    for val in Table:
        if val == Keyword:
            return Table.index(val, 0, len(Table))

def DIS_V():
    print("  # JSC version: Alpha #")

class Title:
    def Custom(text):
        os.system(f"title {text}")
    
    def Reset():
        os.system(f"title JanSel Command (JSC)")

############# COMMANDS #############

def Range(a, b): # wip
    if b[0] == "range":
        min_ = b[1]
        max_ = b[2]

        if min_ < max_:
            rmin = int(min)
            rmax = int(max)
            
            print(" Changed random range sucessfully.")

        else:
            print(" Minimum number cannot be bigger than maximum.")

def Return(Input, _Input):
    if _Input[0] == "cout":
        _char2 = "<$Random>"

        Input.replace('"', "'")
        _out = f" {_Input[1]}"

        print(f"{_out.replace(_char2, str(random.randint(rmin, rmax)))} ")

        return True
        
def Clear(Input, _Input):
    if _Input[0] in ["cls", "clearscreen", "-"]:
        print(" Clearing...")

        time.sleep(0.1)
        os.system('cls')

        return True
    
def LoopReturn(Input, _Input):
    if _Input[0] == "lcout":
        _out = f" {_Input[1]}"

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

        return True

def ReadFile(Input, _Input):
    try:
        if _Input[0] == "readf":
            try:
                FilePath = _Input[1]
            except:
                Marg()

            
            if os.path.exists(FilePath) == False:
                print(" Directory dosen't exist")
                return
            with open(FilePath, 'r+') as file:
                print(f" {file.name}\n")
                
                print(file.read())

            return True 
    except:
        print(" Missing file location arguement or could not find file")
        return True

def Delta(Input, _Input):
    if _Input[0] in ["delta", "del"]:
        FilePath = _Input[1]

        if os.path.exists(FilePath) == False:
            print(" Directory dosen't exist")
            return
        try:
            if os.path.isfile(FilePath):
                os.remove(FilePath)
            elif os.path.isdir(FilePath):
                shutil.rmtree(FilePath)
            
            print(f" Removed file/folder '{FilePath}' sucessfully")
        except:
            print(" Could not remove directory/folder.")

    return True

_LETTERS_ = f"{string.ascii_letters}{string.digits}"

def Namef(Input, _Input):
    if _Input[0] == "namef":
            FilePath = _Input[1]
            DesiredName = str(_Input[2])

            if os.path.exists(FilePath) == False:
                print(" Directory dosen't exist")
                return
            
            os.rename(FilePath, str(DesiredName))
            print(f" Renamed '{FilePath}' to '{DesiredName}'")
            return True

def Cf(Input, _Input):
    if _Input[0] == "cf":
        try:
            FileName = _Input[1]
        except: Marg()
        Contents = None

        with open(f"{FileName}", "x+") as file:
            print(f" Created file: {FileName}")
            pass
        return True

def Stiff(a, b):
    if b[0] in ["stf", "stiff", "td"]:
        try:
            File_To_GetData = b[1]
            File_To_TransferTo = b[2]
        except:
            Marg()
    
        if os.path.exists(File_To_GetData) == False or os.path.exists(File_To_TransferTo) == False:
            print(" Directory dosen't exist")
            return

        with open(File_To_GetData, "r+") as f1:
            with open(File_To_TransferTo, "w+") as f2:
                Contents = str(f1.read())
                try:
                    f2.write(Contents)
                    print(f" Changed {f1.name}'s data to '{f2.name}'")
                except:
                    print("Could not transfer data")
        return True

def geturl(url):
    Link = url

    if not str(url).startswith("https://"):
        Link = f"https://{url}"

    return Link

def Url(a, b):
    www = str(a).startswith("www.")

    if b[0] in ["http", "url"] or www:
        Link = geturl(b[1])

        try:
            webbrowser.open(str(Link))
        except:
            print(" Could not open page.")
        return True

def Save(a, b):
    if b[0] in ["save", "sv"]:
        try:
            FileToSave = Path(b[1])
        except:
            Marg()
        
        if os.path.exists(FileToSave) == False:
            print(" Directory dosen't exist")
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

                print(f" Made a save file for {FileToSave.name}")
        except:
            print("An error has occured and cannot create .sv (save) file.")
        return True

def Ip(a, b):
    dat_hn = f" {socket.gethostname()}"
    dat_ip = f" {socket.gethostbyname(socket.gethostname())}"

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

                print(f" Saved your IP adress to '{Dir}'.\n")
        except: pass
        
        print(dat)
        return True

def Bomb(a, b):
    if b[0] == "bomb":
        Dir = b[1]
        Amount = int(b[2])
        
        if os.path.exists(Dir) == False:
            print(" Directory dosen't exist")
            return
        
        for i in range(Amount):
            with open(f"{Dir}/{random.randint(20000,2000000000)}.b", 'x+') as f:

                for z in range(1024*100):
                    f.write(" ")
                print(f" Made file {f.name}: {i+1}")

        print(f" Sucessfully bomb'ed {Dir}")
        return True

def Reg(a, b):
    if b[0] == "reg":
        try:
            Command = b[1]
        except:
            Marg()

        print(f"{os.popen(Command).read()}")
        return True

def Blank(a, b):
    if b[0] == "blk":
        try:
            Directory = b[1]
        except:
            Marg()

        
        if os.path.exists(Directory) == False:
            print(" Directory dosen't exist")
            return
        
        try:
            for root, _, files in os.walk(Directory):
                for _f in files:
                    path = os.path.join(root, _f)

                    with open(path, "w+") as f:
                        f.write("") # lmao
                    
                    print(f" Blank'ed {path}!")
        except:
            print(f"Could not blank {Directory}")
        return True

def Corrupt(a, b):
    if b[0] == "cor":
        try:
            File = b[1]
        except: 
            Marg()
            return

        if os.path.exists(File) == False:
            print(" Directory dosen't exist")
            return
        
        try:
            with open(File, 'wb') as file:
                for i in range(255):
                    file.write(chr(random.randbytes(255)))

            print(f"Corrupted '{File}'")
        except:
            print("Could not corrupt file.")
        return True

def C(a, b):
    if b[0] in ["c", "cff"]:
        try:
            Directory = b[1]
        except:
            Marg()
            return
        try:
            os.mkdir(Directory)
            print(f" Made directory/folder: (CD) - {os.path.abspath(Directory)}")
        except:
            print(" Could not make directory/folder.")
        return True

def Pearl(a, b):
    RMVD = 0

    if b[0] in ["pearl", "prl", "cln", "clean", "powerwash", "purge"]:
        try: 
            Dir = b[1]
        except:
            Marg()
            return
        
        try:
            if os.path.exists(Dir) == False:
                print(" Directory dosen't exist")
                return
            
            for root, dirs, files in os.walk(Dir):
                for _f in files:
                    path = os.path.join(root, _f)
                    path = path.encode('utf-8', 'replace').decode('utf-8')

                    try:
                        Size = os.path.getsize(path)

                        if os.access(path, os.R_OK) and os.access(path, os.W_OK):
                            Title.Custom(f"title JanSel Command (JSC)  REMOVED FILES: {RMVD}")

                            if Size == 0 and os.path.isfile(path):
                                os.remove(path)
                                RMVD += 1

                    except Exception as e:
                        pass

                    for _d in dirs:
                        dir_path = os.path.join(root, _d)
                        dir_path = dir_path.encode('utf-8', 'replace').decode('utf-8')

                        try:
                            if not os.listdir(dir_path):
                                os.rmdir(dir_path)
                                RMVD += 1
                        except (PermissionError, OSError) as e:
                            pass
            if RMVD == 0:
                print(" Could not find files to remove.")
            else:
                print(f"\n Removed {RMVD} file(s)!")

        except Exception as e:
            print(f"ERROR! {e}")
            print(f"Error is most probably a permission issue. The directory might be protected or locked.")

        return True

def Dir(a, b):
    if b[0] in ["dir", "cd"]:
        try:
            Desired = b[1]
            
            if Desired == "-":
                Desired = os.path.dirname(os.path.realpath(__file__))

            os.chdir(Desired)
            print(f"  Changed working directory to '{Desired}'")
            return True
        except: Marg()

def Run(a, b):
    if b[0] == "run.py":
        try:
            FilePath = b[1]
            os.system(f"python {FilePath}")
            return True
        except:
            Marg()

    elif b[0] == "run.t":
        try:
            FilePath = b[1]
            os.system(f"{FilePath}")
            return True
        except:
            Marg()

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
                except: print(" Could not get IP.")

                print(f" Host name: {hn}")
            except:
                print(" Could not resolve host name.")

            _h = True

        try:
            if _h == True: return

            try:
                ip = socket.gethostbyname(Socket_HN)
            except: print(" Could not get host.")

            print(f" IP: {ip}")
            return True
        except: print(" Could not resolve IP.")

def working(a, b):
    if b[0] in ["working", "test"]:
        for i in range(random.randint(1200, 9000)):
            print(f"TESTING.... {i}")
            print(f"WARMING UP... {random.choice(_LETTERS_)}")
        return True
    
def hello(full, split):
    if split[0] == "/hi":
      print("Halloes!")
      return True
      
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
                    print(f" Made {FName.name} visible. (Changes might take some seconds to show)")

                    return
            except: pass

            attr(FName, "+H")
            
            print(f" Made {FName.name} hidden. (Changes might take some seconds to show)")
            return True
        except:
            Marg()
            return

def _Time(a, b):
    if b[0] in ["time", "t"]:
        print(f" {datetime.datetime.now()}")
        return True

def wifi(a, b):
    if b[0] == "wif":
        print(str(subprocess.check_output("netsh wlan show profiles name=*")).replace("\\n", "\n").replace("\\r", "\r"))
        return True

def jsc(a, b):
    if b[0] == "jsc":
        webbrowser.open('jansel.pages.dev')
        print(" Thanks for using JSC!")
        return True

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

                print(f" {RESULT}")
            else:
                print(f" Cannot have the minimum number bigger than the maximum. Did you mean: randint {MAX_NUMBER} {MIN_NUMBER} ?")
        except:
            print(" Could not get random number.")
            return True
        return True
    elif b[0] == "randstr":
        CanUseLetters = True

        try:
            LETTERS = b[1]
        except: 
            CanUseLetters = False

        if CanUseLetters:
            RESULT = random.choice(list(LETTERS))

            print(f" {RESULT}")
        else:
            RESULT = random.choice(PRINTABLE)

            print(f" {RESULT}")
        return True

def Explorer(a, b): # simple function, but ya' never know ;)
    if b[0] in ["explorer.exe", "explorer", "exp", "exp.exe"]:
        os.system("explorer.exe")
        return True

def Open(a, b):
    if a[0] == "$":
        try:
            PROGRAM_TO_OPEN = str(a)[1:]
        except: Marg()

        try:
            os.system(f"{PROGRAM_TO_OPEN}")
        except: 
            print(" Could not open program, make sure the program name is correct.")
        
        return True

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
            print(" Could not read the byte data for file.")

        return True
    
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
        
        print(" Opening window...")
        tk(title=title, size=size, text=text)

        return True

def MkShortcut(a, b):
    if b[0] in ["ms", "mks", "short", "portal", "witch"]:
        try:
            Location = b[1]
            Destination = b[2]
            Name = b[3]
        except:
            Marg()
            return
        
        shell = win32com.client.Dispatch("WScript.Shell")

        shortcut = shell.CreateShortCut(f"{os.path.join(Destination, Name)}.lnk") # buggy for now it's WIP
        shortcut.TargetPath = os.path.abspath(Location)
        shortcut.WindowStyle = 1

        shortcut.save()

        print(f" Made shortcut ({os.path.realpath(Destination)})")

        return True

def CloneURL(a, b):
    if b[0] in ['wclone', 'corl', 'webclone']:
        COPY_TO_CLIPBOARD_f = False

        try:
            URL = geturl(b[1])
        except:
            Marg()
            return

        if "-cc" in b != -1: COPY_TO_CLIPBOARD_f = True
        
        url = str(URL)

        response = requests.get(url)

        if response.status_code == 200:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            loc = None

            if COPY_TO_CLIPBOARD_f == False:
                with open(f"cloneurl-{time.time()}.html", "w", encoding="utf-8") as file:
                    file.write(str(soup.prettify()))
                    loc = os.path.abspath(file.name)
            else:
                pyperclip.copy(str(soup.prettify()))
                loc = "clipboard"

            print(f"Cloned {url} to {loc}")
        else:
            print(f"Failed to retrieve the website. Status code: {response.status_code}")

        return True

def WebStat(a, b):
    PING_FLAG = False
    PING_ALOT_FLAG = False

    if (b[0] in ["webstat", "webs", "reqstat"]):
        status = "N/A"

        URL = geturl(str(b[1]))

        if "-ping" in b: PING_FLAG = True
        if "-pingfr" in b: PING_ALOT_FLAG = True

        try:
            res = requests.get(URL)
        except Exception as e:
            print(f"`{URL}` does not exist or isn't online!")

            return

        if (res.status_code == 200): status = f"`{URL}` is online"
        else:
            print(f"Status for {URL} is {res.status_code}")

        if (PING_FLAG):
            os.system(f"ping -n 10 {urlparse(URL).netloc}")

            print("\n")
        elif (PING_ALOT_FLAG):
            while True:
                try:
                    os.system(f"ping -t {urlparse(URL).netloc}")
                except KeyboardInterrupt:
                    break

        print(status)
        return True

def FindFile(a, b):
    C_DRIVE_FLAG = False
    CWD_DIR_FLAG = False

    if b[0] in ["syscan", "dscan"]:
        path = os.path.abspath(str(b[1]))
        name = str(b[2])
        
        if "-c" in b: C_DRIVE_FLAG = True
        if "#" in b: CWD_DIR_FLAG = True

        if C_DRIVE_FLAG: 
            path = "C:/"
            name = str(b[1])
        
        if CWD_DIR_FLAG:
            path = "./"
            name = str(b[1])

        targets = []

        #print(" This is a painfully slow process!")

        try:
            for root, dirs, files in os.walk(path):
                if name in files or name in dirs:
                    targets.append(str(os.path.abspath(os.path.join(root, name))))
        except KeyboardInterrupt:
            return

        if len(targets) == 0:
            print(f" Found no files matching '{name}'")
            return
        
        print(targets)
        return True

CURRENT_GLOBAL_VARIABLES = [
    ("test", 250)
]

def VariableDef(a, b):
    if (b[0] == "%"):
        VARIABLE_NAME = b[1]
        VARIABLE_VALUE = b[2]

        if any(VARIABLE_NAME == item[0] for item in CURRENT_GLOBAL_VARIABLES):
            print(" Variable already exists!")
            return
        else:
            CURRENT_GLOBAL_VARIABLES.append([VARIABLE_NAME, VARIABLE_VALUE])
            print(" Made variable sucessfully.")
        return True

def SpewVariables(a, b):
    if (b[0] in ["globals", "vlist"]):
        print(CURRENT_GLOBAL_VARIABLES)
        
        return True

def ListMk(a, b):
    if (b[0] in ["listmk", "mklist"]):
        head = []

        if ("-h" in b):
            header_index = int(list(b).index("-h"))

            head.append(b[header_index + 1])
            head.append(b[header_index + 2])

        data = b[1:header_index]
        print(data)
        try:
            data = list(data)
        except:
            print(" Formatting error when making list!")
        
        print(tabulate(data, headers=head, tablefmt="grid"))

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
    hello,
    Hide,
    _Time,
    wifi,
    jsc,
    Random,
    Explorer,
    Open,
    ByteView,
    Window,
    MkShortcut,
    CloneURL,
    WebStat,
    FindFile,
    VariableDef,
    SpewVariables,
    Range,
    ListMk
]
