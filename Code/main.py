import os
from os import system as sys
import tkinter as tk
from tkinter.filedialog import askdirectory

def checkSave():
    files = os.listdir(os.getcwd())
    desc = False if "save.txt" not in files else True
    if desc: 
        file=open("save.txt", "r")
        currSave = file.readline()
        file.close()
        return currSave
    return False

def askDir():
    root=tk.Tk()
    root.withdraw()
    dirname=askdirectory(parent=root, title="Select Folder")
    root.destroy()
    return dirname

def getHelp():
    print("List of all available commands: ")
    print("\t\"rename\" \t\"r\" \tPrompts for a dir to rename with sequence of digits")
    print("\t\"setting\" \t\"s\" \tProvides Setting for path*")
    print("\t\"help\" \t\t\"h\" \tDisplays help menu")
    print("\t\"quit\" \t\t\"q\" \tQuits the program")
    menu()


def setter():
    print("CAUTION: Any changes to this will create a save file, which will be revoked. Any changes to it will damage the save. Enter the setting ID (number) to alter or type \"clear\" to reset it to default, else press \"q\" to quit settings.\n")
    files = os.listdir(os.getcwd())
    currSave = "Always Ask" if "save.txt" not in files else "Logged"
    if currSave=="Always Ask": print(f"\t1. Current Save: {currSave}")
    else:
        file=open("save.txt", "r")
        currSave = file.readline()
        file.close()
        print(f"\t1. Current Save: {currSave}")
    while True:
        cmd=str(input("\n[SETTING]>>> ")).lower()
        if cmd=="1":
            newPath=str(input("\n[SETTING][NEWPATH]>>> "))
            if newPath!="clear":
                if os.path.exists(newPath):
                    file=open("save.txt", "w")
                    currSave = file.write(f"{newPath}")
                    file.close()
                else: print("Invalid Path")
            elif newPath=="clear":
                sys("del save.txt")
                print("Current Save Resetted to Default : Always Ask")
        elif cmd=="q" or cmd=="quit": menu()
        else: print("Invalid Command"); continue


def ren():
    i=1
    path=checkSave()
    if path==False:
        path = str(askDir())
        if path=='': print("Process Cancelled"); menu()
    cd = f"cd {path}"
    files = os.listdir(path)
    try:
        for fn in files:
            ext=fn.split(".")[-1]
            cmd=(f"{cd} && ren \"{fn}\" \"{str(i).zfill(2)}.{ext}\"")
            print(cmd)
            sys(cmd)
            i+=1
        print("Successfully Renamed")
    except FileNotFoundError: print("Save has been broken.")
    menu()

def menu():
    cmd = str(input("\n>>> ")).lower()
    if cmd=="help" or cmd=="h": getHelp()
    elif cmd=="quit" or cmd=="q": quit()
    elif cmd=="rename" or cmd=="r": ren()
    elif cmd=="setting" or cmd=="s": setter()
    else: print("Invalid Command"); menu()

if __name__ == '__main__':
    print(r"""
__________                                   
\______   \ ____   ____   ____   ___________ 
 |       _// __ \ /    \ /    \_/ __ \_  __ \
 |    |   \  ___/|   |  \   |  \  ___/|  | \/
 |____|_  /\___  >___|  /___|  /\___  >__|   
        \/     \/     \/     \/     \/       
""")
    print("\t\t\t-Built and Developed by Arun")
    print("\n\n\nType \"help\" or \"h\" for more information.")
    menu()
