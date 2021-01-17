print("pyMark v1.0a")
print("Starting...")
import calendar
import time
import sys
from random import randint
print("To start pyMark, press 'S' and then enter.")
init = input("To exit, type 'exit' and then enter: ")
if init == 's':
    print("WARNING! You may exprience a decrease in performance")
    print("on other applications while this benchmark is running.")
    confirm_init = input("Continue (Y/N)? ")
    if confirm_init == 'y':
        current_epoch = calendar.timegm(time.gmtime())
        print("Running the benchmark...")
        print("|", end="")
        for i in range(100000000):
            x = randint(1,9999999999999999)
            y = randint(1,9999999999999999)
            z = x / y
            if i % 10000000 == 0:
                print("\u2593", end="")
        epoch = calendar.timegm(time.gmtime())
        print("|", end="")
        print()
        print("debug")
        print(current_epoch)
        print(epoch)
        runtime = epoch - current_epoch
        benchmark = 100000000/(runtime)
        runtime_min = runtime // 60
        runtime_sec = runtime % 60
        print("PyMark Score:", benchmark)
        print("Total Benchmark Runtime:", runtime_min, "min", runtime_sec, "sec")
        time.sleep(10)
        print("Closing the application...")
        print()
    elif confirm_init == 'n':
        print("Closing the application...")
        print()
    else:
        print("Command not found. Closing the application...")
        print()
elif init == 'exit':
    print("Closing the application...")
    print()
else:
    print("Command not found. Closing the application...")
    print()
