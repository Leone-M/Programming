# Programming

## Задания с я не помню какая это по счету лекция

### Первое задание:

# 1. С клавиатуры поступает строка. Необходимо вывести самую
длинную подстроку без повторных символов.

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

# 2. С клавиатуры поступает строка. Необходимо вывести строку, где
порядок слов в противоположном направлении. Первое слово с
заглавной буквы, остальные с маленькой. МЕЖДУ словами только
ОДИН пробел.

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



