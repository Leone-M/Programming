import abc

class Figure:
    @abc.abstractmethod
    def check_place(self, x, y, table):
        ...

    @abc.abstractmethod
    def place(self, x, y, table):
        ...

    @abc.abstractmethod
    def check_place_full(self, x, y, figr_lst) -> bool:
        for e in figr_lst:
            if (x == e[0] or y == e[1]) or (abs(x - e[0]) <= 1 and abs(y - e[1]) <= 1):
                return False

class King_Dragon(Figure):
    def check_place(self, x, y, table) -> bool:
        if table[y][x] == "#" or table[y][x] == "*": return False
        return True

    def place(self, x, y, table) -> list:
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
        # self.coords = (x, y)
        return table