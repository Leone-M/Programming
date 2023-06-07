import tkinter as tk
import figure
import pygame

class Input_Data_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Input")

        # Ставим лейбл на ввод n потом ентри n потом лейбл на ошибку по n
        self.n_label = tk.Label(self, text="n - размер поля")
        self.n_label.pack(anchor="nw", padx=4)

        self.n_input = tk.Entry(self, validate="key", validatecommand=(self.register(self.check_n), "%P"))
        self.n_input.pack(anchor="nw", padx=5)

        self.n_err_msg = tk.StringVar()
        self.n_err_label = tk.Label(self, textvariable=self.n_err_msg, foreground="red", wraplength=130)
        self.n_err_label.pack(anchor="nw", padx=4)

        # Ставим лейбл на ввод l потом ентри l потом лейбл на ошибку по l
        self.l_label = tk.Label(self, text="l - количество фигур на поле")
        self.l_label.pack(anchor="nw", padx=4)

        self.l_input = tk.Entry(self, validate="key", validatecommand=(self.register(self.check_l), "%P"))
        self.l_input.pack(anchor="nw", padx=5)

        self.l_err_msg = tk.StringVar()
        self.l_err_label = tk.Label(self, textvariable=self.l_err_msg, foreground="red", wraplength=130)
        self.l_err_label.pack(anchor="nw", padx=4)

        # Ставим лейбл на ввод K потом ентри k потом лейбл на ошибку по k
        self.k_label = tk.Label(self, text="k - количество фигур для расстановки")
        self.k_label.pack(anchor="nw", padx=4)

        self.k_input = tk.Entry(self, validate="key", validatecommand=(self.register(self.check_k), "%P"))
        self.k_input.pack(anchor="nw", padx=5)

        self.k_err_msg = tk.StringVar()
        self.k_err_label = tk.Label(self, textvariable=self.k_err_msg, foreground="red", wraplength=130)
        self.k_err_label.pack(anchor="nw", padx=4)

        self.button = tk.Button(self, text="Поехали!")
        self.button["command"] = self.open_next_window
        self.button.pack()
        self.mainloop()

    def check_n(self, entry: str) -> bool:
        if (entry.isnumeric() and int(entry) <= 20) or entry == "":
            self.n_err_msg.set("")
            return True
        elif entry.isnumeric() and int(entry) > 20:
            self.n_err_msg.set("Размер поля - число не больше 20")
            return False
        elif "-" in entry:
            self.n_err_msg.set("Не может быть отрицательным")
            return False
        elif not entry.isnumeric():
            self.n_err_msg.set("Значение должно быть числом")
            return False

    def check_l(self, entry: str) -> bool:
        try:
            if (entry.isnumeric() and int(entry) <= int(self.n_input.get())**2) or entry == "":
                self.l_err_msg.set("")
                return True
            elif "-" in entry:
                self.l_err_msg.set("Не может быть отрицательным")
                return False
            elif entry.isnumeric() and int(entry) > int(self.n_input.get())**2:
                self.l_err_msg.set("Количество фигур не может быть больше количества клеток")
                return False
            elif not entry.isnumeric():
                self.l_err_msg.set("Значение должно быть числом")
                return False
        except ValueError:
            self.l_err_msg.set("Размер доски не указан")
            return False

    def check_k(self, entry: str) -> bool:
        try:
            if (entry.isnumeric() and int(entry) <= int(self.n_input.get())**2) or entry == "":
                self.k_err_msg.set("")
                return True
            elif "-" in entry:
                self.k_err_msg.set("Не может быть отрицательным")
                return False
            elif entry.isnumeric() and int(entry) > int(self.n_input.get())**2:
                self.k_err_msg.set("Количество фигур не может быть больше количества клеток")
                return False
            elif not entry.isnumeric():
                self.k_err_msg.set("Значение должно быть числом")
                return False
        except ValueError:
            self.k_err_msg.set("Размер доски не указан")
            return False

    def open_next_window(self):
        if self.n_input.get() == "":
            self.n_err_msg.set("Не может быть пустым")
        elif self.l_input.get() == "":
            self.l_err_msg.set("Не может быть пустым")
        elif self.k_input.get() == "":
            self.k_err_msg.set("Не может быть пустым")
        elif (self.n_input.get() != "" and self.l_input.get() != "" and self.k_input.get() != "") and (self.check_n(self.n_input.get()) and
                                                                        self.check_l(self.l_input.get()) and self.check_k(self.k_input.get())):
            n, l, k = int(self.n_input.get()),  int(self.l_input.get()), int(self.k_input.get())
            self.destroy()
            Place_Figures_window(n, l, k)





