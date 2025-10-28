###
# checks if speed is valid on polish highways (40 > x < 140)
#

speed = int(input("Enter car speed: "))
is_ok = bool(speed >= 40 and speed <= 140)
print(f'Speed is valid: {is_ok}')