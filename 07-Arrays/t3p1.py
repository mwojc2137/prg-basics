arr = [34,7,19,4,21,8]

n = 0
even_sum = 0
while n < len(arr):
    if arr[n]%2 == 0:
        even_sum += arr[n]
    n += 1

print(f"Sum of even numbers in array: {even_sum}")