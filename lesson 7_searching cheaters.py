from pprint import pprint
users = (
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
    ("12", "Movisyan-23", "4200", "1000", "2", "1"),
    ("13", "GlobalLogic", "720500", "0", "353", "440")
)
list_users = []
keys = list(users[0])
for user in users:
    if user == users[0]:
        list_users.append(list(user))
        continue

    user = {keys[x]: user[x] for x in range(len(keys))}

    max_balance = (int(user['kills']) + int(user['level'])) * 1000
    spent = int(user['spent'])
    balance = int(user['balance'])
    if balance + spent > max_balance:
        user['balance'] = max_balance - spent
        print(f"user with name: {user['name']} and id: {user['id']} is a cheater")

    list_users.append(user)

pprint(list_users)