def find_cheaters(users: list) -> list:
    raise NotImplementedError



# check input data type and transform in need type
def change_type_analise(users) -> tuple:
    try:
        if type(users[0]) == dict:
            return change_dicts_in_tuple_and_check_data_correct(users)
        elif type(users[0]) == tuple or type(users[0]) == list:
            return users
    except TypeError:
        print(TypeError, "Incorrect data type!")


def change_dicts_in_tuple_and_check_data_correct(users) -> tuple:
    l = [list(users[0].keys())]
    for user in list(users):
        # check is user data correct and print result if not
        try:
            if len(user.keys()) != len(l[0]):
                raise ValueError(f'Invalid user data: {user}. It not include in analise.\n')
        except ValueError as v_er:
            print(ValueError, v_er)
            continue
        # create data from dict values for user and add in users_new
        l.append(change_user_dct_in_tpl(user))
    users_new = tuple(l)
    return users_new


def change_user_dct_in_tpl(user: dict) -> list:
    user_data = [*(i for i in user.values())]
    return user_data


# check is users data correct (maybe miss some element) and build new list with lists of user data
def is_data_correct_tuple(users: tuple) -> list:
    userss = list(change_type_analise(users))
    users_new = []
    for user in userss:
        user = list(user)
        try:
            if len(user) != len(userss[0]):
                raise ValueError(f'Invalid user data: {user}. It not include in analise.\n')
        except ValueError as v_er:
            print(ValueError, v_er)
            continue
        users_new.append(user)
    return users_new


# find all user data as int in variables
def find_user_data_int(users: tuple, user) -> vars:
    userss = is_data_correct_tuple(users)
    # user1 = change_user_dct_in_tpl(user)
    level = int(user[userss[0].index('level')])
    kills = int(user[userss[0].index('kills')])
    balance = int(user[userss[0].index('balance')])
    if 'spent' in userss[0]:
        spent = int(user[userss[0].index('spent')])
        return level, kills, balance, spent
    else:
        return level, kills, balance



# check user balance by criteria make output True/False and true_balance
def check_is_user_cheater(users: tuple, user) -> [bool, int]:
    index = find_user_data_int(users, user)
    level = index[0]
    kills = index[1]
    balance = index[2]
    max_balance = level * 1000 + kills * 1000
    if len(index) == 4:
        spent = index[3]
        if (max_balance - spent) >= 0:
            true_balance = (max_balance - spent)
        else:
            true_balance = 0
        return ((balance + spent) > max_balance), true_balance
    else:
        return (balance > max_balance), max_balance

def find_cheaters_list(users_new: tuple) -> (tuple, list):
    users_new = is_data_correct_tuple(users_new)
    cheaters_l = []
    # cheaters_l.append(tuple(users_new[0]))
    for user in users_new[1:]:
        try:
            if check_is_user_cheater(users_new, user)[0]:
                raise ValueError(f"Found  cheater: {user[0:2]}")
        except ValueError as v_er:
            print(ValueError, v_er)
            cheaters_l.append(tuple(user))

    return tuple(cheaters_l)

if __name__ == '__main__':
    from poberezhni_roman.lesson_10.cw_10.p import users_1
    print(find_cheaters_list(users_1))