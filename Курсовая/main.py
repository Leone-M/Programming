import window_tk

output = open("output.txt", mode="w+", encoding="utf-8") # Глобальные переменные - файлы
inpt = open("input.txt", mode="r+", encoding="utf-8")


def main():
    window = window_tk.Input_Data_window()

if __name__ == '__main__':
    main()

