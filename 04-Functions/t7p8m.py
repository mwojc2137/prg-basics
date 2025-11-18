def f(amount_to_pay):
    coins = int(amount_to_pay/5) + int(int(amount_to_pay%5)/2) + (int(amount_to_pay%5)%2)
    return coins

if __name__ == "__main__":
    print(f(23))