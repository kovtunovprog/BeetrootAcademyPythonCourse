from poberezhni_roman.Alfastars.p import users_3 as users_


# We have some data as input or import and check in what type we receive this data, next steps depend on data type
def check_what_data_type_analise(users):
    if type(users[0]) == dict:
        return users
    elif type(users[0]) == tuple:
        return change_users_data_as_dicts(users)
    else:
        print("Incorrect data")

def change_users_data_as_dicts(users):
    users_dict_list = []
    for data in users[1:]:
        # отримання доступу до даних кожного юзера, без першого запису
        users_dict = {key: value for (key, value) in zip(users[0], data)}
        # створення словника з запису кожного юзера де ключі це перший запис, а значення це дані кожного юзера
        users_dict_list.append(users_dict)
    # print(tuple(users_dict_list))
    return tuple(users_dict_list)

def analise_users_dict(users):
    users = list(users)
    for user in users:
        if len(user.keys()) != len(users[0].keys()):
            print(f'Invalid data for user {user.get("id")}')
            users.remove(user)
            continue
        # find all needed data no mater where it places
        level = int(user.get('level'))
        kill = int(user.get('kills'))
        balance = int(user.get('balance'))
        max_balance = level * 1000 + kill * 1000
        # if we have as input data new data with 'spent'
        if 'spent' in user.keys():
            spent = int(user.get('spent'))
            # change balance if user is cheater
            if (balance + spent) > max_balance:
                user['balance'] = str(max_balance - spent)
            # if we receive old data
        else:
            if balance > max_balance:
                user['balance'] = str(max_balance)
    return tuple(users)

def change_dicts_in_lists(users):
    users_new = []
    users_new.append(tuple(users[0].keys()))
    for user in users:
        # create data from dict values for user and add in users_new
        user_in = []
        for x in user.values():
            user_in.append(x)
        users_new.append(tuple(user_in))
    return tuple(users_new)

def question_in_what_type_output(users):
    b = input('In what type make output (1 - tuples, 2 - dicts): ')
    if b == '1':

        print(change_dicts_in_lists(users))
    elif b == '2':
        print(analise_users_dict(users))
    else:
        print('Incorrect input type!!!')

users_new2 = check_what_data_type_analise(users_)
print(users_new2)

c = analise_users_dict(users_new2)
print(users_new2)
print(c)
question_in_what_type_output(c)
