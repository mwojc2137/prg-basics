#Program calculates dogs age in dogs years
age = int(input("Enter dogs age: "))
dogsyears = 0

if age >=2:
    dogsyears = 21 + 4*(age-2)
elif age == 1:
    dogsyears = 10.5

print(f"Dogs age in dogs years is {dogsyears}")