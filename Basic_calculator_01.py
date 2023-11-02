def addition(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def subtraction(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def multipication(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def deviton(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")

while True:
    print("A. Addition")
    print("B. subtraction")
    print("C. Multipication")
    print("D. Division")
    print("E. Exit")

    choice = input("input your choice: ")

    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input frist number : "))
        b = int(input("input second number : "))
        addition(a,b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("Input frist number: "))
        b = int(input("input second number: "))
        subtraction(a,b)
    elif choice == "c" or choice == "C":
        print("Multification")
        a = int(input("Input frist number: "))
        b = int(input("Input second number: "))
        multipication(a,b)
    elif choice == "d" or choice == "D":
        print("Devition")
        a = int(input("Input frist numbeer: "))
        b = int(input("Input second number: "))
        deviton(a,b)
    elif choice == "e" or choice == "E":
        print("Exit")
        quit()