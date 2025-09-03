while True:
    user_choice = input("please choose the increment in the count to 50, or press q to quit ").lower()
    if user_choice == "q":
        break
    
    else:
        try:
            user_choice = int(user_choice)
            for x in range(1, 51, user_choice):
                print(x)
        except (TypeError, ValueError):
            print("we dont appreciate pen testers here...")
            exit()


exit()