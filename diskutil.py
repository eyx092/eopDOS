file_serial_read = open("serialNumber.txt", "r")
sys_serial = int(file_serial_read.read())
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
        print("Command not found for DISKUTIL.")
        print()

