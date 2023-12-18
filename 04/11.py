sum_people = int(input())
sum_iq = 0
person_count = 0
for i in range(sum_people):
    person_iq = int(input())
    sum_iq += person_iq
    person_count += 1
    if sum_iq / person_count > person_iq:
        print('<')
    elif sum_iq / person_count < person_iq:
        print('>')
    else:
        print('0')
