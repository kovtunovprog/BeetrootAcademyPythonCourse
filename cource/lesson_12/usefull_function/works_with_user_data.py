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
