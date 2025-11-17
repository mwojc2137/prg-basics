import math

def triangle_area(a, b, c):
    s = (a + b + c)/2
    result = math.sqrt(s*(s-a)*(s-b)*(s-c))
    return result

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

print(f'The area of a triangle with sides {a}, {b}, {c} is {triangle_area(a, b, c)}')