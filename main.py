#update 'ver' command
print("eopDOS v0.2")
print("Starting...")
import time
from random import *
import sys
init_time = randint(1,3)
time.sleep(init_time)
files_U = 0
notepad_fileNum = 1
statement_placer = 0
notepad_files = []
dir0 = r"C:\Local User>"
sys_serial = randint(1000,9999)
def print_dir_user_():
    time.sleep(0.1)
    print("Volume in drive C has no label")
    print("Volume Serial Number is 8J12-UNDE")
    print(" Name      Size")
    print("Documents ", (1002+((notepad_fileNum) * 58)))
    print("Files:", (files_U))
    print("Dirs: 1")
    print("Cannot find space of 'virtualdrive8j12unde'")
    print("")
def print_dir_drive():
    time.sleep(0.1)
    print("Volume in drive C has no label")
    print("Volume Serial Number is 8J12-UNDE")
    print(" Name                 Size")
    print("eopDOS_v0.2.py    20,480B")
    print("Apps                 2,020B")
    print("Users ", (1010+((notepad_fileNum) * 58)))
    print("Files: 1")
    print("Dirs: 2")
    print("Cannot find space of 'virtualdrive8j12unde'")
    print("")
def chkdsk_r():
    time.sleep(0.1)
    print("Starting read test...")
    time.sleep(1.8)
    print("Checking for bad sectors...")
    time.sleep(0.9)
    print("Checking for formatting errors...")
    time.sleep(1.2)
    print("Checking for registry errors...")
    time.sleep(0.5)
    print("Verifying Usn Journal...")
    time.sleep(0.1)
    print("SystemError: Usn Journal for 'virtualdrive8j12unde' does not exist")
    time.sleep(0.1)
    print("No physical errors found within disk.")
    print("Cleaning up...")
    time.sleep(0.8)
    print("")
def chkdsk_noParam():
    time.sleep(0.1)
    print("Parameters not specified.")
    print("Running general disk scan...")
    time.sleep(8)
    print("Verifying Usn Journal...")
    time.sleep(0.1)
    print("SystemError: Usn Journal for 'virtualdrive8j12unde' does not exist")
    print("Cleaning up...")
    time.sleep(0.8)
    print("")
def chkdsk_f():
    time.sleep(0.1)
    print("Checking for formatting errors...")
    time.sleep(1)
    print("Checking for registry errors...")
    time.sleep(0.9)
    print("No errors found.")
    time.sleep(0.2)
    print("Cleaning up...")
    time.sleep(0.8)
    print("")
print("Type credits or help for more information.")
print("")
while True:
    cmd = input(dir0)
    if cmd == '':
        statement_placer = 0
    elif cmd == 'exit':
        exit()
    elif cmd == 'dir':
        if dir0 == r"C:\Local User>":
            print_dir_user_()
        elif dir0 == r"C:\>":
            print_dir_drive()
        elif dir0 == '':
            print_dir_user_()
        else:
            print("System Error: Cannot find directory", (dir0))
    elif cmd == 'cls':
        cls_error = randint(1,2)
        if cls_error == 1:
            print("System Error: Unable to clear terminal")
            print("")
        else:
            print("System Error: file cmd_clear.dll failed to load")
            print("")
    elif cmd == 'ver':
        print("v0.2")
        print("Checking for updates...")
        time.sleep(0.8)
        print("No updates avaliable.")
        print("Last updated 5/3/2020")
        print("")
    elif cmd == 'credits':
        print("All work done by eyx")
        print("")
    elif cmd == 'hostname':
        print("eopMachine", (sys_serial), sep="-")
        print("")
    elif cmd == 'notepad':
        notepad_prompt = input("New file(n), Load file(l) or Delete all(d): ")
        if notepad_prompt == 'n':
            print("new", (notepad_fileNum))
            print("")
            new_file = input("")
            print("")
            notepad_files.append(new_file)
            notepad_fileNum += 1
        elif notepad_prompt == 'l':
            load_note = input("Type the filename of the note: ")
            if load_note[0:3] == 'new':
                try:
                    load_file_num = int(load_note[4:])
                    print(notepad_files[(int(load_file_num))-1])
                    print("")
                except IndexError:
                    print("Cannot find file.")
                    print("")
            else:
                print("Cannot find file.")
                print("")
        elif notepad_prompt == 'd':
            check_delAll = input("Are you sure you want to delete all of your files (Y/N)? ")
            if check_delAll == 'y':
                notepad_files.clear()
                print("Deleting...")
                time.sleep(0.2*(notepad_fileNum))
                notepad_fileNum = 1
                print("")
            elif check_delAll == 'n':
                print("")
            else:
                print("")
    elif cmd[0:2] == 'cd':
        cdTo = cmd[3:]
        if cdTo == '..':
            dir0 = r"C:\>"
            print("")
        elif cdTo == 'Local User':
            dir0 = r"C:\Local User>"
            print("")
        else:
            print("The system cannot find the path specified.")
            print("")
    elif cmd[0:4] == 'echo':
        echo = cmd[5:]
        if echo == 'off':
            dir0 = ''
        elif echo == 'on':
            dir0 = r"C:\Local User>"
        else:
            print(echo)
            print("")
    elif cmd == 'cmd':
        print("")
        print("eopDOS v0.2")
        print("Type credits or help for more information.")
        print("")
    elif cmd[0:6] == 'chkdsk':
        if cmd[7:] == '':
            chkdsk_noParam()
        elif cmd[7:] == '/r':
            chkdsk_r()
        elif cmd[7:] == '/f':
            chkdsk_f()
    elif cmd == 'help':
        print("To start a program, type in the application name.")
        print("dir: print directory")
        print("chkdsk /f /r: checks disk for errors")
        print("cd: change directory")
        print("echo: change output string")
        print("cls: clear terminal")
        print("hostname: print system name")
        print("ver: print version")
        print("exit: exit shell")
        print("")
    else:
        print((cmd), "is not recognized as an internal or")
        print("external command, operable program or batch file.")
        print("")
        
