def find_mountain(a):
    max_height_list = list()
    for i in range(len(a)):
        max_height_list.append(max(a[i]))
    for i in range(len(a)):
        for j in range(len(a[i])):
            if max(max_height_list) == int(a[i][j]):
                row = i
                col = j
    return row, col
