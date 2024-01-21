from random import choice
import sys
people = []
for line in sys.stdin:
    people.append(line.split())


def secret_friend(friends_list):
    persons = friends_list.copy()
    for i in friends_list:
        rand_pers = choice(persons)
        while rand_pers == i:
            rand_pers = choice(persons)
        else:
            print(*i, '-', *rand_pers)
            persons.remove(rand_pers)


secret_friend(people)
