def main():
    stroka, kolvo = str(input()).split(",")
    kolvo = int(kolvo)

    fe = kolvo

    fstroka = ""

    for i in range(2, kolvo):
        fe += 1
    #print("fe: ", fe)

    for f in range(0, kolvo):
        stp = fe - f * 2
        if (stp == 0):
            stp = fe
        j = f
        while (j < len(stroka)):
            if kolvo % 2 == 0:
                fstroka += stroka[j]
                if (j + stp < len(stroka)) and (stp != fe):
                    fstroka += stroka[j + stp]
                j += fe
            else:
                fstroka += stroka[j]
                j += stp
                print("j", j)

    print(fstroka)

if __name__ == "__main__":
    main()