import json


def parse_users_form_json_file(filename: str) -> list:
    with open(filename, 'r') as file_object:
        try:
            users = json.load(file_object)
            for user in users['users']:
                if len(user) != 6:
                    raise ValueError(f'Invalid user data: {user}. It not include in analise.\n')
        except ValueError as v_er:
            print(ValueError, v_er)
        except TypeError:
            print('Your data type is incorrect')

    return users['users']


def save_users_to_json_file(filename: str, data: list) ->str:
    with open(filename, 'w') as filename:
        json.dump(data, filename, indent=4)

