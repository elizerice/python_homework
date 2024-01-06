yes_food = set()
day_food = set()
unic_food = yes_food

for i in range(int(input())):
    yes_food.add(input())

for days in range(int(input())):
    day_food.clear()
    for food in range(int(input())):
        day_food.add(input())
        unic_food -= day_food
print(unic_food)
