def occurs(n, arr):
    if n in arr:
        return True
    else:
        return False
    
arr = [15,38,7,23,14]

n = int(input("Enter number: "))

print(f"Number in array: {occurs(n,arr)}")