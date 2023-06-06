import tkinter as tk

class DynamicList(tk.Tk):
    def __init__(self):
        super().__init__()
        self.list_create = tk.Button(text="Создание списка", width=20, command=lambda: self.button_function("create_list"))
        self.list_print = tk.Button(text="Вывод в консоль", width=20, command=lambda: self.button_function("print_list"))
        self.list_write = tk.Button(text="Запись в файл", width=20, command=lambda: self.button_function("write_list"))
        self.list_len = tk.Button(text="Кол-во элементов", width=20, command=lambda: self.button_function("len_list"))
        self.list_append = tk.Button(text="Добавление элемента", width=20, command=lambda: self.button_function("add_list"))
        self.list_find = tk.Button(text="Поиск элемента", width=20, command=lambda: self.button_function("find_element"))
        self.list_delete = tk.Button(text="Удаление элемента", width=20, command=lambda: self.button_function("del_element"))
        self.exit = tk.Button(text="Выход", width=20, command=lambda: self.button_function("exit"))

        self.list_create.grid(row=0, column=0)
        self.list_print.grid(row=0, column=1)
        self.list_write.grid(row=1, column=0)
        self.list_len.grid(row=1, column=1)
        self.list_append.grid(row=2, column=0)
        self.list_find.grid(row=2, column=1)
        self.list_delete.grid(row=3, column=0)
        self.exit.grid(row=3, column=1)

    def button_function(self, method: str):
        if method == "create_list":
            self.create_list()
        elif method == "print_list":
            if self.validation():
                print(self.dynamic_list)
        elif method == "write_list":
            if self.validation():
                with open("List.txt", "w+") as file:
                    file.write(str(self.dynamic_list))
        elif method == "len_list":
            if self.validation():
                self.len_list()
        elif method == "add_list":
            if self.validation():
                self.list_add()
        elif method == "del_element":
            if self.validation():
                self.list_del()
        elif method == "find_element":
            if self.validation():
                self.find_element()
        elif method == "exit":
            self.destroy()

    def validation(self) -> bool:
        try:
            self.dynamic_list
            return True
        except AttributeError:
            print("Список ещё не создан")

    def create_list(self):
        window = tk.Toplevel()
        window.grab_set()
        
        label = tk.Label(master=window, text="Введите элементы списка через запятую")
        entry = tk.Entry(master=window)
        done = tk.Button(master=window, text="Закончить", command=lambda: entry_list(self, entry.get()))

        def entry_list(self, entry:str) -> list:
            l: list
            l = entry.split(",")
            while True:
                try:
                    l.remove("")
                except:
                    break
            for e in l:
                e = e.strip()
            
            if l != []:
                self.dynamic_list = l
            else:
                try:
                    delattr(self, "dynamic_list")
                except:
                    pass
            window.grab_release()
            window.destroy()

        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        done.grid(row=1, column=0, columnspan=2)

    def len_list(self):
        window = tk.Toplevel()
        window.grab_set()

        label_text = tk.StringVar(value=str(self.dynamic_list))

        label_list = tk.Label(master=window, textvariable=label_text)
        label_list.grid(row=0, column=0)

    def list_add(self):
        window = tk.Toplevel()
        window.grab_set()

        label = tk.Label(master=window, text="Добавление элемента")
        entry = tk.Entry(master=window)
        add_button = tk.Button(master=window, text="Добавить элемент", command=lambda: self.dynamic_list.append(entry.get()))
        exit_button = tk.Button(master=window, text="Закрыть", command=lambda: window.destroy())

        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        add_button.grid(row=1, column=0)
        exit_button.grid(row=1, column=1)

    def list_del(self):
        window = tk.Toplevel()
        window.grab_set()
        # я бы с радостью сделал отображение списка
        # в окне с удалением, но ткинтер не поддерживает изменяемый список
        # даже если variable юзать там треш показывается в label

        missing_element = tk.StringVar()

        del_label = tk.Label(master=window, text="Удалить элемент")
        del_label.grid(row=1, column=0)
        entry = tk.Entry(master=window)
        button = tk.Button(master=window, text="Удолить", command=lambda: remove(self, entry.get()))
        warn_label = tk.Label(master=window, textvariable=missing_element, foreground="red")

        entry.grid(row=1, column=2)
        button.grid(row=2, column=0, columnspan=2)
        warn_label.grid(row=3, column=0, columnspan=2)

        def remove(self, element):
            if element != "":
                try:
                    self.dynamic_list.remove(element)
                    missing_element.set("")
                except:
                    missing_element.set(f"Отсутсвует элемент {element} в списке")

    def find_element(self):
        window = tk.Toplevel()
        window.grab_set()

        find_element = tk.StringVar()

        label = tk.Label(master=window, text="Найти элемент")
        entry = tk.Entry(master=window)
        button = tk.Button(master=window, text="Найти", command=lambda: find(self, entry.get()))
        label_find = tk.Label(master=window, textvariable=find_element)

        label.grid(row=0, column=0)
        entry.grid(row=0, column=1)
        button.grid(row=1, column=0, columnspan=2)
        label_find.grid(row=2, column=0, columnspan=2)

        def find(self, element):
            if element != "":
                try:
                    find_element.set(f"Элемент найден на {self.dynamic_list.index(element) + 1} позиции")
                except:
                    find_element.set(f"Элемент {element} не найден в списке")
                
        
window = DynamicList()
tk.mainloop()