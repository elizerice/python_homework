list_1 = set()
list_2 = set()
num = input()
while num:
    list_1.add(int(num))
    num = input()
num = input()
while num:
    list_2.add(int(num))
    num = input()
intersection = list_1.intersection(list_2)
print(intersection)
    
