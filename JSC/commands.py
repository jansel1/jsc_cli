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
import win32com.client
import colorama.ansi
import requests
import pyperclip
import psutil
import platform
import sys
import tempfile
import re
import curses


from rich.console import Console
from tabulate import tabulate
from urllib.parse import urlparse
import urllib.request
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
DIRECTORY_HISTORY = [os.getcwd()]

def Marg():
    print(" Index error! Missing arguements or an internal error has ocurred.")

def match_split(Table, Keyword):
    for val in Table:
        if val == Keyword:
            return Table.index(val, 0, len(Table))

def DIS_V():
    print("  # JSC version: Alpha #")


LONG_PRINT_LOCATION = fr"{tempfile.gettempdir()}\JSC"

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

        print(f"{_out}") # print(f"{_out.replace(_char2, str(random.randint(rmin, rmax)))} ")

        return True
_line_data = []

def Clear(Input, _Input):
    EXCEPT_COMMANDS_FLAG = False
    if _Input[0] in ["cls", "clearscreen", "-"]:
        if "-ec" in _Input: EXCEPT_COMMANDS_FLAG = True

        time.sleep(0.1)
        os.system('cls')

        if (EXCEPT_COMMANDS_FLAG):
            for l in _line_data:
                print(l)

        return True
    
def LoopReturn(Input, _Input):
    out = ""

    if _Input[0] == "lcout":

        _out = f" {_Input[1]}"

        amt = 5
        try:
            amt = int(_Input[2])
        except:
            pass

        for i in range(amt + 1):
            out += f"{_out}\n"

        print(out)

        return True

def ReadFile(Input, _Input):
    try:
        if _Input[0] == "readf":
            ae =  False

            CLONE_FLAG = False

            if "-cc" in _Input: CLONE_FLAG = True

            FilePath = _Input[1]

            
            if os.path.exists(FilePath) == False:
                print(" File dosen't exist")
                ae = True

                return


            with open(FilePath, 'r+') as file:
                if not CLONE_FLAG:
                    print(f"{file.name}\n{file.read()}")
                    print(f"\n\nSize - {os.path.getsize(file.name)} bytes\tAbs. Path - {os.path.abspath(file.name)}")
                else:
                    pyperclip.copy(file.read())
                    print(" Copied text to clipboard.")

            return True 
    except Exception as e:
        if not ae:
            print(f" Missing file location arguement or could not find file or permission error\n{e}")
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
        external_ip = urllib.request.urlopen('https://ipinfo.io').read().decode('utf8')
        city = urllib.request.urlopen('https://ipinfo.io/city').read().decode('utf8')

        print(f" IP data:\n {external_ip}")
        print(f"Other:\n HOSTNAME: {dat_hn}\n PRIVATE: {dat_ip}")

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
            print(f" Made directory '{os.path.abspath(Directory)}'")

            if "-cd" in b: os.chdir(Directory)
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
        Desired = b[1]
        
        if Desired == "-":
            Desired = os.path.dirname(os.path.realpath(__file__))

        os.chdir(Desired)

        DIRECTORY_HISTORY.append(Desired)

        return True

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

        if "-h" in b:
            _h = True
            
            try:
                try:
                    hn = socket.gethostbyaddr(Socket_HN)
                except: print(" Could not get IP.")

                print(f" Host name: {hn[0]}")
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
            print(f" Found no files matching '{name}' in {path}")
            return
        
        print(targets)
        return True

D_INDEX = len(DIRECTORY_HISTORY)

CURRENT_GLOBAL_VARIABLES = [ # Comes preloaded with variables, such as Desktop location, etc
    ["cwd", str(os.getcwd()).replace("\\", "/")],
    ["desktop", str(os.path.normpath(os.path.expanduser("~/Desktop"))).replace("\\", "/")],
    ["temp", str(tempfile.gettempdir()).replace("\\", "/")],
    ["printable", PRINTABLE],
    ["user", str(os.path.normpath(os.path.expanduser("~/"))).replace("\\", "/")],
]

