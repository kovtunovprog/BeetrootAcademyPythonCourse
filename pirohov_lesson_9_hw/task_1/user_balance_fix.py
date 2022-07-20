def right_balance(user: dict) -> int:
    return (int(user['level']) + int(user['kills'])) * 1000 - int(user['spent'])


def user_is_cheater(user: dict) -> bool:
    return right_balance(user) != int(user['balance'])


def balance_fix(users: list) -> list:
    for user in users:
        if user_is_cheater(user):
            user['balance'] = right_balance(user)
    return users
