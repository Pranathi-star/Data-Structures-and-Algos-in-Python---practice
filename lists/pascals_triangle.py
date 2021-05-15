def pascals(rows):
    matrix = [0]*rows
    for i in range(rows):
        matrix[i] = [0]*(i + 1)
        matrix[i][0], matrix[i][i] = 1, 1
        for j in range(1, i):
            matrix[i][j] = matrix[i - 1][j] + matrix[i - 1][j - 1]
    return matrix


rows = int(input().strip())
print(pascals(rows))