def VariableDef(a, b):                                  # gotta work on this shit
    if (b[0] == "%"):
        VARIABLE_NAME = b[1]
        VARIABLE_VALUE = b[2]

        if "-math" in b:
            try:
                VARIABLE_VALUE = eval(b[2])
            except:
                print(" Could not do math! Most likely a formatting error.")

        if any(VARIABLE_NAME == item[0] for item in CURRENT_GLOBAL_VARIABLES):
            print(" Variable already exists!")
            return
        else:
            CURRENT_GLOBAL_VARIABLES.append([VARIABLE_NAME, VARIABLE_VALUE])
            print(" Made variable sucessfully.")
        return True

def SpewVariables(a, b):
    if (b[0] in ["globals", "vlist"]):
        
        for var in CURRENT_GLOBAL_VARIABLES:
            print(f"{var[0]} = {var[1]}\n")
        
        return True

def ListMk(a, b):                                       # to be fixed
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

        return True

def NameDelta(a, b): # WIP! Fix: cannot remove directories
    IF_FIND_FLAG = False
    
    removed = []

    if b[0] == "deltn":
        if "-find" in b: IF_FIND_FLAG = True

        LOCATION = b[1]
        NAME = b[2]

        for root, dirs, files in os.walk(LOCATION):
            for _f in files:
                _f_path = os.path.join(root, _f)
                
                if IF_FIND_FLAG == False:
                    if _f == NAME:
                        os.remove(_f_path)
                        removed.append(f" Removed file {_f}")
                
                else: 
                    if NAME in _f:
                        os.remove(_f_path)
                        removed.append(f" Removed file {_f}")
            
            for _d in dirs:
                _d_path = os.path.join(root, _d)
                
                if IF_FIND_FLAG == False:
                    if _f == NAME:
                        os.remove(_d_path)
                        removed.append(f" Removed folder {_f}")
                
                else: 
                    if NAME in _f:
                        shutil.rmtree(_d_path)
                        removed.append(f" Removed folder {_f}")

        if not len(removed) == 0:
            out = f"All files deleted in {os.path.abspath(LOCATION)}"

            for file in removed:
                out += f"{file}\n"
        else:
            print(" Could not find files/folders to remove.")

def Process(a, b):
    if b[0] == "proc":
        processName = str(b[1])
        PROCLIST_FLAG = False

        if not processName.endswith(".exe") and not "-c" in b:
            processName += ".exe"

        if "-list" in b:
            PROCLIST_FLAG = True

        found = False
        PROCLIST_DONE = False

        proc_data = ""

        if (PROCLIST_FLAG):
            print(f" Collecting process data...")

        for pid in psutil.process_iter(['pid', 'name', 'cpu_percent', 'exe']):
            if (PROCLIST_FLAG) and not pid.info["name"] in ["", None]:

                proc = psutil.Process(pid.info['pid'])
                
                if not "-cud" in b:
                    if not proc.cpu_percent(interval=0.1) == 0:
                        cpu_usage_list = proc.cpu_percent(interval=5) / psutil.cpu_count()
                    else:
                        cpu_usage_list = "0"

                else:
                    cpu_usage_list = "(unable to get)"

                proc_data += f"{pid.info['name']:<60}: \t{cpu_usage_list}\n"

                PROCLIST_DONE = True
                found = True

            if pid.info["name"] == processName and not PROCLIST_FLAG:
                cpu_usage = "N/A"

                proc = psutil.Process(pid.info['pid'])

                if "-t" in b: # Terminate
                    proc.terminate()
                    print(" Ended process sucessfully.")

                    break
                if "-ft" in b: # Force Terminate
                    proc.kill()
                    print(" Terminated process sucessfully.")

                    break

                if not "-cud" in b: # Stands for CPU Usage Disabled
                    print("Getting CPU usage...\n")
                    cpu_usage = proc.cpu_percent(interval=5)

                print(f" Process is currently running.\n Process abs. path: {pid.info['exe']}")
                print(f" \nCPU Usage: {cpu_usage}%")
                found = True


                break

        if not found:
            print(" Could not find process")

        if (PROCLIST_DONE):
            now = datetime.datetime.now()
            formatted_time = now.strftime("%a, %H:%M:%S")

            print(f"Shows process data (taken on {formatted_time}), the number on the side is the CPU usage.\n\n{proc_data}")

        return True
    
