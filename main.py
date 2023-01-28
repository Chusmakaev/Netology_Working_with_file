from pprint import pprint
def cookbook():
    with open('cook_book.txt', 'rt',) as f:
        meal = {}
        for line in f:
            dish_name = line[:-1]
            meal_name = line.strip()
            dish_count = int(f.readline())
            dish = []
            for i in range(int(dish_count)):
                dish_items = dict.fromkeys(['ingredient_name', 'quantity', 'measure']) # временный словарь
                ingridient = f.readline().strip().split(' | ') # перемещение по файлу
                for item in ingridient:
                    dish_items['ingredient_name'] = ingridient[0]
                    dish_items['quantity'] = ingridient[1]
                    dish_items['measure'] = ingridient[2]
                dish.append(dish_items)
                cook_book = {dish_name: dish}
                meal.update(cook_book)
            f.readline()
    return(meal)
pprint(cookbook())

def get_shop_list_by_dishes(dishes, persons=int):
    menu = (cookbook())
    print('Ознакомьтесь с Нашим меню :')
    pprint(cookbook())
    print()
    shopping_list = {}
    try:
        for dish in dishes:
            for item in (menu[dish]):
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


