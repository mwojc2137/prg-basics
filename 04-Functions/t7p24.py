def f(expression):
    sum = int(expression[0])
    expression = str(expression)
    for i in range (0,len(expression)):
        if expression[i] == "+":
            sum += int(expression[i+1])
        elif expression[i] == "-":
            sum -= int(expression[i+1])
    return sum

if __name__ == "__main__":
    print(f("2+3"))
    print(f("3+8+1"))
    print(f("2+3-4+5-0"))