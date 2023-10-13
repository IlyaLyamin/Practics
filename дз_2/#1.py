def max_sum(sp = list, n = int):# sp - список с цифрами, n - длина максисмальной суммы 
    mx = [sp[0], sp[1], sp[2]]
    l_m = []
    for i in range(1, len(sp) - n + 1):
        l_m = sp[i:i+n]
        if l_m[-1] > mx[0]:
            mx = sp[i: i + n]
    return mx


if __name__ == "__main__":
    sp = list(map(int, input().split()))
    n = int(input())
    print(max_sum(sp, n))