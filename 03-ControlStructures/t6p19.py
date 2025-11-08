print("SURVEY")
interest = input("Are you interested in computer science? (y/n): ")
playing = input("Do you like playing computer games? (y/n): ")
instagram = input("Do you have an instagram account? (y/n): ")

if interest == "y":
    interest = "Yes"
elif interest == "n":
    interest = "No"
else:
    print("Wrong input in first question.")

if playing == "y":
    playing = "Yes"
elif playing == "n":
    playing = "No"
else:
    print("Wrong input in second question.")

if instagram == "y":
    instagram = "Yes"
elif instagram == "n":
    instagram = "No"
else:
    print("Wrong input in third question.")


print(" ")

if interest == "Yes" or interest == "No" and playing == "Yes" or playing == "No" and instagram == "Yes" or instagram == "No":
    print("SURVEY RESULTS")
    print(f"Interested in computer science: {interest}")
    print(f"Playing computer games: {playing}")
    print(f"Has an instagram account: {instagram}")