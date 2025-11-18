def f(x, y):
    negatives = 0
    for i in range (x,y):
        if i < 0 and i%2 == 0:
            negatives += 1
    return negatives

if __name__ == "__main__":
    print(f(-7,8))