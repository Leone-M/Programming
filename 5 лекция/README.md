# Programming

## Задания с я не помню какая это по счету лекция, вроде вторая, а на файлах первая написано, а на деле пятая оказалась

### Первое задание:

#### 1. С клавиатуры поступает строка. Необходимо вывести самую
#### длинную подстроку без повторных символов.

```Python
def main():
    stringprep = str(input())
    stringfinal = ""
    buf = []
    mx = 0
    cur = 0

    for i in range(0, len(stringprep)):
        if not (stringprep[i] in buf):
            buf.append(stringprep[i])
            cur += 1
            if cur >= mx:
                stringfinal = ""
                for e in buf:
                    stringfinal += e
                mx = cur
        else:
            buf = []
            cur = 0

    print(stringfinal)

if __name__ == "__main__":
    main()
```

![Результат 1](https://user-images.githubusercontent.com/77213122/194324064-dab9ecd8-5f0e-4e4c-b4f2-9d1b3debc2d3.png)
![Результат 2](https://user-images.githubusercontent.com/77213122/194324963-c40cc0a7-e2e8-41dc-85cb-5fe1363f2476.png)
![Результат 3](https://user-images.githubusercontent.com/77213122/194325172-62f9ff01-272f-4e72-b721-a4ac0ec73673.png)

### Второе задание:

#### 2. С клавиатуры поступает строка. Необходимо вывести строку, где
#### порядок слов в противоположном направлении. Первое слово с
#### заглавной буквы, остальные с маленькой. МЕЖДУ словами только
#### ОДИН пробел.

```Python
def main():
    stroka = str(input()).split()
    stroka = stroka[::-1]
    for i in range(len(stroka)):
        stroka[i] = stroka[i].lower()
    stroka[0] = stroka[0].capitalize()
    print(" ".join(stroka))

if __name__ == "__main__":
    main()
```

![Result 1](https://user-images.githubusercontent.com/77213122/194328371-9ab59ac7-9fa3-4cf8-badc-c47d2f160cdb.png)
![Result 2](https://user-images.githubusercontent.com/77213122/194328559-b608c28c-ca09-47c5-907c-cd486ab7e799.png)
![Result 3](https://user-images.githubusercontent.com/77213122/194328639-0f8cc29e-1855-44c2-af04-7b3c43aa724c.png)

### Третье задание:

#### С клавиатуры поступает строка, которая имеет только символы: '(', ')', '{', '}', '[' и ‘]’.
#### Необходимо проверить правильно ли сформированы скобки. Если ВСЕ скобки сформированы правильно, то вывести True,
#### если нет, то вывести самую длинную правильно сформированную подстроку скобок, если такой подстроки нету,
#### то вывести False. (Сначала лучше сделать True и False, а потом работать с подстроками).

```Python
def main():
    stroka = str(input())

    i = 0
    allow_1 = 0
    allow_2 = 0
    allow_3 = 0

    podstroka = ""
    max_podstroka = ""
    maxx = 0

    while i != len(stroka):
        if stroka[i] == "(":
            allow_1 += 1
            podstroka += stroka[i]
        elif stroka[i] == "[":
            allow_2 += 1
            podstroka += stroka[i]
        elif stroka[i] == "{":
            allow_3 += 1
            podstroka += stroka[i]
        elif stroka[i] == ")" and allow_1 > 0 and not (stroka[i - 1] == "[" or stroka[i - 1] == "{"):
            podstroka += stroka[i]
            allow_1 -= 1
        elif stroka[i] == "]" and allow_2 > 0 and not (stroka[i - 1] == "(" or stroka[i - 1] == "{"):
            podstroka += stroka[i]
            allow_2 -= 1
        elif stroka[i] == "}" and allow_3 > 0 and not (stroka[i - 1] == "[" or stroka[i - 1] == "("):
            podstroka += stroka[i]
            allow_3 -= 1
        else:
            allow_1 = 0
            allow_2 = 0
            allow_3 = 0
            maxx = 0
            podstroka = ""

        if len(podstroka) > maxx and len(podstroka) != 1:
            maxx += 1
            max_podstroka = podstroka

        i += 1

    if max_podstroka == stroka:
        print(True)
    elif max_podstroka != "":
        print(max_podstroka)
    else:
        print(False)

if __name__ == "__main__":
    main()
```
![image](https://user-images.githubusercontent.com/77213122/197355387-a5943b84-9786-4d77-a237-d5e599a725c2.png)
![image](https://user-images.githubusercontent.com/77213122/197355500-37729460-fbb6-4aa7-b1dd-ae8cb3038559.png)
![image](https://user-images.githubusercontent.com/77213122/197355517-aa6a6157-026b-420f-adb1-7878310ae110.png)
![image](https://user-images.githubusercontent.com/77213122/197355542-e43b3da1-8628-4d74-b675-370f0501ddde.png)
![image](https://user-images.githubusercontent.com/77213122/197355554-1fb1bc62-da1d-4607-ab7c-5eaa550852d4.png)


