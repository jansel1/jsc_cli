from os import path
import time

SETTINGS_DAT =  """
{
    "Character": ">"
}
"""

def main():
    with open("./Settings.json", "w") as f:
        f.write(SETTINGS_DAT)

try:
    main()
    print("CHANGED SETTINGS.")
except:
    print("COULDNT REVERT SETTINGS.\nTRYING AGAIN.")

    while True:
        print("TRYING TO CHANGE SETTINGS.")
        try:
            main()
        except:
            print("COULDNT REVERT SETTINGS.\nTRYING AGAIN.")
time.sleep(2)
quit()