"""задача программы найти седловой элемент массива 
(большим в своей строке и самым маленьким в своем столбце)
1  8 9  7 2 
11 5 12 6 8
9  9 15 9 9    
3   
5""" 
def fount_saddle_elem(x = int, y = int, m = list):
    masive = [m[i: i + y] for i in range(0, (x * y), y)]
    for i in range(x):
        m_el = [] # хранится максимальный(ые) элемент(ы) и его(их) индекс(ы)
        count = -1
        for j in range(y): # находим максимальные элементы в строке
            count += 1
            if not m_el:
                print(m_el, "-1-", count)
                m_el = [masive[i][j], count]
                continue
            if m_el[0] < masive[i][j]:
                print(m_el, "-2-", count)
                m_el = [masive[i][j], count]
                continue
        # на этот момент у нас есть список с максимальным элементом строки и его индесом
        print(m_el, "заходим в цикл по перебору в столбцах")
        A = True
        for j in masive:
            if m_el[0] > j[m_el[1]]:
                print(j[m_el[1]], "- сравниваемы элемент")
                A = False
                break
        if A:
            print("OK")
            return m_el[0]



if __name__ == "__main__":
    x, y = int(input("кол-во строк: ")), int(input("кол-во столбцов: "))
    m = list(map(int, input().split()))
    print(fount_saddle_elem(x, y, m))