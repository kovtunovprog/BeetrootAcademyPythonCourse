from pprint import pprint

users = (('id', 'name', 'balance', 'level', 'kills'),
    ('1', 'Bilbo', '4000', '2', '4'),
    ('2', 'Indigo', '42600', '40', '100'),
    ('3', 'Farmer', '5000', '3', '2'),
    ('4', 'O’rizotto', '5000', '1', '0'),
    ('5', 'Bilbo-1', '0', '1', '0'),
    ('6', 'Bilbo-2', '0', '1', '0'),
    ('7', 'Bilbo-3', '0', '1', '0'),
    ('8', 'O’rizotto-1', '0', '1', '0'),
    ('9', 'O’rizotto-2', '0', '1', '0'),
    ('10', 'O’rizotto-3', '0', '1', '0'),
    ('11', 'O’rizotto-4', '0', '1', '0'),
    ('12', 'Bilbo-1', '4200', '2', '1'),
    ('13', 'GlobalLogic', '720500', '353', '440'))

users_dict_list = []
for data in users[1:]:      #отримання доступу до даних кожного юзера, без першого запису
    users_dict = {key: value for (key, value) in zip(users[0], data)} #створення словника з запису кожного юзераб де ключі це перший запис, а значення це дані кожного юзера
    users_dict_list.append(users_dict) #через складність додавання даних до кортежу, спочакту додаємо словники до листа. то потім створюємо кортеж зі словників
users_tuple = tuple(users_dict_list)
# pprint(users_tuple) #не знаю чому, ппринт щось не дуже працює, деякі дані обрізає і т.п., для нормально відображення використав цикл нижче
for i in range(len(users_tuple)):
    print(users_tuple[i])
print(users_tuple)





