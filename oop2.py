from pprint import  pprint


def dish_recipes():
    with open('cook_book.txt', encoding='utf-8') as file:
        cook_book = {}
        for line in file:
            dish_name = line.strip()
            ingredients_count = int(file.readline())
            ingredients = []
            for _ in range(ingredients_count):
                name, quantity, measure = file.readline().strip().split(' | ')
                ingredients.append({'name': name, 'quantity': quantity, 'measure': measure})
            file.readline()
            cook_book[dish_name] = ingredients
    file.close()
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredient = {}
    for dish in dishes:
        for i in range(len(dish_recipes()[dish])):
            name, quantity, measure = dish_recipes()[dish][i].values()
            if name not in ingredient:
                ingredient[name] = {'measure': measure, 'quantity': int(quantity) * person_count}
            else:
                ingredient[name]['quantity'] += int(quantity) * person_count
    pprint(ingredient)

