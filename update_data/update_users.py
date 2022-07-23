from data_users.alphabase import users_2 as users


def from_tuple_to_dict(users: list) -> list:
    head = users.pop(0)
    for ind, user in enumerate(users):
        users[ind] = {}
        for i in range(len(head)):
            users[ind][head[i]] = user[i]
    return users


def pop_incorrect_data(users: list) -> tuple:
    incorrect_users = []
    for i in range(len(users)-1, -1, -1):
        if len(users[i]) != len(users[0]):
            incorrect_users.append(users.pop(i))
    if incorrect_users:
        print(*incorrect_users[::-1], sep='\n')
    return tuple(incorrect_users[::-1])


def spent_add(users: list) -> list:
    for user in users:
        user['spent'] = 0
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


def find_cheaters(user: dict, list_of_cheaters: list):
    try:
        if user_is_cheater(user):
            list_of_cheaters.append(user)
            raise ValueError(f'Error. user id.{user["id"]},'
                             f'  name : {user["name"]}, is cheater!')
    except ValueError as arr:
        print(arr)


def collect_cheaters(users: list) -> tuple:
    list_of_cheaters = []
    for user in users:
        find_cheaters(user, list_of_cheaters)
    return tuple(list_of_cheaters)


def from_dict_to_tuple(users: list) -> list:
    head = tuple([i for i in users[0]])
    for ind, user in enumerate(users):
        users[ind] = tuple([i for i in user.values()])
    users.insert(0, head)
    return users


def update_balance(users: tuple) -> tuple:

    users = list(users)

    incorrect_users = pop_incorrect_data(users)  # I think we will need incorrect users in the future

    if type(users[0]) == tuple:
        from_tuple_to_dict(users)
        ''' if we get data of users in tuple(tuple(),tuple()...)
        we will convert it and we create new indexes for elements of users
       original date will not be changed'''

    if 'spent' not in users[0]:
        spent_add(users)

    balance_fix(users)

    how_to_output = input('How to output? (1) - Tuple (tuples) or (2) - Tuple (dicts)\n')

    if how_to_output == '1':
        from_dict_to_tuple(users)

    print(tuple(users))

    return tuple(users)


def get_cheaters(users: tuple) -> tuple:

    users = list(users)

    incorrect_users = pop_incorrect_data(users)  # I think we will need incorrect users in the future

    if type(users[0]) == tuple:
        from_tuple_to_dict(users)

    if 'spent' not in users[0]:
        spent_add(users)

    cheaters = collect_cheaters(users)

    return tuple(cheaters) if cheaters else print('There is no cheaters!')


if __name__ == '__main__':

    get_cheaters(users)

    update_balance(users)
