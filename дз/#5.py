def factorial_(num = int): # вычислет факториал
    ans = 1
    for i in range(1, num + 1):
        ans *= i
    return ans

def factorial_zeros(num = int): # вычисляет кол-во нулей факториала
    c = 1
    s = 0
    while (5 ** c) <= num: # находим кол-во делений на 5, 25, 125, 625...
        s += num // (5 ** c)
        c += 1
    return s

if __name__ == "__main__":
    num = int(input())
    print(factorial_(num))
    print(factorial_zeros(num))