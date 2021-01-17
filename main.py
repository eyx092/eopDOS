import time
print("DOS Simulator v0.01a")
print("Starting...")
time.sleep(2)
files = 1
disk_spaceDirectory = '15,998,006'
disk_spaceChkdsk = '15,999.006'
space_in_use = '1,002'
print("Type credits or help for more information.")
print(" ")
lineOn = 1
fileCreated = False
directory = r"C:\Administrator>"
while lineOn == 1:
    line_input = input(directory)
    if line_input == 'dir' and fileCreated == False and directory == r"C:\Administrator>":
        print("Volume in drive C has no label")
        print("Volume Serial Number is 5A74-HGHG")
        print("                        1,002 math_quiz.exe")
        print("             ", (files), "File(s)")
        #print("              0 Dir(s)  15,998,006 bytes free")
        print("              0 Dir(s) ", (disk_spaceDirectory), " bytes free")
        print(" ")
        lineOn = 1
    elif line_input == 'dir' and directory == r"C:\>":
        print("Volume in drive C has no label")
        print("Volume Serial Number is 5A74-HGHG")
        print("                        12,088 dos_simulator_v0.01a.py")
        print("             ", (files), "File(s)")
        #print("              0 Dir(s)  15,998,006 bytes free")
        print("              0 Dir(s) ", (disk_spaceDirectory), " bytes free")
        print(" ")
        lineOn = 1
    elif line_input == 'dir' and fileCreated == True and directory == r"C:\Administrator>":
        print("Volume in drive C has no label")
        print("Volume Serial Number is 5A74-HGHG")
        print("                        1,002 math_quiz.exe")
        print("                        88 textfile.txt")
        print("             ", (files), "File(s)")
        #print("              0 Dir(s)  15,997,918 bytes free")
        print("              0 Dir(s) " ,(disk_spaceDirectory), " bytes free")
        print(" ")
    elif line_input == 'dir' and fileCreated == False and directory == '':
        print("Volume in drive C is Windows")
        print("Volume Serial Number is 5A74-HGHG")
        print("                        1,002 math_quiz.exe")
        print("             ", (files), "File(s)")
        #print("              0 Dir(s)  15,998,006 bytes free")
        print("              0 Dir(s) ", (disk_spaceDirectory), " bytes free")
        print(" ")
        lineOn = 1
    elif line_input == 'dir' and fileCreated == True and directory == '':
        print("Volume in drive C is Windows")
        print("Volume Serial Number is 5A74-HGHG")
        print("                        1,002 math_quiz.exe")
        print("                        88 textfile.txt")
        print("             ", (files), "File(s)")
        #print("              0 Dir(s)  15,997,918 bytes free")
        print("              0 Dir(s) " ,(disk_spaceDirectory), " bytes free")
        print(" ")
    elif line_input == 'dir' and directory == r"C:\User>":
        print("Volume in drive C is Windows")
        print("Volume Serial Number is 5A74-HGHG")
        print("              0 File(s)")
        print("              0 Dir(s)  15,999,008 bytes free")
        print(" ")
    elif line_input == 'hostname':
        print("SYSTEM-JI86B304")
        print(" ")
        lineOn = 1
    elif line_input == 'chkdsk /r':
        if directory == 'C:\Administrator>':
            time.sleep(0.5)
            print("The type of the file system is NTFS.")
            print(" ")
            print("Running CHKDSK in write/read mode.")
            print(" ")
            print("CHKDSK is running a write test (stage 1 of 4)...")
            time.sleep(10)
            print("Write test completed.")
            print("CHKDSK is verifying files (stage 2 of 4)...")
            time.sleep(1.2)
            print("File verification completed.")
            print("CHKDSK is verifying indexes (stage 3 of 4)...")
            time.sleep(2)
            print("Index verification completed.")
            print("CHKDSK is verifying security descriptors (stage 4 of 4)...")
            time.sleep(3)
            print("Security descriptor verification completed.")
            print("CHKDSK is verifying Usn Journal...")
            time.sleep(4)
            print("Usn Journal verification completed.")
            print(" ")
            print("  16,000 KB total disk space.")
            #print("  0 KB in 0 files.")
            print("  ", (space_in_use), "KB in ", (files), " files.")
            print("  0 KB in 0 dirs.")
            print("  0 KB in bad sectors.")
            print("  4 KB in use by the system.")
            print("  2 KB occupied by the log file.")
            print("  ", (disk_spaceChkdsk), " KB available on disk.")
            print(" ")
            print("  3907 total allocation units on disk.")
            print("  3906 allocation units available on disk.")
            print(" ")
            lineOn = 1
        if directory == '':
            time.sleep(0.2)
            print("The type of the file system is NTFS.")
            print(" ")
            print("Running CHKDSK in write/read mode.")
            print(" ")
            print("CHKDSK is running a write test (stage 1 of 4)...")
            time.sleep(9.7)
            print("Write test completed.")
            print("CHKDSK is verifying files (stage 2 of 4)...")
            time.sleep(2)
            print("File verification completed.")
            print("CHKDSK is verifying indexes (stage 3 of 4)...")
            time.sleep(1)
            print("Index verification completed.")
            print("CHKDSK is verifying security descriptors (stage 4 of 4)...")
            time.sleep(6)
            print("Security descriptor verification completed.")
            print("CHKDSK is verifying Usn Journal...")
            time.sleep(3)
            print("Usn Journal verification completed.")
            print(" ")
            print("  16,000 KB total disk space.")
            #print("  0 KB in 0 files.")
            print("  ", (space_in_use), "KB in ", (files), " files.")
            print("  0 KB in 0 dirs.")
            print("  0 KB in bad sectors.")
            print("  4 KB in use by the system.")
            print("  2 KB occupied by the log file.")
            print("  ", (disk_spaceChkdsk), " KB available on disk.")
            print(" ")
            print("  3907 total allocation units on disk.")
            print("  3906 allocation units available on disk.")
            print(" ")
        if directory == r"C:\User>":
            print("Access Denied as you do not have sufficient privileges or")
            print("the disk may be locked by another process.")
            print("You have to invoke this utility running in elevated mode")
            print("and make sure the disk is unlocked.")
            print(" ")
    elif line_input == 'chkdsk /f':
        if directory == 'C:\Administrator>':
            time.sleep(0.3)
            print("The type of the file system is NTFS.")
            print(" ")
            print("Running CHKDSK in read-only mode.")
            print(" ")
            print("CHKDSK is verifying files (stage 1 of 3)...")
            time.sleep(1.6)
            print("File verification completed.")
            print("CHKDSK is verifying indexes (stage 2 of 3)...")
            time.sleep(3)
            print("Index verification completed.")
            print("CHKDSK is verifying security descriptors (stage 3 of 3)...")
            time.sleep(2)
            print("Security descriptor verification completed.")
            print("CHKDSK is verifying Usn Journal...")
            time.sleep(5)
            print("Usn Journal verification completed.")
            print(" ")
            print("  16,000 KB total disk space.")
            print("  ", (space_in_use), "KB in ", (files), " files.")
            print("  0 KB in 0 dirs.")
            print("  0 KB in bad sectors.")
            print("  4 KB in use by the system.")
            print("  2 KB occupied by the log file.")
            print("  ", (disk_spaceChkdsk), " KB available on disk.")
            print(" ")
            print("  3907 total allocation units on disk.")
            print("  3906 allocation units available on disk.")
            print(" ")
            lineOn = 1
        elif directory == '':
            time.sleep(3)
            print("The type of the file system is NTFS.")
            print(" ")
            print("Running CHKDSK in read-only mode.")
            print(" ")
            print("CHKDSK is verifying files (stage 1 of 3)...")
            time.sleep(1)
            print("File verification completed.")
            print("CHKDSK is verifying indexes (stage 2 of 3)...")
            time.sleep(2)
            print("Index verification completed.")
            print("CHKDSK is verifying security descriptors (stage 3 of 3)...")
            time.sleep(4)
            print("Security descriptor verification completed.")
            print("CHKDSK is verifying Usn Journal...")
            time.sleep(1)
            print("Usn Journal verification completed.")
            print(" ")
            print("  16,000 KB total disk space.")
            print("  ", (space_in_use), "KB in ", (files), " files.")
            print("  0 KB in 0 dirs.")
            print("  0 KB in bad sectors.")
            print("  4 KB in use by the system.")
            print("  2 KB occupied by the log file.")
            print("  ", (disk_spaceChkdsk), " KB available on disk.")
            print(" ")
            print("  3907 total allocation units on disk.")
            print("  3906 allocation units available on disk.")
            print(" ")
            lineOn = 1
        if directory == r"C:\User>":
            print("Access Denied as you do not have sufficient privileges or")
            print("the disk may be locked by another process.")
            print("You have to invoke this utility running in elevated mode")
            print("and make sure the disk is unlocked.")
            print(" ")
    elif line_input == 'chkdsk':
        if directory == 'C:\Administrator>':
            time.sleep(0.1)
            print("The type of the file system is NTFS.")
            print(" ")
            print("WARNING! F paramater not specified.")
            print("Running CHKDSK in read-only mode.")
            print(" ")
            print("CHKDSK is verifying files (stage 1 of 3)...")
            time.sleep(1)
            print("File verification completed.")
            print("CHKDSK is verifying indexes (stage 2 of 3)...")
            time.sleep(2)
            print("Index verification completed.")
            print("CHKDSK is verifying security descriptors (stage 3 of 3)...")
            time.sleep(3)
            print("Security descriptor verification completed.")
            print("CHKDSK is verifying Usn Journal...")
            time.sleep(2)
            print("Usn Journal verification completed.")
            print(" ")
            print("  16,000 KB total disk space.")
            print("  ", (space_in_use), "KB in ", (files), " files.")
            print("  0 KB in 0 dirs.")
            print("  0 KB in bad sectors.")
            print("  4 KB in use by the system.")
            print("  2 KB occupied by the log file.")
            print("  ", (disk_spaceChkdsk), " KB available on disk.")
            print(" ")
            print("  3907 total allocation units on disk.")
            print("  3906 allocation units available on disk.")
            print(" ")
            lineOn = 1
        elif directory == '':
            time.sleep(2)
            print("The type of the file system is NTFS.")
            print(" ")
            print("WARNING! F paramater not specified.")
            print("Running CHKDSK in read-only mode.")
            print(" ")
            print("CHKDSK is verifying files (stage 1 of 3)...")
            time.sleep(4)
            print("File verification completed.")
            print("CHKDSK is verifying indexes (stage 2 of 3)...")
            time.sleep(1)
            print("Index verification completed.")
            print("CHKDSK is verifying security descriptors (stage 3 of 3)...")
            time.sleep(1)
            print("Security descriptor verification completed.")
            print("CHKDSK is verifying Usn Journal...")
            time.sleep(2)
            print("Usn Journal verification completed.")
            print(" ")
            print("  16,000 KB total disk space.")
            print("  ", (space_in_use), "KB in ", (files), " files.")
            print("  0 KB in 0 dirs.")
            print("  0 KB in bad sectors.")
            print("  4 KB in use by the system.")
            print("  2 KB occupied by the log file.")
            print("  ", (disk_spaceChkdsk), " KB available on disk.")
            print(" ")
            print("  3907 total allocation units on disk.")
            print("  3906 allocation units available on disk.")
            print(" ")
            lineOn = 1
        if directory == r"C:\User>":
            print("Access Denied as you do not have sufficient privileges or")
            print("the disk may be locked by another process.")
            print("You have to invoke this utility running in elevated mode")
            print("and make sure the disk is unlocked.")
            print(" ")
    elif line_input == 'cmd':
        print(" ")
        print(" ")
        print("DOS Simulator v0.01a")
        print("Type credits or help for more information.")
        print(" ")
        directory = 'C:\Administrator>'
        lineOn = 1
    elif line_input == 'credits':
        print("All work done by eyx")
        print("Last updated 3/18/2020")
        print(" ")
    elif line_input == 'help':
        print("dir")
        print("   prints directories and files")
        print("hostname")
        print("   prints name of computer")
        print("chkdsk /r /f")
        print("   checks disk for bad sectors and does a disk scan")
        print("cmd")
        print("   restarts command line")
        print("ver")
        print("   prints version")
        print("del")
        print("   delete a file")
        print("load")
        print("   load a file")
        print("start notepad textfile.txt")
        print("   starts a text file with the file name textfile.txt")
        print("cd")
        print("   change directory")
        print("echo on")
        print("   shows directory when typing commands")
        print("echo off")
        print("   doesn't show directory when typing commands")
        print("exit")
        print("   exits command line")
    elif line_input == 'ver':
        print("v0.01alpha")
        print(" ")
        lineOn = 1
    elif line_input == 'del':
        delete = input("Enter a filename to delete: ")
        if delete == 'textfile.txt' and (directory == r"C:\Administrator>" or directory == '') and fileCreated == True:
            confirm_delete = input("Are you sure you want to delete this this file? (Y/N): ")
            if confirm_delete == 'y':
                fileCreated = False
                files = 1
                disk_spaceDirectory = '15,998,006'
                disk_spaceChkdsk = '15,998.006'
                space_in_use = '1,002'
                print("Deleting file...")
                time.sleep(3)
                print("File deleted.")
                print(" ")
            else:
                print(" ")
        elif delete == 'textfile.txt' and directory == r"C:\User>" and fileCreated == True:
            print("Access Denied as you do not have sufficient privileges or")
            print("the disk may be locked by another process.")
            print("You have to invoke this utility running in elevated mode")
            print("and make sure the disk is unlocked.")
            print(" ")
        elif delete == 'math_quiz.exe':
            print("Pre-loaded files may not be deleted.")
            print(" ")
        else:
            print("The file", (delete), "does not exist.")
            print(" ")
    elif line_input == 'load':
        load_file = input("Enter a file name to load: ")
        if load_file == 'textfile.txt' and fileCreated == True and directory == r"C:\Administrator>":
            print(textfile)
            print(" ")
        elif load_file == 'textfile.txt' and fileCreated == True and directory == '':
            print(textfile)
            print(" ")
        elif load_file == 'textfile.txt' and fileCreated == True and directory == r"C:\User>":
            print("Access Denied as you do not have sufficient privileges or")
            print("the disk may be locked by another process.")
            print("You have to invoke this utility running in elevated mode")
            print("and make sure the disk is unlocked.")
            print(" ")
        elif load_file == 'math_quiz.exe':
            start_quiz = input("Press S and then enter to start: ")
            if start_quiz == 's':
                questions_correct = 0
                question1 = input("What is 9 + 10? ")
                if question1 == '19':
                    print("Correct!")
                    questions_correct += 1
                else:
                    print("Incorrect")
                question2 = input("What are the first three digits of pi? ")
                if question2 == '3.14':
                    print("Correct!")
                    questions_correct += 1
                else:
                    print("Incorrect")
                question3 = input("What is 5 modulo 3? ")
                if question3 == '2':
                    print("Correct!")
                    questions_correct += 1
                else:
                    print("Incorrect")
                question4 = input("What is the standard deviation for the set of numbers {1, 2, 3, 4, 5}? ")
                if question4 == 'sqrt 2':
                    print("Correct!")
                    questions_correct += 1
                else:
                    print("Incorrect")
                print("You got", (questions_correct), "out of 4 questions correct.")
                print(" ")
            elif start_quiz != 's':
                print(" ")
        else:
            print((load_file), "does not exist")
            print(" ")
        lineOn = 1
    elif line_input == 'start notepad textfile.txt':
        if fileCreated == False:
            files = 2
            disk_spaceDirectory = '15,997,918'
            disk_spaceChkdsk = '15,997.918'
            space_in_use = '1,090'
            textfile = input("Start textfile.txt> ")
            fileCreated = True
            print("Saving file...")
            time.sleep(2)
            print("File saved.")
            print(" ")
        elif fileCreated == True and (directory == r"C:\Administrator>" or directory == ''):
            print("textfile.txt already exists.")
            overwrite = input("Would you like to overwrite this file? (Y/N): ")
            if overwrite == 'y':
                textfile = input("Overwrite textfile.txt> ")
                print(" ")
            else:
                print(" ")
        elif fileCreated == True and directory == r"C:\User>":
            print("You do not have permission to overwrite this file.")
            print(" ")
    elif line_input[0:2] == 'cd':
        cdTo = line_input[3:]
        if cdTo == 'Administrator':
            directory = "C:\Administrator>"
            print(" ")
        elif cdTo == 'User':
            directory = r"C:\User>"
            print(" ")
        elif cdTo == '..':
            directory = r"C:\>"
            print("")
        else:
            print((cdTo), "does not exist as a directory")
            print(" ")
    elif line_input == 'echo off':
        directory = ''
    elif line_input == 'echo on':
        directory = "C:\Administrator>"
        print(" ")
    elif line_input == 'exit':
        lineOn = 0
    elif line_input == '':
        print(" ")
    else:
        print((line_input), "is not recognized as an internal or")
        print("external command, operable program or batch file.")
        print(" ")
        lineOn = 1
