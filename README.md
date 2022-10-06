# Programming

## Задания с первой лекции

### Первое задание:

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




