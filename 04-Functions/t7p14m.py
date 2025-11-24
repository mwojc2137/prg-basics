def f(n1, n2, o):
    result = 0
    if o == "+":
        result = n1+n2
    elif o == "-":
        result = n1-n2
    elif o == "**":
        result = n1**n2
    elif o == "*":
        result = n1*n2
    elif o == "%":
        result = n1%n2
    else:
        result = "wrong operator"
    return result

if __name__ == "__main__":
    print(f(2,3,"+"))
    print(f(2,3,"%"))
    print(f(2,3,"**"))
    print(f(2,3,"*"))
    print(f(2,3,"-"))