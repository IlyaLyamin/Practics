x = int(input())
masive = [i for i in range(2, x + 1)]
for i in range(2, x + 1):
    p = 2
    if masive:
        while max(masive) >= (i * p):
            if (i * p) in masive:
                masive.remove(i * p)
            p += 1
            if not masive:
                break

for i in masive[::-1]:
    if (x % i) == 0:
        print(i)
        break