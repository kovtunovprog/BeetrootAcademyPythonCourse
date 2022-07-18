# Roman Poberezhnyi
from poberezhni_roman.Alfastars.p import users_1 as users


# We have some data as input or import and check in what type we receive this data, next steps depend on data type
def check_what_data_type_analise(users):
    if type(users[0]) == dict:
        return change_dicts_in_lists(users)
    elif type(users[0]) == tuple:
        return change_tuples_in_list(users)
    else:
        print("Incorrect data")



# We change dicts type to list
def change_dicts_in_lists(users):
    users_new = []
    users_new.append(list(users[0].keys()))
    for user in users:
        # check is user data correct and print result if not
        if len(user.keys()) != len(users_new[0]):
            print(f'Invalid data for user {user}\n')
            continue
        # create data from dict values for user and add in users_new
        user_in = []
        users_new.append(user_in)
        for x in user.values():
            user_in.append(x)
    users_new = tuple(users_new)   ########
    return users_new

# change tuple type to list
def change_tuples_in_list(users):
    users_new = []
    users_new.append(list(users[0]))
    for user in users[1:]:
        # check is user data correct
        if len(user) != len(users_new[0]):
            print(f'Invalid data for user {user[0]}\n')
            continue
        # add all data as lists
        users_new.append(list(user))
    users_new = tuple(users_new) #########
    return users_new

users_new = check_what_data_type_analise(users)
# print(users_new)

# Analise users_new list and if we find incorrect balance change it to correct data
def analise_users_list(users_new):
    list_users = []
    list_users.append(tuple(users_new[0]))
    for user in users_new[1:]:
        # find all needed data no mater where it places
        level = int(user[users_new[0].index('level')])
        kill = int(user[users_new[0].index('kills')])
        balance = int(user[users_new[0].index('balance')])
        max_balance = level * 1000 + kill * 1000
        # if we have as input data new data with 'spent'
        if 'spent' in users_new[0]:
            spent = int(user[users_new[0].index('spent')])
            # change balance if user is cheater
            if (balance + spent) > max_balance:
                user[users_new[0].index('balance')] = str(max_balance - spent)
        # if we receive old data
        else:
            if balance > max_balance:
                user[users_new[0].index('balance')] = str(max_balance)
        list_users.append(tuple(user))
    users_new = tuple(list_users)
    return users_new

# ask customer in what type he/she need output
def question_in_what_type_output():
    b = input('In what type make output (1 - tuples, 2 - dicts): ')
    if b == '1':
        analise_users_list(users_new)
        print(analise_users_list(users_new))
    elif b == '2':
        analise_users_list(users_new)
        print(change_users_data_as_dicts(users_new))
    else:
        print('Incorrect input type!!!')


def change_users_data_as_dicts(users_new):
    users_dict_list = []
    for data in users_new[1:]:
        # отримання доступу до даних кожного юзера, без першого запису
        users_dict = {key: value for (key, value) in zip(users_new[0], data)}
        # створення словника з запису кожного юзера де ключі це перший запис, а значення це дані кожного юзера
        users_dict_list.append(users_dict)
        # через складність додавання даних до кортежу, спочакту додаємо словники до листа. то потім створюємо кортеж зі словників
    users_tuple = tuple(users_dict_list)
    return users_tuple

question_in_what_type_output()






