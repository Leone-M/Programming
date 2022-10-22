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