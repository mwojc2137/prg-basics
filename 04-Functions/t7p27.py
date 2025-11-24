def f(product_code):
    sum = int(product_code[0]) + int(product_code[1]) + int(product_code[2])
    is_correct = False
    if sum%7 == int(product_code[3]):
        is_correct = True
    return is_correct

if __name__ == "__main__":
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))