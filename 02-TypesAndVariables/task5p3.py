###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
a = float(a)
b = input('b=')
b = float(b)
c = input('c=')
c = float(c)
volume = a*b*c
surface_area = 2*a*b+2*a*c+2*b*c
print(f"a cuboid with sides {a}, {b} and {c} has a surface area of {surface_area}, and a volume of {volume}")