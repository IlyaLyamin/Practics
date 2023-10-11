n = 40000
x = [x for x in range(1, n + 1)]
x_copy = []
count = -1
while len(x_copy) != n - 1:
    l_count = 0
    while True:
        count += 1
        if l_count == 2 and x[count % len(x)] not in x_copy:
            x_copy.append(x[count % len(x)])
            break
        elif l_count != 2 and x[count % len(x)] not in x_copy:
            l_count += 1
            continue
for i in x_copy:
    x.remove(i)
print(*x)

