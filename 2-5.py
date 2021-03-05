rating = [12, 8, 6, 6, 4]

while True:
    item = input('Пожалуйста введите число: ')
    if not item.isdigit():
        print("Введены некорректные данные. Попробуйте снова")
        continue
    else:
        item = int(item)

    idx = None

    for i, num in enumerate(rating):
        if item > num:
            idx = i
            break

    if idx is None:
        rating.append(item)
    else:
        rating.insert(idx, item)

    print(rating)

    


