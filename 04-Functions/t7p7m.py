def is_binary(n):
    n = str(n)
    valid = True
    for char in n:
        if not (char == "0" or char == "1"):
            valid = False
    return valid

if __name__ == "__main__":
    print(is_binary("100110010"))