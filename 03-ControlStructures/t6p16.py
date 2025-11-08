###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ')
extra_rinse = input('Extra rinse? (y/n) ')
extra_spin = input('Extra spin? (y/n) ')
correct_input = True

if program == "j":
    total_washing_time = 40
elif program == "u":
    total_washing_time = 70
elif program == "s":
    total_washing_time = 20
else:
    correct_input = False

if extra_rinse == "y":
    total_washing_time += 15
elif not extra_rinse == "n":
    correct_input = False

if extra_spin == "y":
    total_washing_time += 9
elif not extra_spin == "n":
    correct_input = False

if correct_input == True:
    print(f"Washing program will take {total_washing_time} minutes.")
else:
    print("Incorrect input.")