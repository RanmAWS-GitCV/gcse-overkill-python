print("this is a grocery list maker")
groceries = []
while True:
    item = input("Keep adding items until you're done, then press q! ")
    if item == "q":
        break
    else:
        groceries.append(item)

print("Here's your grocery list!")
x = 1
for grocery in groceries:
    print("Grocery number", x)
    print(grocery)
    x += 1