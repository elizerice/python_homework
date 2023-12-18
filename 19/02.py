def simple_map(transformation, values):
    result_list = list()
    for value in values:
        result_list.append(transformation(value))
    return result_list


values = [1, 3, 1, 5, 7]
print(*simple_map(lambda x: x + 5, values))
