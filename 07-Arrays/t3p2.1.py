import random

arr1 = [3,7,1,0,4]

arr2 = [
    [2,3],
    [7,1],
    [0,4]
]

arr3 = []
for i in range(5):
    arr3.append(7)

arr4 = []
for i in range(1,10):
    arr4.append(i)

arr5 = []
for i in range(1,10):
    arr5.append(i**2)

arr6 = []
for i in range (10):
    arr6.append(random.randrange(1,20))

arr7 = []
for i in range (5):
    arr7.append([])

arr8 = []
for i in range (5):
    ar8 = []
    for j in range (2):
        ar8.append(1)
    arr8.append(ar8)

arr9 = []
for i in range (5):
    ar9 = []
    for j in range (3):
        ar9.append(random.randint(1,20))
    arr9.append(ar9)

arr10 = [4,0,3]

arr11 = []
for i in range(15):
    arr11.append(0)

arr12 = []
for i in range(1,31):
    arr12.append(i)

arr13 = []
for i in range(20):
    arr13.append(random.randrange(2))

arr14 = []
for i in range(5):
    ar14 = []
    for j in range(2):
        ar14.append(False)
    arr14.append(ar14)

print("1.", arr1)
print("2.", arr2)
print("3.", arr3)
print("4.", arr4)
print("5.", arr5)
print("6.", arr6)
print("7.", arr7)
print("8.", arr8)
print("9.", arr9)
print("10.", arr10)
print("11.", arr11)
print("12.", arr12)
print("13.", arr13)
print("14.", arr14)