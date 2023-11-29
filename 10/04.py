num = int(input())
_list = []
for i in range(num):
    _list.append(input())
for i in range(num):
    for i in range(num - 1):
        for j in range(num - 1 - i):
            if len(_list[j]) > len(_list[j + 1]):
                _list[j], _list[j + 1] = _list[j + 1], _list[j]
            if len(_list[j]) == len(_list[j + 1]):
                if _list[j] > _list[j + 1]:
                    _list[j], _list[j + 1] = _list[j + 1], _list[j]
for i in range(num):
    print(_list[i])
