def main():
    #matrix = [[1, 2, 3],
    #          [4, 5, 6],
    #          [7, 8, 9]]

    matrix = [[1,2,3,4],
              [5,6,7,8],
              [9,10,11,12]]

    top, bot, right, left = 0, len(matrix) - 1, len(matrix[0]) - 1, 0

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