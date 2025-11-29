def number(text):
    arr = text.split(" ")
    return len(arr)

def order(text):
    arr = text.split(" ")
    for i in range (len(arr)):
        for j in range (len(arr)):
            if len(arr[i]) > len(arr[j]):
                cache = arr[j]
                arr[j] = arr[i]
                arr[i] = cache
    return arr

def alphabet(text):
    arr = text.split(" ")
    arr.sort()
    return arr

