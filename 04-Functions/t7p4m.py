def count_letter(n):
    letter = input("Which letter do you want to count: ")
    letter.capitalize()
    n.capitalize()
    count = 0
    for char in n:
        if char == letter:
            count += 1
    return count


if __name__ == "__main__":
    print(count_letter("You never get a second chance to make a first impression"))
    