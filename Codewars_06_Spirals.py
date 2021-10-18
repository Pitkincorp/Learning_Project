n = int(input("Введите длину матрицы: "))
matrix = [[1] * n] + [[0]*(n-1)+[1] for i in range(n-2)] + [[1] * n]

row = n - 1
col = 0
d_row = -1
d_col = 0
while not matrix[row + 2 * d_row][col + 2 * d_col]:
    while True:
        if not matrix[row + 2 * d_row][col + 2 * d_col]:
            matrix[row][col] = 1
            row += d_row
            col += d_col
        else:
            if d_row == -1:
                d_row = 0
                d_col = 1
            elif d_col == 1:
                d_row = 1
                d_col = 0
            elif d_row == 1:
                d_row = 0
                d_col = -1
            else:
                d_row = -1
                d_col = 0
            break


        for i in matrix:
            print(i)
        print()
