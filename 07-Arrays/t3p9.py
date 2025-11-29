def compare(arr1, arr2):
    same = True
    if len(arr1) != len(arr2):
        same =  False
    else:
        n = 0
        while n < len(arr1):
            if arr1[n] != arr2[n]:
                same = False
            n += 1
    return same

arr11 = ["water","book","sky"]
arr12 = ["water","book","sky"]
arr21 = [True,False]
arr22 = [True,False,True]
arr31 = [5,3,1]
arr32 = [5,3,1]
arr41 = [3,2,1]
arr42 = [3,2]

print(compare(arr11, arr12))
print(compare(arr21, arr22))
print(compare(arr31, arr32))
print(compare(arr41, arr42))