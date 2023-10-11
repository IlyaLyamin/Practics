n = int(input("Введите степень многочлена\n"))
x = int(input("Введите корень многочлена\n"))
cf = list(map(int, input("Введите коэфиценты многочлена\n").split()))
s = 0
s_proiz = 0
for i in range(n):
    if not s:
        s = (cf[i] * (x) + cf[i + 1])
    else:
        s = (s * (x)) + cf[i + 1]
print(s, "значение")
for i in range(n):
    s_proiz += (n - 1 - i) * x * cf[i]
print(s_proiz, "значение производной")
