recipe = list()
for i in range(int(input())):
    line = input()
    if 'лук' not in line:
        recipe.append(line)
print(*', '.join(recipe).split())
