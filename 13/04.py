coord_dict = dict()
for _ in range(int(input())):
    coordinates = input().split()
    coord_1 = int(coordinates[0])
    coord_2 = int(coordinates[1])

    if coord_1 // 10 != 0:
        coord_1 = coord_1 // 10
    if coord_2 // 10 != 0:
        coord_2 = coord_2 // 10

    coord_key = coord_1, coord_2
    if coord_key not in coord_dict:
        coord_dict[coord_key] = 1
    else:
        coord_dict[coord_key] += 1
print(max(coord_dict.values()))
