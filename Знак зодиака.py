month = input('Введите месяц: ')
date = int(input('Введите число: '))

if (month == 'январь' and date >= 21) or (month == 'февраль' and date < 18):
    print('Вывод:\n', 'Водолей')
elif (month == 'февраль' and date >= 19) or (month == 'март' and date < 20):
    print('Вывод:\n', 'Рыбы')
elif (month == 'март' and date >= 21) or (month == 'апрель' and date < 20):
    print('Вывод:\n', 'Овен')
elif (month == 'апрель' and date >= 21) or (month == 'май' and date < 20):
    print('Вывод:\n', 'Телец')
elif (month == 'май' and date >= 21) or (month == 'июнь' and date < 21):
    print('Вывод:\n', 'Близнецы')
elif (month == 'июнь' and date >= 22) or (month == 'июль' and date < 22):
    print('Вывод:\n', 'Рак')
elif (month == 'июль' and date >= 23) or (month == 'август' and date < 23):
    print('Вывод:\n', 'Лев')
elif (month == 'август' and date >= 24) or (month == 'сентябрь' and date < 23):
    print('Вывод:\n', 'Дева')
elif (month == 'сентябрь' and date >= 24) or (month == 'октябрь' and date < 23):
    print('Вывод:\n', 'Весы')
elif (month == 'октябрь' and date >= 24) or (month == 'ноябрь' and date < 22):
    print('Вывод:\n', 'Скорпион')
elif (month == 'ноябрь' and date >= 23) or (month == 'декабрь' and date < 21):
    print('Вывод:\n', 'Стрелец')
elif (month == 'декабрь' and date >= 22) or (month == 'январь' and date < 20):
    print('Вывод:\n', 'Козерог')
