def main():
    # Start your code
    numb = list(map(str, input()))
    buf = []

    for i in range(len(numb) - 1, -1, -1):
        buf.append(numb[i])

    if (numb == buf):
        print(True)
    else:
        print(False)

    # End your code

if __name__ == '__main__':
    main()
