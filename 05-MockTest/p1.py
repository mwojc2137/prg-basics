def f(n):
    n = str(n)
    acronym = ""
    if len(n) == 0:
        return ""
    else:
        acronym = n[0]
        p = 1
        while p < len(n):
            if n[p] == " ":
                acronym += n[p+1]
            p += 1
        return acronym
    

if __name__ == "__main__":
    print(f("Internet of Things"))
    print(f("Fou Your Information"))
    print(f("Python"))
    print(f(""))
