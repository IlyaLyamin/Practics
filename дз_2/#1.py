sp = list(map(int, input().split()))
n = int(input())
mx = 0
for i in range(len(sp) - n + 1):
    if mx < sum(sp[i: i + n]):
        mx = sum(sp[i: i + n])
        print(sp[i: i + n])
print(mx)