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
