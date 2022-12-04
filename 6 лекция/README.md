# Programming

## 6 лекция

### 1 задание

#### Задается количество элементов в списке ( >4). Задается целочисленный список длины N. Задается цель. 
#### Необходимо найти сумму 4 чисел, которые равны цели или находятся близко к ней и вывести их.
```Python
def main():
    n = int(input("amount of nums: ")) #

    spisok = [] #изначальный список циферок
    perebor = [] #для брутфорса)

    # ввожу циферки
    for i in range(n):
        spisok.append(int(input("num: ")))

    # целевое значение
    c = int(input("point num: "))

    # ищу все возможные комбинации без повторов
    for i in range(len(spisok)):
        for j in range(i+1, len(spisok)):
            for d in range(j+1, len(spisok)):
                for f in range(d+1, len(spisok)):
                    buf = [spisok[i], spisok[j], spisok[d], spisok[f]]
                    perebor.append(buf)

    # задаю список для сумм от этих комбинаций
    celev = []

    # ищу суммы комбинаций
    for i in range(len(perebor)):
        k = 0
        for j in range(len(perebor[i])):
            k += perebor[i][j]
        celev.append(k)

    # ищу сумму с минимальным отклонением от целевого значения
    minim = 1000
    ii = 0
    for i in range(len(celev)):
        if abs(c - celev[i]) < minim:
            minim = abs(c - celev[i])
            ii = i

    # вывод
    print("numbers: ", perebor[ii], "\nsumm: ", celev[ii])


if __name__ == "__main__":
    main()
```
![image](https://user-images.githubusercontent.com/77213122/200284686-112efe27-ae16-49d3-b919-201e7eecea0e.png)
![image](https://user-images.githubusercontent.com/77213122/200284850-c6ea2364-bc98-44bc-ae8c-e5f88360b708.png)
![image](https://user-images.githubusercontent.com/77213122/200284985-b18f5284-738a-407f-98f2-b12479c76086.png)
![image](https://user-images.githubusercontent.com/77213122/200285127-03a79e87-468e-4647-9d26-6af9425eb1ce.png)

### 2 задание

#### Задается список целых чисел. Вывести список разделенный списками со всеми 
#### возможными уникальными перестановками целых чисел из заданного списка.

```Python
def main():
    arr = list(map(str, input().split(",")))
    perebor = []

    arr.sort()
    while True:
        perebor.append(list(arr))
        j = len(arr) - 2
        while j >= 0 and arr[j] >= arr[j + 1]:
            j -= 1
        if j < 0:
            break
        else:
            i = j + 1
            while i < len(arr) - 1 and arr[i + 1] > arr[j]:
                i += 1
            arr[i], arr[j] = arr[j], arr[i]
            arr[j + 1:] = arr[j + 1:][::-1]

    print(perebor)

if __name__ == "__main__":
    main()
```
![image](https://user-images.githubusercontent.com/77213122/200285558-9f9dd225-a41c-4756-8a25-0576a26240f6.png)
![image](https://user-images.githubusercontent.com/77213122/200285623-aee3628f-cbd8-4ba1-9b31-9814b6080d45.png)
![image](https://user-images.githubusercontent.com/77213122/200285682-86201ec9-daf6-49ac-9928-9ca5b89f01ed.png)

### 3 задание

#### Задается список строк.  Необходимо сгруппировать их в общий список по двум критериям:
#### 1) слова имеют одни и те же буквы
#### 2) слова одинаковой размерности

```Python
import itertools

def main():
    inp = str(input("Введите элементы списка через запятую: ")).replace(" ", "").split(",")
    out = {str(sorted(inp[0])) : [inp[0]]}
    j = 0
    
    for i in range(1, len(inp)):
        if str(sorted(inp[i])) in out:
            out[str(sorted(inp[i]))].append(inp[i])
        else:
            out[str(sorted(inp[i]))] = [inp[i]]
            
    out = [i for i in out.values()]
    print(out)

if __name__ == "__main__":
    main()
```
![image](https://user-images.githubusercontent.com/77213122/200286511-ef8e86cd-8fc1-49a4-af87-330d4e81fcfd.png)
![image](https://user-images.githubusercontent.com/77213122/200286674-d12526b0-1c40-40de-bb07-32b2d5aeb338.png)
