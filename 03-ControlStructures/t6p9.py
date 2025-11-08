#Program that checks, wheter a word is in some likelihood a female name
name = input("Enter name: ")
ll = len(name)-1
if name[ll] == "a":
    print(f"{name} - Polish female name (potentially)")
