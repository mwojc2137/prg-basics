# Program calculates parking fee
parking_time = int(input("How long (hours) was the car parked for? "))

if parking_time > 6:
    print("Parking fee is 20PLN.")
elif parking_time > 2:
    print("Parking fee is 15PLN.")
else:
    print("Parking fee is 5PLN.")
