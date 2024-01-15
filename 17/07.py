def transpose(matrix):
    transpose_matrix = []
    for i in range(len(matrix[0])):
        line = []
        for j in range(len(matrix)):
            line.append(matrix[j][i])
        transpose_matrix.append(line)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] = transpose_matrix[i][j]
