
# set_1 = set(map(int, input("Введите первое множество:").split()))
# set_2 = set(map(int, input("Введите второе множество:").split()))
# print(set_1 & set_2)

def con(A_s = str, B_s = str):
    c = 0
    print(A_s, B_s)
    for i in range(len(min([A_s, B_s], key=len))):
        c += 1
        if A_s[-(i + 1)] == B_s[-(i + 1)]:
            print(c, A_s[i], B_s[i])


if __name__ == "__main__":
    a = set(map(int, input("Введите первое множество:").split()))
    b = set(map(int, input("Введите второе множество:").split()))
    A = str(sum([10 ** (i - 1) for i in a]))
    B = str(sum([10 ** (i - 1) for i in b]))
    con(A, B)

    # 1111111
    # 00011111