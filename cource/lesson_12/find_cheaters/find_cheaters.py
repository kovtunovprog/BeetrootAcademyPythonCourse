# def find_cheaters(users: list) -> list:
#     raise NotImplementedError



# check input data type and transform in need type
from poberezhni_roman.lesson_10.cw_10.p import users_2


def change_type_analise(users) -> list:
    try:
        if type(users[0]) == dict:
            return change_dicts_in_tuple_and_check_data_correct(users)
        elif type(users[0]) == list:
            return is_data_correct_list(users)
    except TypeError:
        print(TypeError, "Incorrect data type!")


def change_dicts_in_tuple_and_check_data_correct(users) -> list:
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
        users_new.append(change_user_dict_in_tupl(user))
    return users_new


def change_user_dict_in_tupl(user: dict) -> list:
    user_data = [*(i for i in user.values())]
    return user_data


# check is users data correct (maybe miss some element) and build new list with lists of user data
def is_data_correct_list(users: list) -> list:
    users_new = []
    for user in users:
        user = list(user)
        try:
            if len(user) != len(users[0]):
                raise ValueError(f'Invalid user data: {user}. It not include in analise.\n')
        except ValueError as v_er:
            print(ValueError, v_er)
            continue
        users_new.append(user)
    return users_new


# find all user data as int in variables
def find_user_data_int(users: list, user) -> vars:
    userss = change_type_analise(users)
    level = int(user[userss[0].index('level')])
    kills = int(user[userss[0].index('kills')])
    balance = int(user[userss[0].index('balance')])
    spent = int(user[userss[0].index('spent')])
    return level, kills, balance, spent


# check user balance by criteria make output True/False and true_balance
def check_is_user_cheater(users: list, user) -> bool:
    index = find_user_data_int(users, user)
    balance = index[2]
    correct_balance = get_correct_user_balance(users, user)
    return (balance != correct_balance)

def get_correct_user_balance(users, user) -> int:
    index = find_user_data_int(users, user)
    level = index[0]
    kills = index[1]
    balance = index[2]
    spent = index[3]
    max_balance = level * 1000 + kills * 1000
    correct_balance = max_balance - spent
    return correct_balance


def find_cheaters(users_new: list) -> list:
    users_new = change_type_analise(users_new)
    cheaters_l = []
    for user in users_new[1:]:
        try:
            if check_is_user_cheater(users_new, user):
                raise ValueError(f"Found  cheater: {user[0:2]}")
        except ValueError as v_er:
            print(ValueError, v_er)
            cheaters_l.append(user)

    return cheaters_l

if __name__ == '__main__':

    print(find_cheaters(users_2))