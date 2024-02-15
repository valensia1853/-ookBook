import os.path
import os

def acounting(file:str) -> int:
    return sum(1 for _ in open('C:/Нетология/open_reader_file/1.txt', 'rt', encoding='utf-8'))

with open('C:/Нетология/Cookbook/recept.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        name = i.strip()
        count = file.readline()
        ingredients = []
        for p in range(int(count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        file.readline()
        cook_book[name] = ingredients

def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['product'] in result:
                    result[consist['product']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['product']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('Такого блюда нет в книге')
    print(result)
get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет'])