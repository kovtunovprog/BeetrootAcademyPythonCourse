import json
def parse_users_form_json_file(filename: str) -> list:
    with open(filename, 'r') as file_object:
        try:
            users = json.load(file_object)
            for user in users:
                if len(user) != 6:
                    raise ValueError(f'Invalid user data: {user}. It not include in analise.\n')
        except TypeError('Your data type is incorrect')
    return(users)


def save_users_to_json_file(filename: str, data: list) -> str:
    with open(filename, 'w') as data:
        json.dump(filename, data)

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

def verify_data_type(file):
    if type(file) == dict:
        users = file["users"]
        users_update = []
        for user in users:
            try:
                if len(user.keys()) != len(users[0]):
                    raise ValueError(f'Invalid user data: {user}. It not include in analise.\n')
            except ValueError as v_er:
                print(ValueError, v_er)
                continue
            users_update.append(user)
    return True
