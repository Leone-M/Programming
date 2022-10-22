def main():
    n = int(input("amount of nums: ")) #

    spisok = [] #изначальный список циферок
    perebor = [] #для брутфорса)

    # ввожу циферки
    for i in range(n):
        spisok.append(int(input("num: ")))

    # целевое значение
    c = int(input("point num: "))

    # ищу все возможные комбинации без повторов
    for i in range(len(spisok)):
        for j in range(i+1, len(spisok)):
            for d in range(j+1, len(spisok)):
                for f in range(d+1, len(spisok)):
                    buf = [spisok[i], spisok[j], spisok[d], spisok[f]]
                    perebor.append(buf)

    # задаю список для сумм от этих комбинаций
    celev = []

    # ищу суммы комбинаций
    for i in range(len(perebor)):
        k = 0
        for j in range(len(perebor[i])):
            k += perebor[i][j]
        celev.append(k)

    # ищу сумму с минимальным отклонением от целевого значения
    minim = 1000
    ii = 0
    for i in range(len(celev)):
        if abs(c - celev[i]) < minim:
            minim = abs(c - celev[i])
            ii = i

    # вывод
    print("numbers: ", perebor[ii], "\nsumm: ", celev[ii])


if __name__ == "__main__":
    main()