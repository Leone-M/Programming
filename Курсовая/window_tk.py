import tkinter as tk
import figure
import pygame
import algorithm

output = open("output.txt", mode="w+", encoding="utf-8") # Глобальные переменные - файлы
inpt = open("input.txt", mode="r+", encoding="utf-8")

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
        fig = figure.King_Dragon()

        matrix = [["0" for _ in range(int(self.n))] for _ in range(int(self.n))]
        fig = figure.King_Dragon()
        for i in range(top_limit):
            matrix = fig.place(all_coords[i][0], all_coords[i][1], matrix)

        return figure.King_Dragon().check_place(coord[0], coord[1], matrix)

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
            Board(self.n, self.l, self.k, frmted_coords)


class Board:
    def __init__(self, n, l, k, figs):
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
        self.matrix = algorithm.oop_algorithm(int(self.n), int(self.k), int(self.l), figs)
        self.font = pygame.font.Font(None, size=20)


        # главное не перебарщивать со скоростью
        self.clock.tick(60)
        if self.matrix != ["0_0"]:
            self.draw()
        else:
            self.no_solution()


        self.run()

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
                        algorithm.start_algorithm(output,inpt)
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




