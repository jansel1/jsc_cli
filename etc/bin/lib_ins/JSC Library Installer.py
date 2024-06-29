import subprocess
import sys

libraries_to_install = [
    "colorama",
    "pywin32",
    "requests",
    "pyperclip",
    "tabulate",
    "beautifulsoup4"
]

print(f"Installing libraries: {libraries_to_install}")
for lib in libraries_to_install:
    subprocess.check_call([sys.executable, "-m", "pip", "install", lib])
    print(f"Installing {lib}")