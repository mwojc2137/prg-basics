###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print('Last value', arr[-1])
print('Last but one value', arr[len(arr)-2])
print('Sum of the first and last values', arr[0]+arr[len(arr)-1])
print('Middle value', arr[int(len(arr)/2)])

all = ""
for i in range (len(arr)):
    all += str(arr[i]) + " "

print("All array values", all)