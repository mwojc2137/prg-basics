import math
radius = int(input("Enter radius: "))
area = radius**2*math.pi
circumference = 2*math.pi*radius
print(f"radius = {radius}, area is {round(area, 2)}, circumeference is {round(circumference, 2)}")