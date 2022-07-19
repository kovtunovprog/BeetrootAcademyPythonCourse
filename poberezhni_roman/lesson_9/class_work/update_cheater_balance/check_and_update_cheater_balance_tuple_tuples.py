



# check is users data correct (maybe miss some element) and biuld new list with lists of user data
def is_data_correct_tuple(users: tuple) -> list:
    users_new = []
    for user in users:
        user = list(user)
        if len(user) != len(users[0]):
            print(f'User data is incorrect: {user}')
            continue
        users_new.append(user)
    return users_new

#find all user data as int in variables
def find_user_data_int(users, user) -> vars:
    level = int(user[users[0].index('level')])
    kills = int(user[users[0].index('kills')])
    balance = int(user[users[0].index('balance')])
    if 'spent' in users[0]:
        spent = int(user[users[0].index('spent')])
        return level, kills, balance, spent
    else:
        return level, kills, balance

# check user balance by criteria make output True/False and true_balance
def check_user_is_cheater_tuples(users, user: list) ->[bool, int]:
    index = [*find_user_data_int(users, user)]
    level = index[0]
    kills = index[1]
    balance = index[2]
    max_balance = level * 1000 + kills * 1000
    if len(index) == 4:
        spent = index[3]
        return ((balance + spent) > max_balance), (max_balance-spent)
    else:
        return (balance > max_balance), max_balance

def update_cheater_balance_tuple_tuples(users_new: tuple) -> (tuple):
    users_new = is_data_correct_tuple(users_new)
    list_users = []
    list_users.append(tuple(users_new[0]))
    for user in users_new[1:]:
        if check_user_is_cheater_tuples(users_new, user)[0]:
            user[users_new[0].index('balance')] = check_user_is_cheater_tuples(users_new, user)[1]
        list_users.append(tuple(user))
    users_new = tuple(list_users)
    return users_new


