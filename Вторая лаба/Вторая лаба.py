import copy
import time

start = time.time()

def ultra_mega_king_dragon_figure(x, y, desk):
    # добавляю по вертикали
    table = copy.deepcopy(desk)
    for i in range(len(table)):
        table[i][x] = "*"
    # добавляю по горизонтали
    for i in range(len(table)):
        table[y][i] = "*"
    # ячейка слева
    if x > 0:
        table[y][x - 1] = "*"
        # ячейка справа
    if x < len(table) - 1:
        table[y][x + 1] = "*"
    # ячейка сверху
    if y > 0:
        table[y - 1][x] = "*"
    # ячейка снизу
    if y < len(table) - 1:
        table[y + 1][x] = "*"
    # слева-сверху
    if y > 0 and x > 0:
        table[y - 1][x - 1] = "*"
    # справа-сверху
    if y > 0 and x < len(table) - 1:
        table[y - 1][x + 1] = "*"
    # слева-снизу
    if y < len(table) - 1 and x > 0:
        table[y + 1][x - 1] = "*"
    # справа-снизу
    if y < len(table) - 1 and x < len(table) - 1:
        table[y + 1][x + 1] = "*"
    table[y][x] = "#"
    return table

"""for e in matrix:
    print(e)"""

output = open("output.txt", mode="w+", encoding="utf-8")
inpt = open("input.txt", mode="r+", encoding="utf-8")

lines = inpt.readlines() # считали строки
lines = [e.strip("\n" ).split(" ") for e in lines] # Сформатировали строки

figures = []
s = int(lines[0][0]) # размечикс
c = int(lines[0][1]) # скок надо поставить
for e in lines[1:]:
    figures.append((int(e[0]), int(e[1])))
matrix = [["0" for _ in range(s)] for _ in range(s)]

for e in figures:
    matrix = ultra_mega_king_dragon_figure(e[0], e[1], matrix)

inpt.close()
def rec(desk: list, figur_lst: list, n, x_now, y_now):
    if n == 0:
        print(*figur_lst, file=output)
        return
    new_figurs = list()
    i = y_now
    j = x_now
    while True:
        if i == len(desk)-1 and j == len(desk)-1:
            break
        if j == len(desk)-1:
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
        rec(desk, figur_lst + [e], n - 1, e[0], e[1])

rec(matrix, figures, c, -1, 0)
output.close()
output = open("output.txt", mode="r+", encoding="utf-8")

lines = output.readlines()
output.close()
"""
output = open("output.txt", mode="w+", encoding="utf-8")
for i in range(len(lines)):
        lines[i] = lines[i][:-2]
        output.write(lines[i] + "\n")
"""
output = open("output.txt", mode="r+", encoding="utf-8")

lines = output.readline().replace("(", "").replace(")", "").replace(",", "").split(" ") # считали строки
#lines.pop(-1)
print(lines)

matrix_to = [["0" for _ in range(s)] for _ in range(s)]
for i in range(0, len(lines), 2):
    matrix_to = ultra_mega_king_dragon_figure(int(lines[i]), int(lines[i+1]), matrix_to)

output.close()

for e in matrix_to:
    print(e)

end = time.time() - start
print(end)
# ура победа...