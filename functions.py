print("this is a basic calculator")

def add(num1, num2):
    ans = num1 + num2
    print("Answer:", ans)

def times(num1, num2):
    ans = num1 * num2
    print("Answer:", ans)

def take(num1, num2):
    ans = num1 - num2
    print("Answer:", ans)

def divide(num1, num2):
    try:
        ans = num1/num2
        print("Answer:", ans)
    except ZeroDivisionError:
        print("there's one thing that computers hate more than dividing by 0. it's finding the square root of -1.")

while True
    try:
        num1 = float(input("input first number "))
        num2 = float(input("input second number "))
    except ValueError:
        print("We dont appreciate pen testers here!")
        exit()
    choice = input("choose the correct option number\n Option 1: addition\n Option 2: subtraction\n Option 3: Multiplication\n Option 4: Division\nOption number- ").strip()

    if choice == "q":
        print("Bye Bye!")
        exit()
    elif choice == "1":
        add(num1, num2)
    elif choice == "2":
        take(num1, num2)
    elif choice == "3":
        times(num1, num2)
    elif choice == "4":
        divide(num1, num2)
    else:
        print("WE DONT ACCEPT PEN TESTERS HERE")