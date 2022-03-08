# Дан список поисковых запросов. Получить распределение количества слов в них. Т.е. поисковых запросов из одного -
# слова 5%, из двух - 7%, из трех - 3% и т.д.

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
]

one_word_query = 0
two_word_query = 0
three_word_query = 0

for elem in queries:
    count = len(elem.split())
    if count == 1:
        one_word_query += 1
    elif count == 2:
        two_word_query += 1
    elif count == 3:
        three_word_query += 1

total_requests = len(queries)

print(f'Всего запросов: {total_requests}\n'
      f'Поисковых запросов из одного слова: {one_word_query} ({one_word_query * 100 // total_requests}%),\n'
      f'из двух: {two_word_query} ({two_word_query * 100 // total_requests}%),\n'
      f'из трех: {three_word_query} ({three_word_query * 100 // total_requests}%).')
