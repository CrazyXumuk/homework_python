
def simple_calc():
    time = float(input('Введите количество отработанных часов : '))
    hour = float(input('Введите суммы оплаты труда за 1 час : '))
    premia = float(input('Укажите размер премии - '))
    pay = time * hour
    return pay + premia
print(f'Размер заработной платы составил: {simple_calc() }')