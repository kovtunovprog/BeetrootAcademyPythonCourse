# def find_cheaters(users: list) -> list:
#     raise NotImplementedError
from poberezhni_roman.lesson_10.cw_10.p import users_3

def check_is_data_correct(users) -> list:
    users_new = [users[0].keys()]
    for user in users:
        # check is user data correct and print result if not
        try:
            if len(user.keys()) != len(users_new[0]):
                raise ValueError(f'Invalid user data: {user}. It not include in analise.\n')
        except ValueError as v_er:
            print(ValueError, v_er)
            continue
        # create data from dict values for user and add in users_new
        users_new.append(user)
    return users_new


def find_user_data_int(user: dict) -> vars:
    level = int(user.get('level'))
    kills = int(user.get('kills'))
    balance = int(user.get('balance'))
    spent = int(user.get('spent'))
    return level, kills, balance, spent

def get_correct_user_balance(user) -> int:
    index = find_user_data_int(user)
    level = index[0]
    kills = index[1]
    spent = index[3]
    max_balance = level * 1000 + kills * 1000
    correct_balance = max_balance - spent
    return correct_balance


# check user balance by criteria make output True/False and true_balance
def check_is_user_cheater(user) -> bool:
    index = find_user_data_int(user)
    balance = index[2]
    correct_balance = get_correct_user_balance(user)
    return balance != correct_balance


def find_cheaters(users_new: list) -> list:
    users_new = check_is_data_correct(users_new)
    cheaters_l = []
    for user in users_new[1:]:
        try:
            if check_is_user_cheater(user):
                raise ValueError(f"Found  cheater: {user['name']}")
        except ValueError as v_er:
            print(ValueError, v_er)
            cheaters_l.append(user)

    return cheaters_l

if __name__ == '__main__':
    print(find_cheaters(users_3))