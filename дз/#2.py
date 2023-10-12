# программа высчитывает остаток суммы y и x на m по формуле из задания
def ost(x, y, m):
    return (((x % m) + (y % m)) % m)


if __name__ == "__main__":
    a, b, m = int(input("")), int(input()), int(input())
    print(ost(a, b, m))