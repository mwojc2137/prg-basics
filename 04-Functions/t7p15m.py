def f(detector):
    people = 0
    more_than_3 = False
    for char in detector:
        if char == "+":
            people += 1
            if people >= 3:
                more_than_3 = True
        elif char == "-":
            people -= 1
    return more_than_3


if __name__ == "__main__":
    print(f("+-+++-+---")) 
    print(f("+-+-+-+-")) 
    print(f("+-++-+--")) 
    print(f("+-++-++-+---"))