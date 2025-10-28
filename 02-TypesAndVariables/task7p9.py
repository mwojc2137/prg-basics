import random

roll = random.randint(1,6)
one_or_six = bool(roll == 1 or roll == 6)
print(roll)
print(f'Is the roll one or six: {one_or_six}')