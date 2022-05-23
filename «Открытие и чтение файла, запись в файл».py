# Задача 1
way = '/home/nik/Рабочий стол/home_work/open_read_write/'

book_recipe = f'{way}recipe'

first_file = f'{way}1'
second_file = f'{way}2'
third_file = f'{way}3'

fourth_file = f'{way}4'


def get_data_from_file(file):
    """Чтение файла. На вход принимает абсолютный путь к файлу. Возвращает весь содержащийся в нём текст."""

    with open(file, 'r') as f:
        text_file = f.read()

    return text_file


text_in_file = get_data_from_file(book_recipe)


def create_lists_recipe(text=text_in_file):
    """Формирует список со списками ингредиентов. Входные параметры - текст из файла."""

    text = text.split('\n')
    list_recipe = []
    end_data_list = []
    for elem in text:
        if elem != '':
            list_recipe.append(elem)
        else:
            end_data_list.append(list_recipe)
            list_recipe = []

    return end_data_list


total_list = create_lists_recipe()


def create_cook_book(data_list):
    """Формирует cook_book. Принимает списки ингредиентов. Возвращает сформированный cook_book."""
    data = data_list
    cook_book = {}
    for block in data:
        cook_book[block[0]] = []
        for elem in range(2, len(block)):
            recipe = []
            ingredients = block[elem].split(' | ')
            dict_ing = {'ingredient_name': ingredients[0], 'quantity': ingredients[1], 'measure': ingredients[2]}
            recipe.append(dict_ing)
            cook_book[block[0]] += recipe

    return cook_book


cook_book = create_cook_book(total_list)

print(f'cook_book = {cook_book}\n')


# Задача 2. Нужно написать функцию, которая на вход принимает список блюд из cook_book и количество персон для кого
# мы будем готовить

def get_shop_list_by_dishes(dishes, person_count):
    temp_list = []
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for elem in cook_book[dish]:
                temp_list.append(elem)

    for elem in temp_list:
        shop_list[elem['ingredient_name']] = \
            {'measure': elem['measure'], 'quantity': (int(elem['quantity']) * person_count)}

    return shop_list


print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2), '\n')


# Задача №3
# В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны
#
# Необходимо объединить их в один по следующим правилам:
#
# 1. Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть
# первым нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
# 2. Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем

def merge_files(list_files):
    temp_list = []
    for element in list_files:
        with open(element, 'r') as file:
            count_string = len(file.readlines())
            name_file = file.name
            text_file = get_data_from_file(element)
            temp_list.append([count_string, name_file, text_file])

    temp_list.sort()

    for i in temp_list:
        with open(fourth_file, 'a') as file:
            file.write(f'{i[1]}\n{i[0]}\n{i[2]}')


merge_files([first_file, second_file, third_file])

print(get_data_from_file(fourth_file))
