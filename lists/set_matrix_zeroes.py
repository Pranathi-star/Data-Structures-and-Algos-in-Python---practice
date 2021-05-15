# if any of the matrix elements is 0, set all the elements in row and column of that element equal to 0
def set_zero(rows, cols, matrix):
    col0 = 1
    for i in range(0, rows):
        if matrix[i][0] == 0: col0 = 0
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0], matrix[0][j] = 0, 0
    for i in range(rows - 1, -1, -1):
        for j in range(cols - 1, 0, -1):
            if matrix[0][j] == 0 or matrix[i][0] == 0:
                matrix[i][j] = 0
        if col0 == 0: matrix[i][0] = 0
    return matrix




rows = int(input().strip())
matrix = []
for i in range(rows):
    matrix.append([int(i) for i in input().split()])
cols = len(matrix[0])
print(set_zero(rows, cols, matrix))
