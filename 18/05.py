scoring = {
    "Яблочко": 50,
    "Зеленое_кольцо": 25,
    "Внешнее_кольцо": {1: 8, 2: 6, 3: 42, 20: 50},
    "Внутреннее_кольцо": {1: 2, 2: 9, 3: 56, 20: 3}
}
def score(point, sector=None):
    if  point== "Яблочко" or point == "Зеленое_кольцо":
        return scoring[point]
    else:
        return scoring[point][sector]


print(score("Яблочко"))
print(score("Внешнее_кольцо", 1))
