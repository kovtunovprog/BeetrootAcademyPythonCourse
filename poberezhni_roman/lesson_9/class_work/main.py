
from poberezhni_roman.lesson_9.class_work.update_cheater_balance import check_user_is_cheater_tuples, \
    update_cheater_balance_tuple_tuples, check_user_is_cheater_dicts, update_cheater_balance_tuple_dicts

users_1 = (
    ("id", "name", "balance", "level", "kills"),
    ("1", "Bilbo", "4000", "2", "4"),
    ("2", "Indigo", "42600", "40", "100"),
    ("3", "Farmer", "5000", "3", "2"),
    ("4", "O'rizotto", "5000", "1", "0"),
    ("5", "Bilbo-1", "0", "1", "0"),
    ("6", "Bilbo-2", "0", "1", "0"),
    ("7", "Bilbo-3", "0", "1", "0"),
    ("8", "O'rizotto-1", "0", "1", "0"),
    ("9", "O'rizotto-2", "0", "1", "0"),
    ("10", "O'rizotto-3", "0", "1", "0"),
    ("11", "O'rizotto-4", "0", "1", "0"),
    ("12", "Bilbo-1", "4200", "2", "1"),
    ("13", "GlobalLogic", "720500", "353", "440")
)


users_2 = (
    ("id", "name", "balance", "spent", "level", "kills"),
    ("1", "Bilbo", "4000", "5000", "2", "4"),
    ("2", "Indigo", "42600", "97400", "40", "100"),
    ("3", "Farmer", "5000", "0", "3", "2"),
    ("4", "O'rizotto", "5000", "0", "1", "0"),
    ("5", "Bilbo-1", "0", "0", "1", "0"),
    ("6", "Bilbo-2", "0", "0", "1", "0"),
    ("7", "Bilbo-3", "0", "0", "1", "0"),
    ("8", "O'rizotto-1", "0", "0", "1", "0"),
    ("9", "O'rizotto-2", "0", "0", "1", "0"),
    ("10", "O'rizotto-3", "0", "0", "1", "0"),
    ("11", "O'rizotto-4", "0", "0", "1", "0"),
    ("12", "Movisyan-23", "4200", "1000", "1"),
    ("13", "GlobalLogic", "720500", "0", "353", "440")
)


users_3 = (
    {"id": "42452", "name": "Bingo", "balance": "4000", "spent": "5000", "level": "2", "kills": "4"},
    {"id": "5341", "name": "LacasaDePapel", "balance": "42600", "spent": "97400", "level": "40", "kills": "100"},
    {"id": "435232353", "name": "Diablo", "balance": "48888", "spent": "0", "level": "3", "kills": "2"},
    {"id": "424", "name": "Jambo", "balance": "4000", "spent": "24552", "level": "12", "kills": "4"},
    {"id": "5321", "name": "CoroZi", "balance": "4200", "spent": "1000", "level": "2", "kills": "1"},
    {"id": "242432", "name": "Raynor", "balance": "720500", "spent": "0", "level": "353", "kills": "440"},
    {"id": "1", "name": "Raynorhg", "spent": "0", "level": "350", "kills": "440"},                                  #####
    {"id": "242432123", "name": "Raynor123", "balance": "7205002", "spent": "0", "level": "353", "kills": "440"},
)



print(f'Is {users_2[1][1]} cheater?: {check_user_is_cheater_tuples(users_2, users_2[1])[0]}, balance need to be: {check_user_is_cheater_tuples(users_2, users_2[1])[1]}')

print(update_cheater_balance_tuple_tuples(users_2))

print(f'Is {users_3[0]["name"]} cheater?: {check_user_is_cheater_dicts(users_3[0])[0]}, balance need to be: {check_user_is_cheater_dicts(users_3[0])[1]}')

print(update_cheater_balance_tuple_dicts(users_3))



