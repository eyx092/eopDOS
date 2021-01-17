print()
print("""                   ____   ___  ____  
   ___  ___  _ __ |  _ \ / _ \/ ___| 
  / _ \/ _ \| '_ \| | | | | | \___ \ 
 |  __/ (_) | |_) | |_| | |_| |___) |
  \___|\___/| .__/|____/ \___/|____/ 
            |_|                      
""")
print()
import time
from random import *
import sys

def loading_bar(char, n, start_msg,end_msg):
    print((start_msg), end="")
    print("|", end="")
    for i in range(n):
        print((char), end="")
        time.sleep(randint(0,1))
    print("|")
    print(end_msg)
loading_bar("\u2593",15,"Starting: ","OS has been successfully loaded.")
init_time = randint(1,3)
time.sleep(init_time)
files_U = 0
notepad_fileNum = 1
statement_placer = 0
notepad_files = []
verify_file = False
disk_label = 'no-label'
dir0 = r"C:\Local User>"
sys_serial = randint(1000,9999)
string_sys_serial = str(sys_serial)
file_serial = open("serialNumber.txt", "w")
file_serial.write((string_sys_serial))
file_serial.close()
def print_dir_user_():
    time.sleep(0.1)
    if disk_label == 'no-label':
        print("Volume in drive C has no label")
    else:
        print("Volume in drive C is", (disk_label))
    print("Volume Serial Number is 8J12-UNDE")
    print(" Name                 Size")
    print("Documents             ", (1002+((notepad_fileNum) * 58)),"B",sep="")
    print("Files:", (files_U))
    print("Dirs: 1")
    print("Error 1101: Cannot find space of 'virtualdrive8j12unde'")
    print("")
def print_dir_drive():
    time.sleep(0.1)
    if disk_label == 'no-label':
        print("Volume in drive C has no label")
    else:
        print("Volume in drive C is", (disk_label))
    print("Volume Serial Number is 8J12-UNDE")
    print(" Name                 Size")
    print("eopDOS_v0.4.py        20,480B")
    print("Apps                  2,020B")
    print("Users                 ", (1010+((notepad_fileNum) * 58)),"B",sep="")
    print("Files: 1")
    print("Dirs: 2")
    print("Error 1101: Cannot find space of 'virtualdrive8j12unde'")
    print("")







#FLOPPY DISK SYSTEM
def floppyDriveSystem():
    print("eopDrive System v1.0a")
    print("Type 'exit' to exit.")
    while True:
        floppy_in = input("FLOPPYDRIVE>")
        if floppy_in == 'calculator':
            exec(open('calculator.py').read())
            print()
        elif floppy_in == 'pymark':
            exec(open('pymark.py').read())
        elif floppy_in == 'diskutil':
            exec(open('diskutil.py').read())
        elif floppy_in == 'help':
            print("Type in a program name to insert a disk.")
            print("Type 'exit' to exit.")
            print()
        elif floppy_in == 'info':
            print("eopVFloppyDrive-M01")
            print()
        elif floppy_in == 'exit':
            print()
            break
        else:
            print("!Drive Error 1110")
            print()










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
    print("Drive Error 1101: Usn Journal for 'virtualdrive8j12unde' does not exist")
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
    print("Drive Error 1101: Usn Journal for 'virtualdrive8j12unde' does not exist")
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

def cls():
    for i in range(0,100):
        print()
    
if statement_placer == 0:
    try:
        print("Checking key...")
        time.sleep(1)
        file = open("eopDOS-key.txt", "r")
        fileRead = (file.read())
        if fileRead == '5k8r!2T@J90(7{]ad&31f1adD1%&*^&s!Qa,c.L':
            print("Correct key.")
            print("Continuing startup...")
            time.sleep(1)
        else:
            print("Incorrect key.")
            print("Startup aborted.")
            time.sleep(4)
            exit()
    except FileNotFoundError:
        print("Could not find startup key.")
        print("Startup aborted.")
        time.sleep(4)
        exit()
