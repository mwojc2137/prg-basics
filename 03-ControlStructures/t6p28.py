list = [0, 1]
next = 0
sequence = "0 1"

for i in range(0,18):
    next = list[len(list)-2] + list[len(list)-1]
    list.append(next)
    sequence += (" " + str(next))

print(sequence)

print(list)