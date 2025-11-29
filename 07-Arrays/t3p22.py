import random

arr1 = [4,5,6,7,4,3,2,5]

def rand_elem(arr):
    return arr[random.randrange(len(arr)-1)]


print(rand_elem(arr1))