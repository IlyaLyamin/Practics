def polynom_znach(x = int, n = int, cfs = list): # принимает на вход корень - x, степень многочлена - n, коэфиценты - cfs и считает значение многочлена
    s = 0
    for i in range(n): # в этом цикле считаем значение многочлена по формуле из задания
        if not s: # если 
            s = (cf[i] * (x) + cf[i + 1])
        else:
            s = (s * (x)) + cf[i + 1]
    if s == 0:
        return (f"корень {x} удовлетворяет")


def znach_proiz(x = int, n = int, cfs = list):  # принимает на вход то же самое что и первая функция, считает значение многочлена производной многочлена
    s_proiz = 0
    for i in range(n): 
        s_proiz += (n - i) * (x ** (n - 1 - i) * cf[i])
        print(s_proiz, f"производная от {i + 1} члена:", (n - i), " ", x, " ", cf[i])
    return(s_proiz, "значение производной")


if __name__ == "__main__":
    n = int(input("Введите степень многочлена\n"))
    x = int(input("Введите корень многочлена\n"))
    cf = list(map(int, input("Введите коэфиценты многочлена\n").split()))
    print(*polynom_znach(x, n, cf))
    print(*znach_proiz(x, n, cf))
