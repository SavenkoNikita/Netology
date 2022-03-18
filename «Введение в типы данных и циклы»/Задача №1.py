boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

boys.sort()
girls.sort()

if len(boys) == len(girls):
    list_lovers = zip(boys, girls)
    print('Идеальные пары:')
    for boy, girls in list_lovers:
        print(f'{boy} и {girls}')
else:
    print(f'Мальчиков {len(boys)}, а девочек {len(girls)}, кто-то может остаться без пары!')
