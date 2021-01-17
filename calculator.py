print()
import math
print("eopDOS Calculator version 1.0")
print("""Type "/exit" to exit this program.""")
print()
while True:
    _firstNumber = input("Enter first number: ")
    if _firstNumber == '/exit':
        print("")
        break
    else:
        firstNumber = int(_firstNumber)
        operation = input("Enter the operation: ")
        if operation == 'sqrt' :
            answer = math.sqrt(firstNumber)
        elif operation == '%':
            answer = firstNumber * .01
        else:
            secondNumber = int(input("Enter second number: "))
            if operation == 'mod':
                answer = firstNumber % secondNumber
            if operation == '+':
                answer = firstNumber + secondNumber
            if operation == '-':
                answer = firstNumber - secondNumber
            if operation == '*':
                answer = firstNumber * secondNumber
            if operation == '/':
                answer = firstNumber / secondNumber
            if operation == '^':
                answer = firstNumber ** secondNumber

        print(answer)

