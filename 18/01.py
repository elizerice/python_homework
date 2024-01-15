def matrix(m = 1, a = 0):
    matr = []
    for i in range(m):
        row = []
        for j in range(m):
            row.append(a)
        matr.append(row)
    return matr
