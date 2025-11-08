PIN = "0805"

PINinput = ""

tries = 0

while tries < 3:
    PINinput = input("Enter PIN: ")
    if PINinput == PIN:
        print("Correct.")
        tries += 4
    else:
        print("Incorrect.")
        tries += 1

if not PINinput == PIN:
    print("Your credit card has been blocked.")