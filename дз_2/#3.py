x, y = int(input("кол-во строк: ")), int(input("кол-во столбцов: "))
m = list(map(int, input().split()))
massive = []
stol = []
for i in range(x):
    ma = []
    for j in range(y):
        ma.append(m[i + (j * y)])
    stol.append(ma)
print(stol)

for i in range(0, len(m), y):
    ma = []
    for j in range(y):
        ma.append(m[i + j])
    massive.append(ma)
print(massive, "sadvade")
for i in range(x):
    for j in range(y):
        if massive[i][j] == max(massive[i]) == min(stol[j]):
            print(massive[i][j])