def SysData(a, b):
    if b[0] in ["sysinfo", "sys"]:
        ram = psutil.virtual_memory()

        # Cpu
        print(f" CPU:\n\t Logical CPU's: {psutil.cpu_count()}\n\t CPU Frequency: {psutil.cpu_freq().current}MHz\n\t CPU Usage: {psutil.cpu_percent()}%")

        # Cpu Stats
        print(f"\n CPU Stats\n\t CTX Switches: {psutil.cpu_stats().ctx_switches} \n\t Soft Interrupts: {psutil.cpu_stats().soft_interrupts}\n\t Syscalls: {psutil.cpu_stats().syscalls}")

        # Ram
        print(f" Ram:\n\tTotal RAM: {ram.total / (1024 * 1024 * 1024):.2f} GB")
        print(f" \tAvailable RAM: {ram.available / (1024 * 1024 * 1024):.2f} GB")
        print(f" \tUsed RAM: {ram.used / (1024 * 1024 * 1024):.2f} GB")
        print(f" \tPercentage Used: {ram.percent}%")

        # OS
        os_info = platform.uname()

        print(f"\nOperating System:\n\tSystem: {os_info.system}")
        print(f"\tNode Name: {os_info.node}")
        print(f"\tRelease: {os_info.release}")
        print(f"\tVersion: {os_info.version}")
        print(f"\tMachine: {os_info.machine}")
        print(f"\tProcessor: {os_info.processor}")
        print(f"\tBoot Time: {psutil.boot_time()}")

def PythonUtils(a, b):
    if b[0] == "pyutil":
        flags = ""

        b[1] # This is so if it's missing, it will return a marg

        if "-dir" in b: flags += "--onedir"
        if "-sta" in b: flags += "--onefile"

        if "-exe" in b: # This shit sucks ass
            file_loc = os.path.abspath(b[1])

            try:
                os.system(f"pyinstaller {flags} {file_loc}")
            except:
                print(" Could not convert to EXE, check file location and check if PyInstaller is installed.")
        elif b[1] == "-version":
            print(f" JSC is running Python {sys.version}")
        else:
            print(f" Could not find argument '{b[1]}'")

        return True
    
def Path(a, b): # Shits suck
    if b[0] == "path" and b[1]:
        current_path = os.getenv('PATH', '')

        if "-list" in b:
            path_list = current_path.split(os.pathsep)

            for path in path_list:
                print(path)

            return
        
        if "-mk" in b:
            new_path = os.path.abspath(b[1])
            new_path_variable = f'{current_path}:{new_path}'

            os.environ['PATH'] = new_path_variable

            print(" Added directory to PATH (for this current session).")
            
        return True

def duplicate_remove_sort(filepath):
    amt = 0
    with open(filepath, 'r') as file:
        lines = file.readlines()
        amt = len(file.readlines())

    unique_lines = list(set(lines))

    with open(filepath, 'w') as file:
        file.writelines(unique_lines)

    print(" Removed duplicates")

def reverse_file_sort(filepath):
    with open(filepath, 'w+') as file:
        file.write(str(reversed(file.read())))
        print(" Reversed text")

def Fort(a, b): # Stands for FileSort
    if b[0] == "fort":
        if b[1] == "?":
            print()
            return
        
        FilePath = b[1]
        SortType = b[2]

        SORT_TYPES = [
            ["-dupes", duplicate_remove_sort],
            ["-reverse", reverse_file_sort]
        ]

        for sorts in SORT_TYPES:
            if SortType in sorts[0]:
                sorts[1](FilePath)

        return True

def ParseFile(fil):
    with open(fil, 'r') as file:
        lines = file.readlines()

    unique_lines = list(set(lines))
    out = [line for line in unique_lines if not re.fullmatch(r'\d+', line.strip())]

    with open(fil, 'w') as file:
        file.writelines(out)

