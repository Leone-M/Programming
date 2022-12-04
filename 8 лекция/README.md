# Programming

## 8 лекция

### 1 задание

#### Функция получает два списка. В каждом списке не должно быть дубликатов.
#### Функция возвращает:
#### 1) Количество элементов, присутствующих в обоих списках
#### 2) Количество элементов, присутствующих только в одном списке
#### 3) Количество оставшихся элементов в list1 после извлечения элементов из list2
#### 4) Количество оставшихся элементов в list2 после извлечения элементов из list1
```Python
def main():
    list1, list2 = [0, 33, 37, 6, 10, 44, 13, 47, 16, 18, 22, 25], [1, 38, 48, 8, 41, 7, 12, 47, 16, 40, 20, 23, 25]

    set1, set2 = set(list1), set(list2)

    ans1 = list(set1.intersection(set2))
    ans2 = list(set1.symmetric_difference(set2))
    ans3 = list(set1.difference(set2))
    ans4 = list(set2.difference(set1))

    print(ans1)
    print(ans2)
    print(ans3)
    print(ans4)

if __name__ == "__main__":
    main()
```
![image](https://user-images.githubusercontent.com/77213122/200289654-97a1fda2-16e8-4c2d-9e35-14a4d6610388.png)

### 2 задание

#### Функция получает список элементов. Любой элемент может встречаться более одного раза.
#### Вернуть количество подмножеств, не содержащих повторяющихся элементов, не включая пустое множество. И сами подмножества.
```Python
def main():
    lst = [1, 2, 3, 4]
    print("in: %s" % lst)

    # избавляюсь от повторений с помощью множеств
    lst = set(lst)
    lst = list(lst)

    buf = [[]]

    # т.к. повторения уже убраны списки получаются уникальными
    for e in lst:
        for i in range(len(buf)):
            tmp = buf[i] + [e]
            buf.append(tmp)

    # убираю рабочий список требуемый для первых итераций for i
    buf.pop(0)

    print("out: %s" % buf)
    print("len: %i" % len(buf))

if __name__ == "__main__":
    main()
```
![image](https://user-images.githubusercontent.com/77213122/200289879-05601472-cd07-4519-9c7e-bbb4f38278dc.png)
![image](https://user-images.githubusercontent.com/77213122/200289962-9aaf4a79-c4d2-44aa-90d9-d731e3ff713b.png)
![image](https://user-images.githubusercontent.com/77213122/200290165-29fa4da6-7a43-47fb-b451-0caf26898676.png)

