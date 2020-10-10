import os
import sys

def info(message):
    sys.stdout.write('\x1b[1;34mINFO\x1b[0m ' + message + "\n")

def tip(message):
    sys.stdout.write('\x1b[1;33mTIP\x1b[0m ' + message + "\n")

def main():    
    clone_firefox()
    clone_dot()

    print("\n")
    info("You are now ready to build Dot Browser!\n")

    info("Building the application can be done via the './build.sh' script.")
    info("Make sure you sync before you build with the './sync.sh' script.\n")

    tip("For more information and help on building, check out the build workflow document.")

def clone_firefox():
    os.system("git clone https://github.com/dothq/ffr -b master firefox")

def clone_dot():
    os.system("git clone https://github.com/dothq/browser dot")

if __name__ == "__main__":
    main()