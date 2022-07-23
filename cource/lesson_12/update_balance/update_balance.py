def update_users_balances(users: list) -> list:
    raise NotImplementedError


from poberezhni_roman.lesson_10.cw_10.update_balance_pack.find_cheaters_pack import is_data_correct_tuple, \
    check_is_user_cheater


def update_cheaters_balance(users_new: tuple) -> (tuple, list):

    users_new = is_data_correct_tuple(users_new)
    list_users = []
    list_users.append(tuple(users_new[0]))
    for user in users_new[1:]:
        if check_is_user_cheater(users_new, user)[0]:
            user[users_new[0].index('balance')] = check_is_user_cheater(users_new, user)[1]
        list_users.append(tuple(user))
    users_new = tuple(list_users)
    return users_new


if __name__ == '__main__':
    from poberezhni_roman.lesson_10.cw_10.p import users_1
    print(update_cheaters_balance(users_1))