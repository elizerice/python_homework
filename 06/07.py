people = set()
good_people = set()
sum_lists = int(input())

for i in range(sum_lists):
    pepl_sum = int(input())
    now_pepl = set()

    for i in range(pepl_sum):
        person = str(input())
        now_pepl.add(person)
    good_people = good_people.intersection(now_pepl) if len(good_people) > 0 else now_pepl
    people.update(now_pepl)
  
for person in good_people:
    print(person)

