
try:
    number = int(input("input the number "))

    if number > 0:
        print("You're an optimist aren't you?!")
        if number >= 100:
            print("And a megalomaniac too!")
    elif number < 0:
        print("You're an pessimist aren't you?!")
        if number <= -100:
            print("In fact, you took glass half empty so far it's spilled out")
    elif number == 0:
        print("don't even think about trying to divide by this...")
except ValueError:
    print("we dont appreciate pen testers here.")

