import json


def parse_users_form_json_file(filename: str) -> list:
    with open(filename, 'r') as f:
        try:
            users = json.load(f)['users']
            for user in users:
                if len(user) != 6:
                    print(f'incorrect format data {user}, string deleted, check manually')
                    users.remove(user)
                    # raise ValueError('Seems like some keys are missing')
        except TypeError:
            raise TypeError('Seems like your data type is incorrect (Expecting: [{}])')
    return users


def save_users_to_json_file(filename: str, data: list) -> str:
    with open(filename, 'w') as f:
        json.dump(data, f)
