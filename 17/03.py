example_list = [1, 5, 8, 4, 6, 9, 21, -6]
print(id(example_list)) #id списка

sort_list = sorted(example_list) # создается новый отсортированный список со своим id
example_list.sort() # id остается прежним, список сортируется

print(sort_list, id(sort_list)) #sorted(), id
print(example_list, id(example_list)) #.sort, id
