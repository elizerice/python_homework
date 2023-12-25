import random


def make_bingo():
    bingo_matrix = list()
    for i in range(1, 6):
        bingo_list = list()
        for j in range(1, 6):
            rand = random.randint(1, 76)
            bingo_list.append(rand)
        bingo_matrix.append(bingo_list)
    bingo_matrix[2][2] = 0
    bingo_tuple = tuple(tuple(u) for u in bingo_matrix)
    return tuple(bingo_tuple)
print(make_bingo())
