from pprint import pprint

from aplpha_2_py import users_2 as users

# import data1

# users = (
#     ("id", "name", "balance", "spent", "level", "kills"),
#     ("1", "Bilbo", "4000", "5000", "2", "4"),
#     ("2", "Indigo", "42600", "97400", "40", "100"),
#     ("3", "Farmer", "5000", "0", "3", "2"),
#     ("4", "O'rizotto", "5000", "0", "1", "0"),
#     ("5", "Bilbo-1", "0", "0", "1", "0"),
#     ("6", "Bilbo-2", "0", "0", "1", "0"),
#     ("7", "Bilbo-3", "0", "0", "1", "0"),
#     ("8", "O'rizotto-1", "0", "0", "1", "0"),
#     ("9", "O'rizotto-2", "0", "0", "1", "0"),
#     ("10", "O'rizotto-3", "0", "0", "1", "0"),
#     ("11", "O'rizotto-4", "0", "0", "1", "0"),
#     ("12", "Movisyan-23", "4200", "1000", "2", "1"),
#     ("13", "GlobalLogic", "720500", "0", "353", "440")
# )

newlist = []
for user in users:
    if user[0] == 'id':
        continue
    user = list(user)
    id, name, balance, spent, level, kills = user

    max_balans = (int(kills) + int(level)) * 1000
    # print(max_balans)
    # print(int(spent))
    # print(int(balance))
    # print(max_balans-int(spent))


    if int(balance) != (max_balans-int(spent)):
        print(f'User {name} is cheater and id: {id}')
        user[2] = (max_balans-int(spent))

    newlist.append(user)


newlist = [list(users[0])] + newlist
    # print(user)
pprint(newlist)



