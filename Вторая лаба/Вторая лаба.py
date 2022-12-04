import copy


def main():
    file = open("input.txt", "r", encoding="utf-8")

    output = open("output.txt", "r+", encoding="utf-8")

    lines = file.readlines() # считали строки
    lines = [e.strip("\n" ).split(" ") for e in lines] # Сформатировали строки

    matrix_size = int(lines[0][0])
    matrix = []

    for i in range(matrix_size): # Создаю пустую доску
        matrix.append(list())
        for _ in range(matrix_size):
            matrix[i].append("0")


    print(lines)
    # for e in matrix: # Распечатываем начальную матрицу
    #     print(e)

    def ultra_mega_king_dragon_figure(x, y, table):
        if table[y][x] == "0":
            able_to = True
        else:
            able_to = False

        if able_to:
            # добавляю по вертикали
            for i in range(len(table)):
                table[i][x] = "*"
            # добавляю по горизонтали
            for i in range(len(table)):
                table[y][i] = "*"
            # ячейка слева
            if x > 0:
                table[y][x-1] = "*"
            # ячейка справа
            if x < len(table)-1:
                table[y][x+1] = "*"
            # ячейка сверху
            if y > 0:
                table[y-1][x] = "*"
            # ячейка снизу
            if y < len(table)-1:
                table[y+1][x] = "*"
            # слева-сверху
            if y > 0 and x > 0:
                table[y-1][x-1] = "*"
            # справа-сверху
            if y > 0 and x < len(table)-1:
                table[y-1][x+1] = "*"
            # слева-снизу
            if y < len(table)-1 and x > 0:
                table[y+1][x-1] = "*"
            # справа-снизу
            if y < len(table)-1 and x < len(table)-1:
                table[y+1][x+1] = "*"
            table[y][x] = "#"
            return True
        else:
            return False

    for i in range(1, int(lines[0][2]) + 1):  # Раставляем данные фигуры
        ultra_mega_king_dragon_figure(int(lines[i][0]), int(lines[i][1]), matrix)

    def recursion(n, table, x_now, y_now, c, out):
        if n == c:
            while True:
                my_table = copy.deepcopy(table)
                if x_now == len(table) and y_now == len(table) - 1:
                    break
                if x_now == len(table):
                    y_now += 1
                    x_now = 0
                ultra_mega_king_dragon_figure(x_now, y_now, my_table)
                x_now += 1

            print("\n")
            for e in my_table:
                print(e)

            figures = []
            for i in range(len(my_table)):
                for j in range(len(my_table)):
                    if my_table[i][j] == "#":
                        figures.append(tuple([j,i]))

            otv = ""
            for e in figures:
                otv += str(e)
                otv += " "
            otv.strip()

            out.write(otv + "\n")

        while True:
            my_table = copy.deepcopy(table)
            if x_now == len(table) and y_now == len(table)-1:
                break
            if x_now == len(table):
                y_now += 1
                x_now = 0
            if ultra_mega_king_dragon_figure(x_now, y_now, my_table):
                recursion(n+1, my_table, x_now, y_now, c, out)
            x_now += 1

    for e in matrix: # Начальная матрица
        print(e)

    recursion(0, matrix, 0, 0, int(lines[0][1]), output)

    file.close() # Обязательно
    output.close()
if __name__ == "__main__":
    main()