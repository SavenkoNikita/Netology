import csv
import re

## Читаем адресную книгу в формате CSV в список contacts_list:
with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


## 1. Выполните пункты 1-3 задания.

## 1.1 Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной
# книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.

def format_name():
    """С помощью регулярных выражений расставляет на свои места ФИО. Возвращает скорректированный список."""

    data_list = contacts_list

    name = r'(^([А-ЯЁ]{1}[а-яё]+)?)([\s\,])' \
           r'(([А-ЯЁ]{1}[а-яё]+)?)([\s\,])' \
           r'(([А-ЯЁ]{1}[а-яё]+)?)([\s\,])' \
           r'([А-ЯЁ]{1}[а-яё]+)?([\s\,]*)' \
           r'(([а-яёА-ЯЁ]*)?)([\s\,]*)' \
           r'(([а-яёА-ЯЁa-zA-Z\s\W][^\,\+0-9]+)?)([\,]*)' \
           r'(((\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)' \
           r'(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*))?)(,)(\S*)'

    name_format = r'\2,\5,\8,\13,\15,\18,\42'

    contacts_list_format_name = []
    for elem in data_list:
        address_book = ','.join(elem)
        format_address_book = re.sub(name, name_format, address_book)
        new_data = format_address_book.split(',')
        contacts_list_format_name.append(new_data)

    return contacts_list_format_name


## 1.2 Привести все телефоны в формат +7(999)999-99-99.
# Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.

def format_phone():
    """С помощью регулярных выражений приводит все телефоны в формат +7(999)999-99-99.
    Возвращает скорректированный список."""

    data_list = format_name()

    phone_number_format = r'(\+7|8)(\s*)' \
                          r'(\(*)(\d{3})(\)*)(\s*)' \
                          r'(\-*)(\d{3})(\s*)' \
                          r'(\-*)(\d{2})(\s*)' \
                          r'(\-*)(\d{2})(\s*)' \
                          r'(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'

    new_phone_number_format = r'+7(\4)\8-\11-\14\15\17\18\20'

    contacts_list_format_phone = []
    for elem in data_list:
        address_book = ','.join(elem)
        format_address_book = re.sub(phone_number_format, new_phone_number_format, address_book)
        new_data = format_address_book.split(',')
        contacts_list_format_phone.append(new_data)

    return contacts_list_format_phone


## 1.3 Объединить все дублирующиеся записи о человеке в одну.

def create_a_dictionary_from_the_list():
    """Функция принимает список со списками людей из телефонной книги. Создаёт из него список с упорядоченными
    словарями и возвращает его."""

    list_of_subscribers = format_phone()

    sort_list = []
    for element in list_of_subscribers:
        dict_contact_book = {'lastname': element[0],
                             'firstname': element[1],
                             'surname': element[2],
                             'organization': element[3],
                             'position': element[4],
                             'phone': element[5],
                             'email': element[6]}
        sort_list.append(dict_contact_book)

    return sort_list


def merging_dictionaries(first_dict, second_dict):
    """Объединяет два идентичных словаря заполняя пустые поля"""

    combined_dictionary = {}

    dictionary_elements = [
        'lastname',
        'firstname',
        'surname',
        'organization',
        'position',
        'phone',
        'email'
    ]

    for elements in dictionary_elements:
        if first_dict.get(elements) == '':
            combined_dictionary[elements] = second_dict.get(elements)
        elif first_dict.get(elements) != '':
            combined_dictionary[elements] = first_dict.get(elements)

    return combined_dictionary


def search_for_duplicate_records():
    """Принимает лист с упорядоченными словарями. Ищет совпадения по имени и фамилии. Если есть совпадение, вызывает
    функцию merging_dictionaries(). Возвращает список с упорядоченными словарями без дублей."""

    list_dicts = create_a_dictionary_from_the_list()
    unique_list = []

    while len(list_dicts) > 1:
        first_dict = list_dicts[0]
        lastname_first_dict = first_dict.get('lastname')
        firstname_first_dict = first_dict.get('firstname')
        index_first_dict = list_dicts.index(first_dict)

        index_next_dict = index_first_dict + 1

        for elem in list_dicts:
            if index_next_dict < len(list_dicts):
                next_dict = list_dicts[index_next_dict]
                lastname_next_dict = next_dict.get('lastname')
                firstname_next_dict = next_dict.get('firstname')

                if lastname_first_dict == lastname_next_dict and firstname_first_dict == firstname_next_dict:
                    unique_list.append(merging_dictionaries(first_dict, next_dict))
                    list_dicts.pop(index_next_dict)
                    break
                index_next_dict += 1
            else:
                unique_list.append(first_dict)

        list_dicts.pop(index_first_dict)
    return unique_list


def reformat_to_csv_type_book():
    """Преобразует сформированные словари в исходных формат. Возвращает список."""

    dict_data = search_for_duplicate_records()
    new_phone_book = []

    for dicts in dict_data:
        lastname = dicts.get('lastname')
        firstname = dicts.get('firstname')
        surname = dicts.get('surname')
        organization = dicts.get('organization')
        position = dicts.get('position')
        phone = dicts.get('phone')
        email = dicts.get('email')

        new_phone_book.append([lastname, firstname, surname, organization, position, phone, email])

    return new_phone_book


## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

    ## Вместо contacts_list подставьте свой список:
    datawriter.writerows(reformat_to_csv_type_book())
