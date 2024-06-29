# Core

JSC (JanSel Command) is by no means a programming language - yes, it does include loops, variables, printing, etc. but this was made to be a replica of the Windows Command Prompt. The core-core comes down to the Command Prompt. JSC is just a (wrapper?) for it - meaning it dosen't use any UI libraries, just cmd.exe. I did that for simplicity, and for a light-weight release binary. Another thing to clear up is that, yes, this is very slow (since written in Python3.11). JSC was never intended to be fast, because if it was, I would've written it in C++. It's made to be simple for developers who want to re-make it (and also the amount of libraries Python has).

# Basics

## This talks about how JSC processes commands

To get the command, like "wclone", etc. we use Pythons built-in function: ```input()```. It gets the users input, then does some things with shlex. Why shlex? Because for example, if I want to do this ``` cout Hello world ```, it will just print "hello", but shlex makes it so you can add qoutes: ``` cout "Hello world" ```, and the output would be "Hello world".

Okay, moving on from Shlex, let me provide you a simple function template:
```
def DoSomething(a, b):
    if b[0] == "myCmd":
        ...
``` 
(you must add this function to the CommandList array in commands.py)

So 'jsc.py' (lets call the compiler) sends 2 variables to each function in CommandList, NormalInput (a), and SplitInput (b). The difference between them is that NormalInput is the full input, so ``` cout "I love C" ```, but the SlitInput is ``` ["cout", "I love C"]```, an array. So our little function ```DoSomething``` checks if the first Input (b[0]) ("cout") matches its desired input/command name, "myCmd". If not, it will just skip.

NormalInput can be used for other things too.
Also, to make flags, just do ``` if "myFlagName" in b: (run code) ```. This is a tip for the users, if using flags, please put them at the end or else your code will mess up.

## How JSC processes variables and math

Variables are made by doing ``` % myVar 1500 ```, which stores it to an array called CURRENT_GLOBAL_VARIABLES. You can do math inside this, by doing ``` % myMath "1500+1500" -math```, which will store the output as its value. To do math with other variables, just do ``` %myMath "%x + %y" -math ```, and the output will be stored as the value.

Now, how this all works comes down to ```eval()``` as of now. Which is unsafe, because people can directly execute Python code in it. I won't talk to much about this because why would I?

# Syntax

The syntax is following:
```
    % Variable <n> <flags...>       After "%", leave a space and type your variable name, then, put your string, float, int, etc. into <n>, preferrably with qoutation marks. Flags are: 
        *-math (for math operations)
    
    %Variable   Basically a placeholder for a variable, so you can use it anywhere and it will be replaced with your variable value.

    WIP!
```