

# check is users data correct (maybe miss some element) and biuld new list with dicts of user data
def is_data_correct_dict(users: (dict)) -> [dict]:
    users_new = list(users)
    for user in users_new:
        if len(user.keys()) != len(users_new[0].keys()):
            print(f'Invalid data for user {user.get("id")}')
            users_new.remove(user)
            continue
    return users_new


#find all user data as int in variables
def find_user_data_int_dict(user) -> vars:
    level = int(user.get('level'))
    kills = int(user.get('kills'))
    balance = int(user.get('balance'))
    # if we have as input data new data with 'spent'
    if 'spent' in user.keys():
        spent = int(user.get('spent'))
        return level, kills, balance, spent
    else:
        return level, kills, balance


# check input user balance by criteria make output True/False and true_balance
def check_user_is_cheater_dicts(user) -> [bool, int]:
    index = [*find_user_data_int_dict(user)]
    level = index[0]
    kills = index[1]
    balance = index[2]
    max_balance = level * 1000 + kills * 1000
    if len(index) == 4:
        spent = index[3]
        return ((balance + spent) > max_balance), (max_balance - spent)
    else:
        return (balance > max_balance), max_balance

def update_cheater_balance_tuple_dicts(users: (dict)) -> tuple:
    users_new = is_data_correct_dict(users)
    for user in users_new:
        if check_user_is_cheater_dicts(user)[0]:
            user['balance'] = str(check_user_is_cheater_dicts(user)[1])
    return tuple(users)