cls()
print("eopDOS v0.4 on", (sys.platform))
print("""Type "help", "credits", or "license" for more information.""")
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
        elif dir0 == r"A:\>":
            print()
            floppyDriveSystem()
        else:
            print("System Error: Cannot find directory", (dir0))
    elif cmd == 'cls':
       cls()
    elif cmd == 'ver':
        print("v0.4")
        print("Checking for updates...")
        time.sleep(0.8)
        print("No updates avaliable.")
        print("Last updated 09/17/2020")
        print("")
    elif cmd == 'credits':
        print("All work done by eyx")
        print("")
    elif cmd == 'license':
        print("MIT License")
        print("")
        print("Copyright (c) 2020 eyx")
        print("")
        print("Permission is herby granted, free of charge, to any person obtaining a copy")
        print("""of this software and associated documentation files (the "Software"), to deal""")
        print("in the Software without restriction, including without limitation the rights")
        print("to use, copy, modify, merge, publish, distribute, sublicense, and/or sell")
        print("copies of the Software, and to permit persons to whom the Software is")
        print("furnished to do so, subject to the following conditions:")
        print("")
        print("The above copyright notice and this permission notice shall be included in all")
        print("copies or substantial portions of the Software.")
        print("")
        print("""THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR""")
        print("IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,")
        print("FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE")
        print("AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER")
        print("LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,")
        print("OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE")
        print("SOFTWARE.")
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
            if verify_file == True:
                print("Verifying file save to drive C...")
                time.sleep(1)
                print()
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
        elif cdTo == 'A':
            if dir0 == r"C:\>" or dir0 == r"A:\>":
                dir0 = r"A:\>"
                print()
            else:
                print("The system cannot find the path specified.")
                print()
        elif cdTo == 'C':
            if dir0 == r"C:\>" or dir0 == r"A:\>":
                dir0 = r"C:\>"
                print()
            else:
                print("The system cannot find the path specified.")
                print()
        elif cdTo == '':
            print(dir0)
            print("")
        else:
            print("The system cannot find the path specified.")
            print("")
    elif cmd[0:5] == 'chdir':
        cdTo = cmd[6:]
        if cdTo == '..':
            dir0 = r"C:\>"
            print("")
        elif cdTo == 'Local User':
            dir0 = r"C:\Local User>"
            print("")
        elif cdTo == 'A':
            if dir0 == r"C:\>" or dir0 == r"A:\>":
                dir0 = r"A:\>"
                print()
            else:
                print("The system cannot find the path specified.")
                print()
        elif cdTo == 'C':
            if dir0 == r"C:\>" or dir0 == r"A:\>":
                dir0 = r"C:\>"
            else:
                print("The system cannot find the path specified.")
            print()
        elif cdTo == '':
            print(dir0)
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
        cls()
        print("eopDOS v0.4")
        print("""Type "help", "credits", or "license" for more information.""")
        print("")
        dir0 = r"C:\Local User>"
    elif cmd[0:6] == 'chkdsk':
        if cmd[7:] == '':
            chkdsk_noParam()
        elif cmd[7:] == '/r':
            chkdsk_r()
        elif cmd[7:] == '/f':
            chkdsk_f()
    elif cmd[0:4] == 'ping':
        ping = cmd[5:]
        print("Ping request could not find host", ping, ". Please check the name and try again.")
        print("")
    elif cmd == 'ipconfig':
        print("")
        print("eopDOS IP Configuration")
        print("")
        print("")
        print("Ethernet adapter Ethernet")
        print("")
        print("   Media State . . . . . . . . . . . : Media disconnected")
        print("   Connection-specific DNS Suffix  . : VRZN-NT320")
        print("")
        print("Wireless LAN adapter Local Area Connection* 2:")
        print("")
        print("   Media State . . . . . . . . . . . : Media disconnected")
        print("   Connection-specific DNS Suffix  . :")
        print("")
        print("Wireless LAN adapter Local Area Connection* 3:")
        print("")
        print("   Media State . . . . . . . . . . . : Media disconnected")
        print("   Connection-specific DNS Suffix  . :")
        print("")
        print("Ethernet adapter Bluetooth Network Connection:")
        print("")
        print("   Media State . . . . . . . . . . . : Media disconnected")
        print("   Connection-specific DNS Suffix  . :")
        print("")
        print("Wireless LAN adapter Wi-Fi:")
        print("")
        print("   Media State . . . . . . . . . . . : Media disconnected")
        print("   Connection-specific DNS Suffix  . : VRZN-NT320")
        print("")
    elif cmd == 'fc':
        compare1 = input("First file to compare: ")
        compare2 = input("Second file to compare: ")
        if compare1[0:3] == 'new' and compare2[0:3] == 'new':
            try:
                file1 = int(compare1[4:])
                file2 = int(compare2[4:])
                print("File 1:")
                print("")
                print(notepad_files[(int(file1))-1])
                print("")
                print("File 2:")
                print("")
                print(notepad_files[(int(file2))-1])
                print("")
            except IndexError:
                print("File(s) not found.")
                print("")
            except ValueError:
                print("File(s) not found.")
                print("")
        else:
            print("File(s) not found.")
            print("")
    elif cmd == 'systeminfo':
        print("Loading...")
        time.sleep(10)
        print("")
        print("Host Name:                 eopMachine", (sys_serial))
        print("OS Name:                   eopDOS v0.4")
        print("OS Version:                v0.4")
        print("OS Manufacturer:           eyx")
        print("System Manufacturer:       eopDOS")
        print("System Type:               32-bit Virtual Machine")
        print("Processor(s):              1 Processor(s) Installed.")
        print("eopDOS Directory:          C:\EOPDOS_V0.4.PY")
        print("System Directory:          C:\EOPDOS_V0.4.PY")
        print("System Locale:             en-us;English (United States)")
        print("Input Locale:              en-us;English (United States)")
        print("Total Physical Memory:     !Drive Error: 1101")
        print("Available Physical Memory: !Drive Error: 1101")
        print("")

    elif cmd[0:6] == 'verify':
        if cmd[7:] == '':
            if verify_file == False:
                print("Off")
            else:
                print("On")
        if cmd[7:] == '[on]':
            verify_file = True
        elif cmd[7:] == '[off]':
            verify_file = False
        print()
        


    elif cmd == 'diskutil':
        print()
        print("eopDOS Disk Utility version 1.0")
        print()
        print("Copyright (c) eyx under the MIT License")
        print("On computer: eopMachine", (sys_serial),sep="-")
        print()
        while True:
            diskpart_cmd = input("DISKUTIL>")
            if diskpart_cmd == 'list disk':
                print("No physical disk(s) found on this computer.")
                print()
            elif diskpart_cmd == 'list volume':
                print("No physical volume(s) found on this computer.")
                print()
            elif diskpart_cmd == 'list partition':
                print("No partitions found.")
                print()
            elif diskpart_cmd == 'list vdisk':
                print()
                print("Disk #    Status    Free")
                print("-------   --------  -------")
                print("Disk 0    Online    !Drive Error: 1101")
                print("FDisk 1   Online    N/A")
                print()
            elif diskpart_cmd == 'help':
                print("list disk: list the physical disks connected")
                print("list volume: list the physical volumes connected")
                print("list partition: list the physical partitions on disks")
                print("list vdisk: list the virtual disks connected")
                print("exit: leave this program")
                print()
            elif diskpart_cmd == 'exit':
                print()
                break
            else:
                print("Command not found for .")
                print()

    elif cmd[0:8] == 'freedisk':
        if cmd[9:] == 'C':
            print("!Drive Error 1101")
        elif cmd[9:] == 'A':
            print("!Drive Error 1000")
            print("This drive does not have any volumes.")
        elif cmd[9:] == '':
            print("Detecting for virtual drives...")
            time.sleep(0.2)
            print("Virtual drive in volume C found.")
            print("!Drive Error 1101")
        else:
            print("Drive not found on system.")
        print()

    elif cmd[0:5] == 'label':
        if cmd[6:7] == 'C':
            disk_label = cmd[8:]
        #test this
        if cmd[6:7] == 'A':
            print("SystemError 1001: This device's name is locked by the system.")
        else:
            print("Disk not found.")
        print()

    elif cmd[0:6] == "python":
            exec(cmd[7:])
            print()

    elif cmd == 'fdisksys':
        floppyDriveSystem()
            
    elif cmd == 'help':
        #TODO
        print("To start a program, type in the application name.")
        print("dir: print directory")
        print("fdisksys: start the virtual floppy disk system")
        print("chkdsk /f /r: checks disk for errors")
        print("ping: check if a particular web host is reachable")
        print("ipconfig: configure ip")
        print("systeminfo: prints system information")
        print("fc: compare files")
        print("freedisk <drive letter>: checks how much storage is available on this disk")
        print("cd: change directory")
        print("echo: change output string")
        print("chdir: change directory")
        print("cls: clear terminal")
        print("label <drive letter> <new label>: changes the disk label")
        print("hostname: print system name")
        print("python <code>: execute python code")
        print("ver: print version")
        print("verify [on | off]: tells eopDOS to verify files on the disk")
        print("exit: exit shell")
        print("")
    else:
        print((cmd), "is not recognized as an internal or")
        print("external command, operable program or batch file.")
        print("")
        
