import figure
import copy
import time

def rec(desk: list, figur_lst: list, n, x_now, y_now, output):
    if n == 0:
        print(*figur_lst, file=output)
        return
    new_figurs = list()
    i = y_now
    j = x_now
    while True:
        if i == len(desk) - 1 and j == len(desk) - 1:
            break
        if j == len(desk) - 1:
            i += 1
            j = 0
        else:
            j += 1
        ability = True
        for e in figur_lst:
            if (j == e[0] or i == e[1]) or (abs(j - e[0]) <= 1 and abs(i - e[1]) <= 1):
                ability = False
        if ability:
            new_figurs.append(tuple([j, i]))

        """   for i in range(len(desk)):
        for j in range(len(desk)):
            ability = True
            for e in figur_lst:
                if (j == e[0] or i == e[1]) or (abs(j - e[0]) <= 1 and abs(i - e[1]) <= 1):
                    ability = False
            if ability:
                new_figurs.append(tuple([j, i]))"""

    for e in new_figurs:
        rec(desk, figur_lst + [e], n - 1, e[0], e[1], output)

def start_algorithm(out, inpt):
    lines = inpt.readlines() # считали строки
    lines = [e.strip("\n" ).split(" ") for e in lines] # Сформатировали строки

    fig = figure.King_Dragon()

    figures = []
    s = int(lines[0][0]) # размечикс
    c = int(lines[0][1]) # скок надо поставить
    for e in lines[1:]:
        figures.append((int(e[0]), int(e[1])))
    matrix = [["0" for _ in range(s)] for _ in range(s)]

    for e in figures:
        matrix = fig.place(e[0], e[1], matrix)

    inpt.close()

    rec(matrix, figures, c, -1, 0, out)
    out.close()
    out = open("output.txt", mode="r+", encoding="utf-8")

    lines = out.readlines()
    if lines == []:
        print("No solution", file=out)
        out.close()
    else:
        out.close()
        """
            output = open("output.txt", mode="w+", encoding="utf-8")
            for i in range(len(lines)):
                lines[i] = lines[i][:-2]
                output.write(lines[i] + "\n")
        """
        out = open("output.txt", mode="r+", encoding="utf-8")

        lines = out.readline().replace("(", "").replace(")", "").replace(",", "").split(" ") # считали строки
        #lines.pop(-1)
        #print(lines)

        matrix_to = [["0" for _ in range(s)] for _ in range(s)]
        for i in range(0, len(lines), 2):
            matrix_to = fig.place(int(lines[i]), int(lines[i+1]), matrix_to)

        out.close()

        for e in matrix_to:
            print(e)

def oop_algorithm(n: int, k: int, l: int, start_figs: list[tuple[str]]):
    desk = [["0" for _ in range(n)] for _ in range(n)]
    fig = figure.King_Dragon()
    for coords in start_figs:
        desk = fig.place(int(coords[0]), int(coords[1]), desk)

    input = open("input.txt", "w+", encoding="utf-8")
    # поменять запись на подходящую
    input.write(str(n) + " ")
    input.write(str(k) + " ")
    input.write(str(l) + "\n")

    for e in start_figs:
        for c in e:
            input.write(str(c+1) + " ")
        input.write("\n")

    c = 0 # figures placed
    i = 0 # y
    j = 0 # x
    while c < k:
        if fig.check_place(j, i, desk):
            desk = fig.place(j, i, desk)
            c += 1
        if i == n - 1 and j == n - 1:
            break
        if j == n - 1:
            i += 1
            j = 0
        else:
            j += 1
    if c < k: return ["0_0"]
    return desk

