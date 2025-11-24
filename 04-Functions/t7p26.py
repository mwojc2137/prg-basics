def f(text):
    if len(text) > 0:
        modtext = str(text[0])
    else:
        return ""
    for i in range (1,len(text)):
        modtext += "-" + str(text[i])
    return modtext

if __name__ == "__main__":
    print(f("University"))
    print(f("UE"))
    print(f("x"))
    print(f(""))
