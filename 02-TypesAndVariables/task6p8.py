###
# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = ord(last)-ord(first)
print(f'Between {first} and {last} is {number_of_letters-1} letters')