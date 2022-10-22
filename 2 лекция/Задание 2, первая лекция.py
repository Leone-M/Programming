def main():
    stroka = str(input()).split()
    stroka = stroka[::-1]
    for i in range(len(stroka)):
        stroka[i] = stroka[i].lower()
    stroka[0] = stroka[0].capitalize()
    print(" ".join(stroka))

if __name__ == "__main__":
    main()