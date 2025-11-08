EAN = input("Enter EAN-13 article number: ")

if EAN.isdigit() == True:
    if len(EAN) == 13:
        print("Article number is correct")
        if EAN[0:3] == "590":
            print("Article manufactured in Poland.")
    else:
        print("Incorrect length.")
else:
    print("Has to be a number.")

