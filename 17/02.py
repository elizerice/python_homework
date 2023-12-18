def count_food(days):
    sum = 0
    for i in days:
        sum += daily_food[i - 1]
    return sum


daily_food = [0, 150, 150]
print(count_food([1]))

daily_food = [0, 150, 150]
print(count_food([2, 3]))
