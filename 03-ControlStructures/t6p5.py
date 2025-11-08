###
# Program that simulates the operation of an electronic thermometer.
#
temperature = int(input('Enter temperature: '))
if temperature > 35:
    print("It is extermely hot")
elif temperature > 30:
    print("It's hot")
elif temperature >= 15:
    print("It's warm")
elif temperature >= 0:
    print("It's cold")
else:
    print("Warning - frost")