def f(n):
    sentence = ""
    for char in n:
        if not char == " ":
            sentence += char
    return sentence

if __name__ == "__main__":
    print(f("integrated development environment")) 
    print(f("A programming language is a system of notation for writing computer programs")) 