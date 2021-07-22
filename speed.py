#!/usr/bin/python3
# This Code Write by Mr.nope
# Speed-Test 1.2

import os
import time
import sys
import platform
try:
    import speedtest
    run = speedtest.Speedtest()
except ImportError:
    os.system("pip install speedtest-cli")
try:
    from colorama import Fore,init
    init()
except ImportError:
    os.system("pip install colorama")

system = platform.uname()[0]
cls_Err = "This Programm run on Linux, Windows, MacOS\n"
End = '\033[0m'
banner = Fore.LIGHTGREEN_EX + """
  _________                           .___    ___________                __    
 /   _____/______    ____   ____    __| _/    \__    ___/____    _______/  |_  
 \_____  \ \____ \ _/ __ \_/ __ \  / __ |       |    | _/ __ \  /  ___/\   __\  """ + Fore.RED + "Version: " + Fore.YELLOW + "1.2" + Fore.LIGHTGREEN_EX + """
 /        \|  |_> >\  ___/\  ___/ / /_/ |       |    | \  ___/  \___ \  |  |   
/_______  /|   __/  \___  >\___  >\____ |       |____|  \___  >/____  > |__|   
        \/ |__|         \/     \/      \/                   \/      \/         
                                                             """ + End

def title():
    if system == 'Windows':
        os.system("title Speed-Test")
    elif system  == 'Linux':
        os.system("printf '\033]2;Speed-Test\a'")
    else:
        print(cls_Err)
        sys.exit()
def cls():
    if system == 'Windows':
        os.system("cls")
    elif system == 'Linux':
        os.system("clear")
    else:
        print(cls_Err)
        sys.exit()
def ext():
    cls()
    print(Fore.GREEN + "Exiting..." + End)
    sys.exit()
def main():
    title()
    cls()
    print(banner)
    start()
def start():
    time.sleep(0.25)
    try_s = input("\nDo you want to start Speed Test? [y/n] ")
    if try_s == 'y':
        down_check = run.download()
        upload_check = run.upload()
        print(f"\nDownload: {down_check}")
        print(f"Upload: {upload_check}\n")
        try2()
    elif try_s == 'n':
        try1()
    else:
        start()
def try1():
    try_to_ext = input("\npress Enter...")
    if try_to_ext == '':
        ext()
    else:
        ext()
def try2():
    try_again = input("\nDo you want to try again? [y/n] ")
    if try_again == 'y':
        start()
    elif try_again =='n':
        try1()
    else:
        try2()
if __name__ == '__main__':
    try:
        try:
            main()
        except EOFError:
            print("\nCtrl + D")
            print("\nExiting...")
            sys.exit()
    except KeyboardInterrupt:
        print("\nCtrl + C")
        print("\nExiting...")
        sys.exit()