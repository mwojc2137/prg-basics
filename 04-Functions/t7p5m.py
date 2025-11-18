def range(x, y):
    n = int(input("Enter a number: "))
    is_in_range = False
    if n >= x and n <= y:
        is_in_range = True
    if is_in_range == True:
        return f"Number in range <{x},{y}>: yes"
    elif is_in_range == False:
        return f"Number in range <{x},{y}>: no"
    

if __name__ == "__main__":
    print(range(2,15))
    