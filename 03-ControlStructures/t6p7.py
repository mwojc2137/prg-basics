#Program checking age group
age = int(input("Enter your age: "))

if age >= 65:
    print("You're a senior.")
elif age >= 20:
    print("You're an adult.")
elif age >= 13:
    print("You're a teen.")
else:
    print("You're a child.")