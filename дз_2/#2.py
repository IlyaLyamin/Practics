def resheto(x = int): # x - число для которого надо найти максимальный делитель
    masive = [i for i in range(2, x + 1)]
    for i in range(2, (x // 2) + 1):
        p = 2
        if masive:
            while max(masive) >= (i * p):
                if (i * p) in masive:
                    masive.remove(i * p)
                p += 1
                if not masive:
                    break
    return masive


def found_prime_div(x = int):
    masive = resheto(x)
    for i in masive[::-1]:
        if (x % i) == 0:
            return i

if __name__ == "__main__":
    x = int(input())
    print(found_prime_div(x))

    