class Place_Figures_window(tk.Tk):
    def __init__(self, n, l, k):
        super(Place_Figures_window, self).__init__()
        self.entries = []
        self.maxsize(400, 400)
        self.n = n
        self.l = l
        self.k = k
        self.fig = figure.King_Dragon()

        # Создаю Canvas чтобы можно было скроллить и фрейм в котором будут поля ввода
        self.canvas = tk.Canvas()
        self.canvas.pack(anchor="nw", expand=1)

        # Создаю лейбл и текст о неправильных координатах
        self.err_msg = tk.StringVar()
        self.err_label = tk.Label(textvariable=self.err_msg, foreground="red", wraplength=175)
        self.err_label.place(rely=0.75, relx=0.35)

        # Важная пометка: чтобы скроллить по канвазу нужно чтобы фрейм был больше канваза, как следствие нужно чтобы
        # высота менялась в зависимости от кол-ва фигур
        self.frame = tk.Frame(master=self.canvas, height=50*l)

        # Цикл создающий l лейблов и ентриев с принадлежностью к фрейму, упаковываю при создании
        for i in range(1, l+1):
            tk.Label(self.frame, text=f"Фигура {i}").pack()
            self.entries.append(tk.Entry(self.frame, validate="key", validatecommand=(self.register(self.check_coords),"%P")))
            self.entries[i-1].pack()

        # Фрейм упаковывать не надо он сразу как виджет отправляется в канваз
        self.canvas.create_window(10, 10, anchor="nw", window=self.frame)

        # Создаю скроллбар и ставлю его в окне
        self.scroll = tk.Scrollbar(orient=tk.VERTICAL , command=self.canvas.yview)
        self.scroll.place(relheight=0.9, width=15, relx=0.9, rely=0.1)

        # В канвазе настраиваем скролл и присваиваем команду скролинга недавно созданому виджету
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.canvas["yscrollcommand"] = self.scroll.set

        # Кнопка запуска алгоритма
        self.run_button = tk.Button(text="Запустить алгоритм", command=self.open_next_window)
        self.run_button.place(rely=0.9, relx=0.35)

        self.mainloop()

    def check_coords(self, coords: str) -> bool:
        chrs = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]
        space_count = coords.count(" ") # кол-во пробелов


        for chr in coords:
            if chr not in chrs: # правильность символа
                self.err_msg.set("Неправильный символ")
                return False
        self.err_msg.set("")
        return True

    def check_atck(self, coord: tuple[int], all_coords: list[tuple[int]], top_limit: int) -> bool:

        matrix = [["0" for _ in range(int(self.n))] for _ in range(int(self.n))]
        self.fig = figure.King_Dragon()
        for i in range(top_limit):
            matrix = self.fig.place(all_coords[i][0], all_coords[i][1], matrix)

        return figure.King_Dragon().check_place(coord[0], coord[1], matrix)

    def setting_up(self, coords): # подготавливаю матрицу для отображения на доске в следующем окне и файлы для чтения
        desk = [["0" for _ in range(self.n)] for _ in range(self.n)]
        input = open("input.txt", "w+", encoding="utf-8")
        print(type(coords[0]))

        # записываем начальные данные n l k
        input.write(f"{self.n} ")
        input.write(f"{self.k} ")
        input.write(f"{self.l}\n")

        for c in coords: # записыванные координаты меняют матрицу через класс фигуры
            desk = self.fig.place(int(c[0]), int(c[1]), desk)
            for i in c: # попутно записываем координта в файл
                input.write(str(i+1) + " ") # с+1 т.к. в программе индексы с 0, а в файле с 1
            input.write("\n") # переводим каретку на след. строчку и там запишутся другие координаты
        input.close()
        return desk

    def open_next_window(self):
        entries = [entry.get() for entry in self.entries]
        frmted_coords = ["" for _ in range(len(entries))]

        i = 0
        right = True
        for coords in entries:
            coords = coords.strip()

            try:
                space = coords.index(" ")
            except:
                self.err_msg.set(f"Фигура {i+1} имеет неправильные координаты")
                right = False
                break
            x = coords[:space]
            y = coords[space + 1:]

            if not x.isdigit() or not y.isdigit(): # если переменные оказываются не числами то строка неправтльная
                self.err_msg.set(f"Фигура {i+1} имеет неправильные координаты")
                right = False
                break

            if not self.check_coords(coords):
                right = False

            if int(x) > self.n:
                self.err_msg.set("Координаты не могут быть больше доски")
                right = False
            elif int(y) > self.n:
                self.err_msg.set("Координаты не могут быть больше доски")
                right = False

            if not self.check_atck((int(x) - 1, int(y) - 1), frmted_coords, i):
                self.err_msg.set(f"Фигура {i+1} находится под боем")
                right = False

            frmted_coords[i] = (int(x) - 1, int(y) - 1)
            i += 1

        not_repeat = True
        for a in frmted_coords:
            for b in frmted_coords[frmted_coords.index(a)+1:]:
                if a == b:
                    self.err_msg.set("Координаты не могут повторятся")
                    not_repeat = False

        if right and not_repeat:
            self.destroy()
            matrix_to_show = self.setting_up(frmted_coords) # мне возвращается матрица с расставленными фигурами
            Board(self.n, self.l, self.k, matrix_to_show)





