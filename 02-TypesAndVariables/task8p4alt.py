import math
cm = int(input("Your height in cm: "))
inches = round(cm*0.3937)
print(f"if you're {cm}cm tall, you're {math.floor(inches/12)} feet and {round(inches%12)} inches tall.")