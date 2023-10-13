"""задача программы найти седловой элемент массива 
(большим в своей строке и самым маленьким в своем столбце)""" 
def fount_saddle_elem(x = int, y = int, m = list):
    masive = [m[i: i + y] for i in range(0, (x * y), y)]
    for i in range(x):
        m_el = [] # хранится максимальный(ые) элемент(ы) и его(их) индекс(ы)
        count = -1
        for j in range(y): # находим максимальные элементы в строке
            count += 1
            if not m_el:
                print(m_el, "-1-", count)
                m_el.append([masive[i][j], count])
                continue
            if m_el[0][0] == masive[i][j]:
                print(m_el, "-2-", count)
                m_el.append([masive[i][j], count])
                continue
            if m_el[0][0] < masive[i][j]:
                print(m_el, "-3-", count)
                m_el = [[masive[i][j], count]]
                continue
        # на этот момент у нас есть кортеж с максимальными элементами строки и их индесами
        print(m_el)
        for l in m_el:
            print(l)
            A = True
            for j in masive:
                if l[0] != j[l[1]]:
                    A = False
                    break
            if A:
                return l[0]
                break



if __name__ == "__main__":
    x, y = int(input("кол-во строк: ")), int(input("кол-во столбцов: "))
    m = list(map(int, input().split()))
    print(fount_saddle_elem(x, y, m))