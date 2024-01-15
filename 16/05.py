friends_dict = dict()

def add_friends(name_of_person, list_of_friends):
    global friends_dict
    if name_of_person not in friends_dict:
        friends_dict[name_of_person] = list_of_friends
    else:
        friends_dict[name_of_person].extend(list_of_friends)


def are_friends(name_of_person1, name_of_person2):
    if name_of_person2 in friends_dict[name_of_person1]:
        return True
    else:
        return False


def print_friends(name_of_person):
    global friends_dict
    print(*sorted(friends_dict[name_of_person]))
