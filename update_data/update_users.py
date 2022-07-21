from data_users.alphabase import users_3 as users


def from_tuple_to_dict(users: list) -> list:
    head = users.pop(0)
    for ind, user in enumerate(users):
        users[ind] = {}
        for i in range(len(head)):
            users[ind][head[i]] = user[i]
    return users


def spent_add(users: list) -> list:
    for i in users:
        i['spent'] = 0
    return users


def right_balance(user: dict) -> int:
    return (int(user['level']) + int(user['kills'])) * 1000 - int(user['spent'])


def user_is_cheater(user: dict) -> bool:
    return right_balance(user) != int(user['balance'])


def balance_fix(users: list) -> list:
    for user in users:
        if user_is_cheater(user):
            user['balance'] = right_balance(user)
    return users


def find_cheaters(users: list) -> tuple:
    list_of_cheaters = []
    for user in users:
        try:
            if user_is_cheater(user):
                list_of_cheaters.append(user)
                raise ValueError(f'Error. user id.{user["id"]},  name = {user["name"]} is cheater!')
        except ValueError as arr:
            print(arr)
    return tuple(list_of_cheaters)


def from_dict_to_tuple(users: list) -> list:
    head = tuple([i for i in users[0]])
    for ind, user in enumerate(users):
        users[ind] = tuple([i for i in user.values()])
    users.insert(0, head)
    return users


def update_balance(users: tuple) -> tuple:

    users = list(users)

    if type(users[0]) == tuple:
        users = from_tuple_to_dict(users)

    if 'spent' not in users[0]:
        spent_add(users)

    users = balance_fix(users)

    how_to_output = input('How to output? (1) - Tuple (tuples) or (2) - Tuple (dicts)\n')

    if how_to_output == '1':
        print(tuple(from_dict_to_tuple(users)))
    else:
        print(tuple(users))
    return tuple(users)


def get_cheaters(users: tuple) -> tuple:
    users = list(users)

    if type(users[0]) == tuple:
        users = from_tuple_to_dict(users)

    if 'spent' not in users[0]:
        spent_add(users)
    cheaters = find_cheaters(users)
    print(f'All cheaters:', *cheaters, sep='\n')
    return tuple(cheaters)


if __name__ == '__main__':

    get_cheaters(users)

    update_balance(users)
