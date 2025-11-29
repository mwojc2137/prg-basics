arr = [7,9,2,4,5,6]


n = 0
while n < len(arr) :
    if arr[n]%2 != 0:
        i = n
        while i < len(arr) and arr[i]%2 != 0:
            i += 1
        if i < len(arr) and arr[i]%2 == 0:
            cache = arr[n]
            arr[n] = arr[i]
            arr [i] = cache
    n += 1

print (arr)
