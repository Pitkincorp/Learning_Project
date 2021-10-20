size = int(input("Введите длину матрицы: "))
matrix = [[1] * size] + [[0] * (size - 1) + [1] for i in range(size - 2)] + [[1] * size]

row = size - 1
col = 0
d_row = -1
d_col = 0
count = 0
while not matrix[row + 2 * d_row][col + 2 * d_col] and count != 1:
    count = 0
    while True:
        if not matrix[row + 2 * d_row][col + 2 * d_col]:
            row += d_row
            col += d_col
            matrix[row][col] = 1
            count += 1
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

