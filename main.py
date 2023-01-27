from pprint import pprint
with open('cook_book.txt', 'rt',) as f:
    meal = {}
    for line in f:
        meal_name = line.strip()
        dish_count = int(f.readline())
        dish = []
        for i in range(dish_count):
            abc = f.readline()
            ingredient_name, quantity, measure = abc.split(" | ")
            dish.append({'ingredient_name': ingredient_name,  'quantity': quantity, 'measure': measure})
        f.readline()
        meal[meal_name] = dish
pprint(meal)
def get_shop_list_by_dishes(dishes, persons=int):
    print('Ознакомьтесь с Нашим меню :')
    pprint(meal)
    print()
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (meal[meal_name]):
                items_list = dict([(item['ingredient_name'], {'measure': item['measure'], 'quantity': int(item['quantity'])*persons})])
                if shopping_list.get(item['ingredient_name']):
                    extra_item = (int(shopping_list[item['ingredient_name']]['quantity']) +
                                  int(items_list[item['ingredient_name']]['quantity']))
                    shopping_list[item['ingredient_name']]['quantity'] = extra_item
                else:
                    shopping_list.update(items_list)
        print(f"Для приготовления блюд на {persons} человек  нам необходимо купить:")
        pprint(shopping_list)
    except KeyError:
        print("Вы ошиблись в названии блюда, проверьте ввод")
get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2)


