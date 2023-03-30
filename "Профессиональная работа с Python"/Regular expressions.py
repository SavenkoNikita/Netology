from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

## 1. Выполните пункты 1-3 задания.
## 1.1 Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. В записной
# книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.
for elements in contacts_list:


# ## 2. Сохраните получившиеся данные в другой файл.
# ## Код для записи файла в формате CSV:
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#
#     ## Вместо contacts_list подставьте свой список:
#     datawriter.writerows(contacts_list)
