from pprint import pprint
import os #Вот это не очень поянтно

def get_cook_book():
# ну то есть вот тут def get_cook_book():
  path = os.path.join(os.getcwd(), 'recipes.txt') #И вот это тоже, брал из лекции
  with open(path, encoding="utf-8") as file: #Читаем файл, можно добавить и в функцию| Не получилось
      cook_book = {}
      for book in file:
          dish_name = book.strip()  # Название блюда
          am_ingredients = int(file.readline().strip())  # количество ингредиентов
          temp_data = []
          for items in range(am_ingredients):  # Проход по колличеству ингредиентов
              ingredient_name, quantity, measure = file.readline().strip('\n').split(' | ')  # Вот как это работает не очень понимаю
              a = {'ingredient_name': ingredient_name, 'quantity': int(quantity),
                  'measure': measure}  # Переменная с ключами и значениями
              temp_data.append(a)  # Добавление занчений блюд в список
          cook_book[dish_name] = temp_data  # Списки всех ингредиетов
          file.readline()  # Сделал как в уроке "?"
      # На выходе получаем словарь
      #pprint(cook_book)
      # print(cook_book)
  return cook_book

def get_shop_list_by_dishes_1(cook_book, dishes, person_count):
    if dishes in cook_book:
        print(f'{dishes}: ')
    for value in cook_book[dishes]:
        ingredient_name = value['ingredient_name']
        quantity = value["quantity"] * person_count
        measure = value['measure']
        print(f'{ingredient_name}: {quantity}, {measure}', end="")
    print()

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    # shopping_dict = {}
    # for dish in dishes:
    #     for item in cook_book[dish]:
    #         #Создаём словарь спсика блюд
    #         items_list = dict(
    #             [(item['ingredient_name'],  {'quantity': item['quantity'] * person_count, 'measure': item['measure'].strip()})])
    #         if item['ingredient_name'] in shopping_dict:
    #             extra_item = (int(shopping_dict[item['ingredient_name']]['quantity']) + int(
    #                 items_list[item['ingredient_name']]['quantity']))
    #             shopping_dict[item['ingredient_name']]['quantity'] = extra_item
    #             shopping_dict.update(items_list)
    #         # if shopping_dict.get(item['ingredient_name']): # Возвращаем значения для указанного ключа, если находим ключ в словаре
    #         #     extra_item = (int(shopping_dict[item['ingredient_name']]['quantity']) + int(items_list[item['ingredient_name']]['quantity']))
    #         #     shopping_dict[item['ingredient_name']]['quantity'] = extra_item #Нашёл в инете, как работает не могу понять "если ключа ещё нет - он создатся, если уже есть - то обновится по формулам"
    #         # else:
    #         #     shopping_dict.append(items_list) #Добаляет в словарь новый словарь (ключ значения)
    #     #print(f'Для приготовления блюда "{dish}" на {person_count} человек нам необходимо купить:')
    #     pprint(shopping_dict) #Ппринт, как он выводит не понятно, живёт своей жизнью
    #     print()

    cook_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingress_diets in cook_book[dish]:
                dict_ing = {}
                if ingress_diets['ingredient_name'] in cook_dict:
                    quantity = cook_dict[ingress_diets['ingredient_name']].get('quantity') + \
                               ingress_diets['quantity'] * person_count
                    cook_dict[ingress_diets['ingredient_name']].update(quantity=quantity)
                else:
                    dict_ing['measure'] = ingress_diets['measure']
                    dict_ing['quantity'] = ingress_diets['quantity'] * person_count
                    cook_dict[ingress_diets['ingredient_name']] = dict_ing
    return cook_dict

def read_txt():
    l = []
    counter = 3
    for i in range(1, counter + 1):
        with open(f'{i}.txt', 'r+', encoding="utf-8") as file:
            f = file.readlines()
            l.append([len(f), f'{i}.txt', f])
    # print(l)
    l.sort()
    #print(l)

    with open('output_file.txt', 'w', encoding="utf-8") as f:
        # output_file.write(output_file)
        for el in l:
            #print(el[0])
            f.write(str(el[0]) + '\n')
            f.write(el[1] + '\n')
            for line in el[2]:
                f.write(line)
            f.write('\n\n')

# def read_txt():
#     with open('1.txt', 'r+', encoding="utf-8") as file_1, \
#             open('2.txt', 'r+', encoding="utf-8") as file_2, \
#             open('3.txt', 'r+', encoding="utf-8") as file_3, \
#             open('4.txt', 'w', encoding="utf-8") as file_4:
#
#         data_1 = file_1.readlines()
#         data_2 = file_2.readlines()
#         data_3 = file_3.readlines()
#
#         dict_data_2 = {}
#         for i, lines in enumerate(data_2):  # Получаем по строчно данные из файла 2.txt
#             dict_data_2[i] = lines.strip()  # словарь где ключ - номер строки, а значение - текст
#             file_4.write(dict_data_2[0] + '\n')
#
#
#         dict_data_1 = {}
#         for i, lines in enumerate(data_1):   # Получаем по строчно данные из файла 1.txt
#             dict_data_1[i] = lines.strip()
#         file_4.write(dict_data_1[0] + ' ')
#         file_4.write(dict_data_1[1] + '.' + '\n')
#
#
#         dict_data_3 = {}
#         for i, lines in enumerate(data_3):   # Получаем по строчно данные из файла 3.txt
#             dict_data_3[i] = lines.strip()
#         file_4.write(dict_data_3[0] + ' ')
#         file_4.write(dict_data_3[1] + ' ')
#         file_4.write(dict_data_3[2] + ' ')
# Интресно, а можно прочитать файл по точке? И добавлять строку по точке?

def main_logic():
  cook_book = get_cook_book()  # вот теперь тут словарь,  это я понял
  # print(cook_book)

  # get_shop_list_by_dishes_1(cook_book, 'Омлет', 2)
  # get_shop_list_by_dishes(cook_book, ['Омлет', 'Фахитос'], 4)
  pprint(get_shop_list_by_dishes(cook_book, ['Омлет', 'Фахитос', 'Омлет'], 4))

  read_txt()


if __name__ == "__main__":
  main_logic()
