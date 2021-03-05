list = [34.5, 46, None, 'interisting']
new_list = input('ВВедите элементы списка: ')
list.append(new_list)

last_idx = len(list) - 1

for idx, _ in enumerate(list):
    if idx % 2 == 0 and idx < last_idx:
        list[idx + 1], list[idx] = list[idx:idx + 2]


print(list)