class Board:
    def __init__(self, n, l, k, matrix):
        pygame.font.init()
        pygame.display.init()
        self.n = n
        self.l = l
        self.k = k

        pygame.init()
        self.resolution = (720, 768)
        self.screen = pygame.display.set_mode(self.resolution)
        pygame.display.set_caption("Solution")
        self.clock = pygame.time.Clock()
        self.matrix = matrix
        self.fig = figure.King_Dragon()
        self.font = pygame.font.Font(None, size=20)


        # главное не перебарщивать со скоростью
        self.clock.tick(60)
        
        self.matrix = self.solution("single_oop")
        if self.matrix != ["0_0"]:
            self.draw()
        else:
            self.no_solution()


        self.run()

    def solution(self, method: str):
        if method == "single_oop":
            c = 0 # figures placed
            i = 0 # y
            j = 0 # x
            while c < self.k: # так как ищем одно решние для отображения, можно пробежать циклом while
                if self.fig.check_place(j, i, self.matrix):
                    self.matrix = self.fig.place(j, i, self.matrix)
                    c += 1
                if i == self.n - 1 and j == self.n - 1:
                    break
                if j == self.n - 1:
                    i += 1
                    j = 0
                else:
                    j += 1
            if c < self.k: return ["0_0"]
            return self.matrix
        elif method == "full_algorithm": # большая подготовка перед большой рекурсией
            inpt = open("input.txt", "r+", encoding="utf-8")
            out = open("output.txt", "w+", encoding="utf-8")
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

            self.rec(matrix, figures, c, -1, 0, out)
            out.close()
            out = open("output.txt", mode="r+", encoding="utf-8")

            lines = out.readlines()
            if lines == []:
                print("No solution", file=out)
                out.close()
            else:
                out.close()
                out = open("output.txt", mode="r+", encoding="utf-8")

                lines = out.readline().replace("(", "").replace(")", "").replace(",", "").split(" ") # считали строки

                matrix_to = [["0" for _ in range(s)] for _ in range(s)]
                for i in range(0, len(lines), 2):
                    matrix_to = fig.place(int(lines[i]), int(lines[i+1]), matrix_to)

                out.close()

                for e in matrix_to: # единичный вывод в консоль
                    print(e)



    def run(self):
        run = True
        while run:
            mouse_pos = pygame.mouse.get_pos()

            for event in pygame.event.get():
                # закрытие окна
                if event.type == pygame.QUIT:
                    run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if 600 <= mouse_pos[0] <= 600 + 100 and 733 <= mouse_pos[1] <= 733 + 20:
                        self.solution(method="full_algorithm")
            pygame.display.flip()

    def draw(self):
        # Создаю легенду

        figs_text = self.font.render("Желтый - фигура", 1, "Yellow")
        self.screen.blit(figs_text, (30, 740))

        slot_text = self.font.render("Серый - пустая ячейка", 1, "Grey")
        self.screen.blit(slot_text, (150, 740))

        atck_text = self.font.render("Красный - ячейка под атакой", 1, "Red")
        self.screen.blit(atck_text, (305, 740))

        # создаю кнопку и текст для полного алгоритма с записью в файл
        full_algorithm_button = pygame.draw.rect(self.screen, "Magenta", (600,733, 100, 20))

        full_algorithm_text = self.font.render("GO!", 1, "White")
        self.screen.blit(full_algorithm_text, (640, 736))

        size = 720 / self.n # размер ячеек
        cy = 0 # врубаю счетчик чтобы располагать ячейки по y
        for y in self.matrix:
            cx = 0 # врубаю счетчик чтобы располагать ячейки по x
            for x in y:
                if self.matrix[cy][cx] == "0":
                    drawrect = pygame.draw.rect(self.screen, "Grey", (cx*size, cy*size, size-2, size-2))
                if self.matrix[cy][cx] == "*":
                    drawrect = pygame.draw.rect(self.screen, "Red", (cx * size, cy * size, size-2, size-2))
                if self.matrix[cy][cx] == "#":
                    drawrect = pygame.draw.rect(self.screen, "Yellow", (cx * size, cy * size, size-2, size-2))
                cx += 1
            cy += 1

    def no_solution(self):
        self.font = pygame.font.Font(None, size=60)
        no_solution = self.font.render("No solution", 1, "Red")
        self.screen.blit(no_solution, (260, 360))

    def rec(self, desk: list, figur_lst: list, n, x_now, y_now, output):
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
        for e in new_figurs:
            self.rec(desk, figur_lst + [e], n - 1, e[0], e[1], output)