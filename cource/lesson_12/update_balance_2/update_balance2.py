from cource.lesson_12.usefull_function import from_dict_to_tuple, from_tuple_to_dict, spent_add, balance_fix, pop_incorrect_data


def update_users_balances_2(users: list) -> list:

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

    print(users)

    return users


update_users_balances(users_2)