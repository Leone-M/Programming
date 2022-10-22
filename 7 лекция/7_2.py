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