def BrootMain(a, b):
    if b[0] in ["broot", "passlist"]:
        symbols = ".!?#-"

        Extratags = b[1].split(',')
        Amount = b[2]

        passwords = []

        passwords_2 = [] # All lowercase
        passwords_3 = [] # All upercase
        passwords_4 = [] # No symbols
        passwords_5 = [] # No numbers
        
        components = Extratags

        for tag in Extratags:
            passwords.append(tag)

        for _ in range(int(Amount)):
            password = ""
            num_parts = random.randint(1, 3)

            parts = random.sample(components, num_parts)

            for p in parts:
                password += p

            if random.choice([True, False]):
                password += str(random.randint(0, 1000))
            
            if random.choice([True, False]):
                if random.choice([True, False]):
                    password = random.choice(symbols) + password
                else:
                    password += random.choice(symbols)

            if password:
                index = random.randint(0, len(password) - 1)
                if password[index].isalpha():
                    password = password[:index] + password[index].upper() + password[index+1:]

            passwords.append(password)

        passwords_2 = [element.lower() for element in passwords]
        passwords_3 = [element.upper() for element in passwords]

        passwords_4 = [''.join(re.findall(r'\w', element)) for element in passwords]
        passwords_5 = [''.join(re.findall(r'[A-Za-z]', element)).upper() for element in passwords]


        print("Don't exit, we're storing the passwords to ./passwords.txt")

        with open("./passwords.txt", 'a') as f:
            for pwd in passwords: f.write(pwd + "\n")
            for pwd2 in passwords_2: f.write(pwd2 + "\n")
            for pwd3 in passwords_3: f.write(pwd3 + "\n")
            for pwd4 in passwords_4: f.write(pwd4 + "\n")
            for pwd5 in passwords_5: f.write(pwd5 + "\n")

        ParseFile("./passwords.txt")

        return True

def GeneralCommands(Input, _Input):
    if (_Input[0] == "xy"):
        try:
            X = int(_Input[1])
            Y = int(_Input[2])
        except: Marg()

        confirm = input(" This command will clear all the text! Y/n to proceed:")

        if (confirm.lower() == "y"):
            os.system(f'mode {X},{Y}')
        else:
            pass

        return True

    elif (_Input[0] == "whoami"): 
        print(f" {os.getlogin()} at {os.path.normpath(os.path.expanduser('~/'))}")
        return True

    elif (_Input[0]) == "ld": 
        os.system("dir")
        return True


    elif _Input[0] in ["qr", "restart", "r", "upt", "latest", "reset"]:
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        os.system("python jsc.py") 
        quit()

    elif _Input[0] in ["q", "quit", "bye", "!!", "close"]: quit()

def CUSTOM_COLOR(red, green, blue): return f'\033[38;2;{red};{green};{blue}m'

def Ls(a, b):
    if b[0] == "ls":
        files = os.listdir()


        out = ""

        for file in files:
            c = ""

            if not os.path.isfile(file):
                c = f"{colorama.Back.MAGENTA}"
                data = f"{'N/A':<15} {'N/A':<20}"
            else:
                file_size = os.path.getsize(file)

                last_modif = os.path.getmtime(file)
                last_modif_str = datetime.datetime.fromtimestamp(last_modif).strftime('%Y-%m-%d %H:%M:%S')

                data = f"{file_size:<15} {last_modif_str:<20}"

            out += f"{c}{file:<40} {colorama.Back.RESET}{colorama.Fore.RESET} {data}\n"


        print(out)

        return True


def curl(cmd): os.system(f"curl {cmd}")

def Curls(a, b):
    if b[0] == "weather": 
        city = urllib.request.urlopen('https://ipinfo.io/city').read().decode('utf8')
        if {b[1]}: city = b[1]

        url = f"https://wttr.in/{city}"

        response = requests.get(url)

        if response.status_code == 200:
            weather_info = response.text
            print(weather_info)
        else:
            print("Failed to retrieve weather information.")

        return True

    if b[0] == "unwrap":
        url = b[1]
        curl(f"--head --location \"{url}\" | findstr Location")

        return True

    if b[0] == "qrcode":
        website = b[1]
        curl(f"https://qrenco.de/https://{website}")

        return True

