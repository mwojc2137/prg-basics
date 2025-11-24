def sum_natural(n):
    if n == 0:
        return 0
    if n > 0:
        return n + sum_natural(n-1)

if __name__ == "__main__":
    print(sum_natural(10))