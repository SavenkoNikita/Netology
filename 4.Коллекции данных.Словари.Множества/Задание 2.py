ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

# list_id = [ids.values()]
# print(list_id)

list_id = []

for elem in ids.values():
       for name_id in elem:
              list_id.append(name_id)

list_id_1 = list(set(list_id))
list_id_1.sort()

print(list_id_1)
