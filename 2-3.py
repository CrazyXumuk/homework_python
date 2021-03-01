seasons_list = [
               ['Зима', ['12', '1', '2']],
               ['Весна', ['3', '4', '5']],
               ['Лето', ['6', '7', '8']],
               ['Осень', ['9', '10', '11']]
]
seasons_dict = {
                'Зима': ['12', '1', '2'],
                'Весна': ['3', '4', '5'],
                'Лето': ['6', '7', '8'],
                'Осень': ['9', '10', '11']
}
month_number = input('Введите номер месяца от 1 до 12: ')
for season, months in seasons_list:
    if month_number in months:
        print(month_number, season)

for season, months in seasons_dict.items():
    if month_number in months:
        print(season, month_number)

