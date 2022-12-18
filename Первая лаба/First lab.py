import _io

files = open("input(lab1).txt", "r", encoding="utf-8")  # Файл с входящими данными

sub = files.read().split(" ")  # Строка с данными

n = int(sub[0])  # Кол-во чисел
s = int(sub[-1])  # Целевое число
sub = sub[1:-1]  # Выделяем ряд чисел на вход
sim = [int(e) for e in sub]  # Вносим все числа в список в формате Int

files.close()  # Обязательно

def rec(arr: list, c: int, n: int, sum: int, signs: list, sign: str):
    if n == len(arr) - 1 and sum + arr[n] == c: # 1 из 3 базовых случаев
        signs[-1] = "+"
        return signs
    elif n == len(arr) - 1 and sum - arr[n] == c: # 2 из 3 базовых случаев
        signs[-1] = "-"
        return signs
    elif n == len(arr) - 1: # 3 из 3 базовых случаев
        signs[-1] = "*" # * будет знаком ложности
        return signs
    else:
        bf = rec(arr, c, n+1, sum + arr[n], signs, "+") # сумма с плюсом
        if bf[n+1] != "*": # проверяет получилась ли сумма если знак +
            signs = bf
            signs[n] = "+"
            return signs
        else:
            bf = rec(arr, c, n+1, sum - arr[n], signs, "-") # если знак -
            if bf[n+1] != "*":
                signs = bf
                signs[n] = "-"
                return signs
            else: # не получилась(
                signs = bf
                signs[n] = "*"
                return signs

zn = [0 for _ in range(n)]
zn = rec(sim, s, 0, 0, zn, "") # на выходе получается список со знаками

otv = ""
if "*" in zn:
    otv = "no solution" # если список забит знаками ложности - no solution
else: # иначе в переменную ответа записываем знак и его число
    for i in range(n):
        otv += zn[i]
        otv += str(sim[i])
    otv += "=%i" %s

# запись в файл
output = open("output(1lab).txt", "w", encoding="utf-8")
output.write(otv)
output.close() # обязательно