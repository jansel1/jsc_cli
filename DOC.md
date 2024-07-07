# JSC Pre-Release Beta Alpha v1.1.2 : 46 Commands (PBA1.1.2:46)

# Command Documentation

## General Commands:

### Return
- **Syntax:** `cout <string>`
- **Description:** Prints the given string.

### Clear
- **Syntax:** `cls`, `clearscreen`, `-`
- **Description:** Clears the console screen.

### LoopReturn
- **Syntax:** `lcout <string> <amount>`
- **Description:** Prints the given string multiple times, specified by `<amount>`.

### RestartJSC
- **Syntax** `qr`, `restart`, `r`, `upt`, `latest`, `reset`
- **Description:** Restarts JSC

### QuitJSC
- **Syntax** `q`, `quit`, `bye`, `!!`, `close`
- **Description:** Quits JSC

### QuitAfter Flag
- **Syntax** `<any command> <-$q>`
- **Description:** Quits JSC after the command/task executed finishes.

### whoami
- **Syntax** `whoami`
- **Description:** Prints the user's name

### Current Directory
- **Syntax** `#`
- **Description:** Prints current directory

### ReadFile
- **Syntax:** `readf <file path> [-cc]`
- **Description:** Reads and displays the contents of the specified file.
  - `-cc`: Copies the file contents to clipboard.

### Delta
- **Syntax:** `delta`, `del <file or directory path>`
- **Description:** Deletes the specified file or directory.

### Namef
- **Syntax:** `namef <file path> <new name>`
- **Description:** Renames the specified file to the new name.

### Cf
- **Syntax:** `cf <file name>`
- **Description:** Creates a new file with the given name.

### Stiff
- **Syntax:** `stf`, `stiff`, `td <source file> <destination file>`
- **Description:** Transfers contents from the source file to the destination file.

### Url
- **Syntax:** `http`, `url <link>`
- **Description:** Opens the specified URL in a web browser.

### Save
- **Syntax:** `save`, `sv <file path>`
- **Description:** Creates a save file for the specified file.

### Ip
- **Syntax:** `ip [-L <location>]`
- **Description:** Displays the hostname and IP address.
  - `-L`: Saves the IP address to the specified location.

### Bomb
- **Syntax:** `bomb <directory> <amount>`
- **Description:** Creates multiple files in the specified directory.

### Reg
- **Syntax:** `reg <command>`
- **Description:** Executes the specified command and prints the output.

### Blank
- **Syntax:** `blk <directory>`
- **Description:** Blanks out all files in the specified directory.

### Corrupt
- **Syntax:** `cor <file path>`
- **Description:** Corrupts the specified file.

### C
- **Syntax:** `c`, `cff <directory>`
- **Description:** Creates a new directory.

### Pearl
- **Syntax:** `pearl`, `prl`, `cln`, `clean`, `powerwash`, `purge <directory>`
- **Description:** Cleans up the specified directory by removing empty files and directories.

### Dir
- **Syntax:** `dir`, `cd <directory>`
- **Description:** Changes the working directory to the specified directory.

### Run
- **Syntax:** `run.py <file path>`, `run.t <file path>`
- **Description:** Executes the specified Python file or script.

### SocketInfo
- **Syntax:** `ski <hostname or ip adress> [-h]`
- **Description:** Displays the IP address or hostname.
  - `-h`: Displays the hostname (argument must be valid IP adress).

### working
- **Syntax:** `working`, `test`
- **Description:** Runs a test loop for a random number of iterations.

### hello
- **Syntax:** `/hi`
- **Description:** Prints "Halloes!"

### Hide
- **Syntax:** `hif <file path>`, `hif /u <file path>`
- **Description:** Hides or unhides the specified file.

### _Time
- **Syntax:** `time`, `t`
- **Description:** Displays the current date and time.

### wifi
- **Syntax:** `wif`
- **Description:** Displays WiFi profiles.

### jsc
- **Syntax:** `jsc`
- **Description:** Opens the JanSel Command (JSC) web page.

### Random
- **Syntax:** `randint <min> <max>`, `randstr [characters]`
- **Description:** Generates a random integer between min and max or a random string from the given characters.

### Explorer
- **Syntax:** `explorer.exe`, `explorer`, `exp`, `exp.exe`
- **Description:** Opens File Explorer.

