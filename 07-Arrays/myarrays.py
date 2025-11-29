def bubble_sort(arr):
   n = len(arr)
   for i in range(n+1):
      for j in range(n-i-1):
         if arr[j] > arr[j+1]:
            x = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = x
   return arr



def f1(arr):
   sorted_arr = bubble_sort(arr)
   return sorted_arr[len(sorted_arr)-2]

def f2(arr):
   sorted_arr = bubble_sort(arr)
   return sorted_arr[len(sorted_arr)-1] - sorted_arr[0]

def f3(arr):
   sorted_arr = bubble_sort(arr)
   if len(sorted_arr)%2 == 0:
      return (sorted_arr[len(sorted_arr)/2] + sorted_arr[(len(sorted_arr)/2)-1])/2
   else:
      return sorted_arr[int(len(sorted_arr)/2)]
   
def f4(arr):
   sorted_arr = bubble_sort(arr)
   minmax = []
   minmax.append(sorted_arr[0])
   minmax.append(sorted_arr[len(sorted_arr)-1])
   return minmax

def f5(arr):
   string = ""
   for row in arr:
      string += str(row) + "-"
   return string[:len(string)-1]