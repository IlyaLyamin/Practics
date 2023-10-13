def killing(n = int):
    x = [x for x in range(1, n + 1)]
    x_copy = [] # будем заполнять индексами убитых
    count = -1
    while len(x_copy) != n - 1:# запускаем цикл до того момента пока не останется один человек
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
    return x

if __name__ == "__main__":
    n = 10 # кол-во людей
    print(*killing(n))