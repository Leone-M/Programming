import tkinter as tk
import abc



class Figure(abc.ABC):
    _name: str  # To show in tkinter submenu

    def __init__(self, *args) -> None:
        ...
    
    @abc.abstractmethod
    def draw(self, window) -> None: # to draw in tkinter window
        ...
    
    @abc.abstractmethod
    def square(self) -> int:
        ...



class Rectangle(Figure):
    _name = "Rectangle"

    def __init__(self, height, width) -> None:
        super().__init__()
        self.height = height
        self.width = width
    
    @property   # made it read-only cause i can
    def name(self):
        return self._name
    
    def square(self) -> int:
        return self.width * self.height
    
    def draw(self, window: tk.Toplevel) -> None:
        canvas = tk.Canvas(master=window)
        rect = canvas.create_rectangle(0,0,self.width, self.height, fill="Cyan")
        square = tk.StringVar(value=f"Square: {str(self.square())}")
        label = tk.Label(master=window, textvariable=square, width=50)
        label.grid(row=2, column=0, columnspan=3)
        canvas.grid(row=3, column=0, columnspan=3)
        
        
    


class Circle(Figure):
    _name = "Circle"

    def __init__(self, radius) -> None:
        super().__init__()
        self.radius = radius
    
    @property   # made it read-only cause i can
    def name(self):
        return self._name
    
    def square(self) -> int:
        return 3.14*self.radius**2
    
    def draw(self, window: tk.Toplevel) -> None:
        canvas = tk.Canvas(master=window)
        circle = canvas.create_oval(150-self.radius,150-self.radius,150+self.radius, 150+self.radius, fill="Cyan")
        square = tk.StringVar(value=f"Square: {str(self.square())}")
        label = tk.Label(master=window, textvariable=square, width=50)
        label.grid(row=1, column=0, columnspan=3)
        canvas.grid(row=2, column=0, columnspan=3)



class Triangle(Figure):
    _name = "Triangle"

    def __init__(self, side) -> None:
        super().__init__()
        self.side = side
    
    @property   # made it read-only cause i can
    def name(self):
        return self._name
    
    def square(self) -> int:
        return (self.side**2)/2
    
    def draw(self, window) -> None:
        canvas = tk.Canvas(master=window)
        x_0, y_0 = 0, 0
        x_1, y_1 = x_0, y_0 + self.side
        x_2, y_2 = x_1 + self.side, y_1
        x_3, y_3 = x_0, y_0
        points = [x_0, y_0, x_1, y_1, x_2, y_2, x_3, y_3]
        triangle = canvas.create_polygon(points, fill="Cyan")
        square = tk.StringVar(value=f"Square: {str(self.square())}")
        label = tk.Label(master=window, textvariable=square, width=50)
        label.grid(row=1, column=0, columnspan=3)
        canvas.grid(row=3, column=0, columnspan=3)
    


class Main_window(tk.Tk):
    def __init__(self):
        super().__init__()

        figures_available = [e._name for e in Figure.__subclasses__()]
        figures_available = tk.Variable(value=figures_available)
        list_of_figures = tk.Listbox(listvariable=figures_available, activestyle="dotbox", height=len(figures_available.get()), selectmode="SINGLE")
        list_of_figures.grid(row=0, column=0)

        go_button = tk.Button(text="Выбрать", command=lambda: self.entry_window(Figure.__subclasses__()[list_of_figures.curselection()[0]]))
        go_button.grid(row=0, column=1, sticky="N")
    
    def entry_window(self, figure: Figure):
        window = tk.Toplevel()
        window.grab_set()

        def validate(line: str):
            for e in line:
                if e not in "1234567890": return False
            return True

        if issubclass(figure, Rectangle):
            width_label = tk.Label(master=window, text="Width")
            width_entry = tk.Entry(master=window, validatecommand=(window.register(validate), "%P"), validate="all")

            height_label = tk.Label(master=window, text="Height")
            height_entry = tk.Entry(master=window, validatecommand=(window.register(validate), "%P"), validate="all")

            draw_button = tk.Button(master=window, text="Draw!", command=lambda: figure(int(height_entry.get()), int(width_entry.get())).draw(window))

            width_label.grid(row=0, column=0)
            width_entry.grid(row=0, column=1)
            height_label.grid(row=1, column=0)
            height_entry.grid(row=1, column=1)
            draw_button.grid(row=0, rowspan=2, column=2)

        if issubclass(figure, Circle):
            radius_label = tk.Label(master=window, text="Radius")
            radius_entry = tk.Entry(master=window, validatecommand=(window.register(validate), "%P"), validate="all")

            draw_button = tk.Button(master=window, text="Draw!", command=lambda: figure(int(radius_entry.get())).draw(window))

            radius_label.grid(row=0, column=0)
            radius_entry.grid(row=0, column=1)
            draw_button.grid(row=0, rowspan=1, column=2)

        if issubclass(figure, Triangle):
            first_label = tk.Label(master=window, text="Catets length")
            first_entry = tk.Entry(master=window, validatecommand=(window.register(validate), "%P"), validate="all")

            draw_button = tk.Button(master=window, text="Draw!", command=lambda: figure(int(first_entry.get())).draw(window))

            first_label.grid(row=0, column=0)
            first_entry.grid(row=0, column=1)
            draw_button.grid(row=0, rowspan=3, column=2)

        



window = Main_window()
tk.mainloop()