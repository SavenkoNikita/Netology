stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}  # , 'zsearch': 325, 'yahoo': 3}

top_list = []

for name, meaning in stats.items():
    top_list.append([meaning, name])

top_list.sort()

print(top_list[-1][1])
