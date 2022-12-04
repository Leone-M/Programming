# Programming

## 7 лекция

### 1 задание

#### Вы хотите ограбить банки вдоль улицы, которые идут подряд. В каждом банке есть сейф, 
#### в котором лежим определенная сумма денег ( в миллионах рублей).
#### Так же в каждом банке есть система защиты,
#### которая сработает если были ограблены два ближайших банка. 
#### На вход поступает количество банков на улице.
#### Далее пользователь вводит (по мере их расположения): название банка и сумма денег в сейфе. 
#### Вам необходимо вернуть максимальную сумму денег,  которую вы можете получить
#### (так чтобы не сработала сигнализация), название банков и их порядковые номера на улице.
```Python
def main():
    n = int(input("Amount of banks: "))
    names = tuple(map(str, input("Names of banks: ").split(",")))
    b_summs = tuple(map(int, input("Banks summ: ").split(",")))
    street = list()
    route = []
    indexes = []
    max_sum = []

    for i in range(n):
        street.append((names[i], i + 1, b_summs[i]))

    max_sum.append([street[0][2],[street[0][1]]])
    if street[1][2] > street[0][2]:
        max_sum.append([street[1][2],[street[1][1]]])
    else:
        max_sum.append([street[0][2],[street[0][1]]])
    
    for i in range(2, len(street)):
        if max_sum[i-1][0] > max_sum[i-2][0] + street[i][2]:
            max_sum.append([max_sum[i-1][0], max_sum[i-1][1]])
        else:
            max_sum.append([max_sum[i-2][0] + street[i][2], max_sum[i-2][1] + [street[i][1]]])
     
    indexes = max_sum[-1][1]
    
    for e in indexes:
        route.append(street[e - 1][0])
    
    print("bank sum: ", max_sum[-1][0])
    print("indexes: ", *indexes)
    print("route: ", *route)

if __name__ == "__main__":
    main()
```
![image](https://user-images.githubusercontent.com/77213122/200287407-8f2e1b87-c7c3-4ecc-9a79-e6f2f88d5b8e.png)
![image](https://user-images.githubusercontent.com/77213122/200287470-c143f9db-4f60-4918-b4de-425c803e09f5.png)
![image](https://user-images.githubusercontent.com/77213122/200287848-64507f13-0036-4e35-8b0e-75e373b9b0df.png)

### 2 задание

#### Повернуть матрицу по часовой стрелке
```Python
def main():
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    for i in range(len(matrix)):
        for j in range(i, len(matrix[i])):
            matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]

    for j in range(len(matrix)):
        matrix[j] = matrix[j][::-1]

    print(*matrix, sep="\n")

if __name__ == "__main__":
    main()
```
![image](https://user-images.githubusercontent.com/77213122/200288349-0b76cbf2-65d9-4b15-9d4e-12f7f5224253.png)

### 3 задание

#### Спиралью вывести элементы матрицы
```Python
def main():
    #matrix = [[1, 2, 3],
    #          [4, 5, 6],
    #          [7, 8, 9]]

    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]]
    
    print("in: ", *matrix, sep = "\n")

    top, bot, right, left = 0, len(matrix) - 1, len(matrix[0]) - 1, 0

    print("\nout: ")
    while top <= bot and left < right:
        for i in range(left, right + 1):
            print(matrix[top][i])
        top += 1

        for i in range(top, bot + 1):
            print(matrix[i][right])

        right -= 1

        for i in range(right, left-1, -1):
            if abs(right - (left-1)) != 1:
                print(matrix[bot][i])
        bot -= 1

        for i in range(bot, top-1, -1):
            print(matrix[i][left])
        left += 1

if __name__ == "__main__":
    main()
```
![image](https://user-images.githubusercontent.com/77213122/200289108-669747e4-c9fd-475a-ac08-faf4efb49e6b.png)
