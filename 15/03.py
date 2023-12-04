def take_large_banknotes(banknotes):
    bank_list = []
    for i in banknotes:
        if i > 10:
            bank_list.append(i)
    return bank_list
print(*take_large_banknotes([]))
print(*take_large_banknotes([1, 5, 500, 0.5, 2, 0.1, 10, 100, 100, 1000, 50]))
