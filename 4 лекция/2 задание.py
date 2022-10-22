def main():
    numb =  int(input())
    if (numb > 127) or (numb < -128):
        print("no solution")
    else:
        numb = str(numb)
        if numb[0] == "-":
            numb = numb[1:]
            if numb[-1] == "0":
                numb = numb[1::-1]
            else:
                numb = numb[::-1]
            if int(numb) > 128:
                print("no solution")
            else:
                print("-" + numb)
        else:
            if numb[-1] == "0":
                numb = numb[1::-1]
            else:
                numb = numb[::-1]
            if int(numb) > 127:
                print("no solution")
            else:
                print(numb)



if __name__ == '__main__':
    main()