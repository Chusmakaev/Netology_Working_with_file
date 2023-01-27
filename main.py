import os
file_to_open = os.path.expanduser('cook_book.txt')
with open('cook_book.txt', 'rt',) as f:
    meal = {}
    for line in f:
        meal_name = line.strip()
        dish_count = int(f.readline())
        dish = []
        for i in range(dish_count):
            abc = f.readline().strip()
            ingredient_name, quantity, measure = abc.split(' | ')
            dish.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        f.readline()
        meal[meal_name] = dish
print(meal)
