def f(dice):
    dice = str(dice)
    in_row = 0
    max_in_row = 0
    n = 1
    while n < len(dice):
        if dice[n] == dice[n-1]:
            in_row += 1
        if max_in_row < in_row:
            max_in_row = in_row
            result = dice[n]
        elif dice[n] != dice[n-1]:
            in_row = 0
        n += 1
    return result

        

if __name__ == "__main__":
    print(f("5233165554211"))
    print(f("2133"))
