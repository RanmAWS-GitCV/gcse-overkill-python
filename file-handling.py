import datetime

print("\nwe do not appreciate pen testers.\n like, we realy REALLY wish for you not to try to mess around with us...")
print("\nDONT GET ANY IDEAS- we're not hinting at anything here.\n we're just stating the fact that we don't want pen testers!")

while True:
    try:
        password = int(input("please input password 1234- "))
        if password == 1234:
            print("OK! I'll let you go, bye bye!")
            break
        else:
            print("you literally got the password wrong, but aren't even trying to break my ultra un-robust code? WHY? ahem.. i mean try again please...")
    except Exception:
        FileName = str(datetime.datetime.now())
        FileName += "-pen-tester-harrassment-log"
        contents = "HEEEEEEEEEEEELLLLLPP IT'S A PEN TESTER AAAAAAAAAHHHHHHHH"
        with open(FileName, 'w') as f:
            f.write(contents)

        print(f"a new file has been successufully generated!\n\nname: {FileName}\n\ncontents: {contents}")

quit()