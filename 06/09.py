freezer = set()
yes_recipe = set()
for i in range(int(input('продуктов в холодильнике:'))):
    freezer.add(input())
for i in range(int(input('рецептов:'))):
    recipe_name = input('имя рецепта:')
    recipe_food = set()
    for j in range(int(input('ингридиентов:'))):
        food = input()
        recipe_food.add(food)
    if recipe_food <= freezer:
        yes_recipe.add(recipe_name)
for i in yes_recipe:
        print(i)
