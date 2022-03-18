# Напишите код для преобразования произвольного списка вида ['2018-01-01', 'yandex', 'cpc', 100] (он может быть любой
# длины) в словарь {'2018-01-01': {'yandex': {'cpc': 100}}}

data_list = ['2018-01-01', 'yandex', 'cpc', 100]
data_dict = {}
first_dict = {data_list[-2]: data_list[-1]}

data_list.pop(-1)
data_list.pop(-1)
data_dict[data_list[-1]] = first_dict

for i in data_list:
    data_dict[data_list[-1]] = data_dict
    data_list.pop(-1)

print(data_dict)
