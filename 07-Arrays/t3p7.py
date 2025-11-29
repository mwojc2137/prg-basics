arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]

max = 0
longest_name = ""

for row in arr:
    if len(row) > max:
        longest_name = row
        max = len(row)

print(longest_name)