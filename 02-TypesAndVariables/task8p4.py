###
# A program that prints your height both in cm and in feet and inches.
#
import math
cm = int(input("How tall are you? "))
feet = cm*0.0328 # calculate the number of feet
inches = round(feet*12-(math.floor(feet)*12)) #calculates the number of inches

if inches == 12: #accounts for the situation in which the number of should round up, because the number of inches is 12 
    inches = 0
    feet = feet+1

print(f'I am {cm}cm tall, i.e. {math.floor(feet)} feet and {inches} inches')