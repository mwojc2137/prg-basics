arr = [15,8,31,47,2,19]

total = 0
n = 0
while n < len(arr):
    total += arr[n]
    n += 1

average = total / len(arr)

print(arr)
print(average)