sum_number = 0
is_exit = False

while True:
    number = input('Введите последовательность: ').split()
    for item in number:
        if item == 'x':
            is_exit = True
            break
        if not item.isdigit():
            print(f"Это не число {item}")
            break
        try:
            item = float(item)
        except ValueError:
            pass
        sum_number += int(item)
    print(f"Сумма: {sum_number}")