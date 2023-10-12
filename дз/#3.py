def finobachi(x = int):# функция записывает числа до числа x
    sp = [1, 2]
    while (sp[-1] + sp[-2]) < x:
        sp.append(sp[-1] + sp[-2])
    return(sp)

if __name__ == "__main__":
    x = int(input())
    print(finobachi(x))