friends = dict()
for _ in range(int(input())):
    name, day, month = input().split()
    if month in friends:
        friends[month]+= " " + name
    else:
        friends[month] = name
for i in range(int(input())):
    month = input()
    if month in friends:
        print(friends[month])