def WriteFile(a, b):
    if b[0] == "writef":
        def main(stdscr): # made by https://github.com/maksimKorzh/ (thanks)
            file_path = b[1]
            screen = curses.initscr()
            screen.nodelay(1)
            curses.noecho()
            curses.raw()
            screen.keypad(1)
            
            buffer = []
            max_rows, max_cols = screen.getmaxyx()
            view_x, view_y, cursor_row, cursor_col = [0] * 4

            try:
                with open(file_path) as file:
                    content = file.read().split('\n')
                    content = content[:-1] if len(content) > 1 else content
                    for row in content:
                        buffer.append([ord(char) for char in row])
            except:
                buffer.append([])

            while True:
                screen.move(0, 0)
                if cursor_row < view_y:
                    view_y = cursor_row
                if cursor_row >= view_y + max_rows:
                    view_y = cursor_row - max_rows + 1
                if cursor_col < view_x:
                    view_x = cursor_col
                if cursor_col >= view_x + max_cols:
                    view_x = cursor_col - max_cols + 1

                for row in range(max_rows):
                    buffer_row = row + view_y
                    for col in range(max_cols):
                        buffer_col = col + view_x
                        try:
                            screen.addch(row, col, buffer[buffer_row][buffer_col])
                        except:
                            pass
                    screen.clrtoeol()
                    try:
                        screen.addch('\n')
                    except:
                        pass

                curses.curs_set(0)
                screen.move(cursor_row - view_y, cursor_col - view_x)
                curses.curs_set(1)
                screen.refresh()
                char_input = -1

                while char_input == -1:
                    char_input = screen.getch()

                if char_input != (char_input & 0x1f) and char_input < 128:
                    buffer[cursor_row].insert(cursor_col, char_input)
                    cursor_col += 1
                elif chr(char_input) in '\n\r':
                    remainder = buffer[cursor_row][cursor_col:]
                    buffer[cursor_row] = buffer[cursor_row][:cursor_col]
                    cursor_row += 1
                    cursor_col = 0
                    buffer.insert(cursor_row, [] + remainder)
                elif char_input in [8, 263]:
                    if cursor_col:
                        cursor_col -= 1
                        del buffer[cursor_row][cursor_col]
                    elif cursor_row:
                        remainder = buffer[cursor_row][cursor_col:]
                        del buffer[cursor_row]
                        cursor_row -= 1
                        cursor_col = len(buffer[cursor_row])
                        buffer[cursor_row] += remainder
                elif char_input == curses.KEY_LEFT:
                    if cursor_col != 0:
                        cursor_col -= 1
                    elif cursor_row > 0:
                        cursor_row -= 1
                        cursor_col = len(buffer[cursor_row])
                elif char_input == curses.KEY_RIGHT:
                    if cursor_col < len(buffer[cursor_row]):
                        cursor_col += 1
                    elif cursor_row < len(buffer) - 1:
                        cursor_row += 1
                        cursor_col = 0
                elif char_input == curses.KEY_UP and cursor_row != 0:
                    cursor_row -= 1
                elif char_input == curses.KEY_DOWN and cursor_row < len(buffer) - 1:
                    cursor_row += 1

                current_row = buffer[cursor_row] if cursor_row < len(buffer) else None
                current_row_length = len(current_row) if current_row is not None else 0
                if cursor_col > current_row_length:
                    cursor_col = current_row_length

                if char_input == (ord('q') & 0x1f):
                    try:
                        os.system(f"{__file__}")
                    except: os.system(f"python {__file__}")

                    sys.exit()
                elif char_input == (ord('s') & 0x1f):
                    content = ''
                    for line in buffer:
                        content += ''.join([chr(char) for char in line]) + '\n'
                    with open(file_path, 'w') as file:
                        file.write(content)

        curses.wrapper(main)

        return True
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
    MkShortcut,
    CloneURL,
    WebStat,
    FindFile,
    VariableDef,
    SpewVariables,
    Range,
    ListMk,
    Process,
    SysData,
    PythonUtils,
    Path,
    NameDelta,
    Fort,
    BrootMain,
    GeneralCommands,
    Ls,
    Curls,
    WriteFile
]
