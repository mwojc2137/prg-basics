def f(password):
    password = str(password)
    chars_used = []
    is_valid = True
    if len(password) >= 6:
        for char in password:
            if not char in chars_used:
                chars_used.append(char)
            else:
                is_valid = False
    else:
        is_valid = False
    return is_valid

if __name__ == "__main__":
    print(f("ax15"))
    print(f("book123"))
    print(f("A2water3"))
    print(f("qwerty"))
    print(f(""))