### Open
- **Syntax:** `$<program>`
- **Description:** Opens the specified program.

### ByteView
- **Syntax:** `readb <file path>`
- **Description:** Reads and displays the byte data of the specified file.

### MkShortcut
- **Syntax:** `ms`, `mks`, `short`, `portal`, `witch <location> <destination> <name>`
- **Description:** Creates a shortcut to the specified location.

### CloneURL
- **Syntax:** `wclone`, `corl`, `webclone <url> [-cc]`
- **Description:** Clones the specified webpage to a file or clipboard.
  - `-cc`: Copies the HTML content to clipboard.

### WebStat
- **Syntax:** `webstat`, `webs`, `reqstat <url> [-ping] [-pingfr]`
- **Description:** Checks the status of the specified URL.
  - `-ping`: Pings the URL.
  - `-pingfr`: Pings the URL continuously.

### FindFile
- **Syntax:** `syscan`, `dscan <path> <name> [-c] [#]`
- **Description:** Searches for the specified file or directory.
  - `-c`: Scans the C drive.
  - `#`: Scans the current working directory.

### VariableDef
- **Syntax:** `% <variable name> <value> [-math]`
- **Description:** Defines a global variable with the specified name and value.
  - `-math`: Evaluates the value as a mathematical expression.

### SpewVariables
- **Syntax:** `globals`, `vlist`
- **Description:** Lists all global variables.

### Range
- **Syntax:** `range <min> <max>`
- **Description:** Sets the random range for generating random numbers.

### ListMk
- **Syntax:** `listmk`, `mklist <data> [-h <header1> <header2>]`
- **Description:** Creates a table from the given data.
  - `-h`: Adds headers to the table.

### Process
- **Syntax:** `proc <process name> [-list] [-t] [-ft] [-cud]`
- **Description:** Manages processes.
  - `-list`: Lists all processes.
  - `-t`: Terminates the process.
  - `-ft`: Force terminates the process.
  - `-cud`: Disables CPU usage display.

### SysData
- **Syntax:** `sysinfo`, `sys`
- **Description:** Displays system information including CPU, RAM, and OS details.

### PythonUtils
- **Syntax:** `pyutil <file> [-dir] [-sta] [-exe]`, `pyutil -version`
- **Description:** Utility commands for Python files.
  - `-dir`: Uses one directory mode.
  - `-sta`: Uses one file mode.
  - `-exe`: Converts the Python file to an executable.
  - `-version`: Displays the Python version.

### Path
- **Syntax:** `path <directory> [-list] [-mk]`
- **Description:** Manages the PATH environment variable.
  - `-list`: Lists all directories in the PATH.
  - `-mk`: Adds a directory to the PATH.

### NameDelta
- **Syntax:** `deltn <location> <name> [-find]`
- **Description:** Deletes files or directories with the specified name.
  - `-find`: Deletes files or directories that contain the specified name.

### Fort
- **Syntax:** `fort <file path> <sort type>`
- **Description:** Sorts the contents of the specified file.
  - `-dupes`: Removes duplicate lines.
  - `-reverse`: Reverses the file content.

### BrootMain
- **Syntax:** `broot`, `passlist <tags> <amount>`
- **Description:** Generates a password list based on the specified tags and amount.

## Important!
If your string has a space in it, like "hey world", REMEMBER TO USE QOUTATION MARKS AROUND IT! Or else it will error out. Also, qoutation marks inside outher qoutation marks are broken!

ALSO, SOME COMMANDS WILL OUTPUT TO NOTEPAD.EXE (OR YOUR DEFAULT NOTEPAD) BECAUSE THE FUCKING TERMINAL SUCKS ASS! THIS MIGHT BE FIXED SOON I HOPE!

## Note to developers

(docs on how to make commands coming)

# Variables

To make a variable you must do `% <variable name> <variable value>`, and to use a variable you do `%<variable name>` (without the '<>' things ofcourse), DIFFERNCE IS: to use the variable, the '%' and the variable name are not seperated!

You can use that variable anywhere, such as `cout %myVariable`, and it will return whatever value you stored. 

# More
This was generated by ChatGPT, since it's hard to document all commands. Some commands might now work, so please report them to me! 