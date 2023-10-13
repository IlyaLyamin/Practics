# программа вычисляет пересение двух множеств храня данные в формату int
def con(A_s = str, B_s = str):
    c = 0
    for i in range(len(min([A_s, B_s], key=len))):
        c += 1
        if A_s[-(i + 1)] == B_s[-(i + 1)]:
            print(c, A_s[i], B_s[i])


if __name__ == "__main__":
    a = set(map(int, input("Введите первое множество: ").split()))
    b = set(map(int, input("Введите второе множество: ").split()))
    A, B = str(sum([10 ** (i - 1) for i in a])), str(sum([10 ** (i - 1) for i in b]))
    con(A, B)