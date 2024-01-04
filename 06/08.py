pers_sum = int(input())
repeat_list = set()
pers_list = set()
count = 0
for i in range(pers_sum):
    person = str(input())
    if person not in pers_list:
        pers_list.add(person)
        repeat_list.add(person)
    elif person in repeat_list:
        repeat_list.remove(person)
        count += 2
    else:
        count += 1
print(count)
