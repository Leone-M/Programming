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

![Результат 1](![image](https://user-images.githubusercontent.com/77213122/194323448-3599ba00-c346-401b-a1d1-efaeeff0a698.png)
)
