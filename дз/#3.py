sp= [1, 2]
x = int(input())
while (sp[-1] + sp[-2]) < x:
    sp.append(sp[-1] + sp[-2])
print(sp)