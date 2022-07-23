def parse_users_form_json_file(filename: str) -> list:
    with open(filename, 'r') as file_object:
        f = json.load(file_object)
    return(f)


def save_users_to_json_file(filename: str, data: list) -> str:
    with open(filename, 'w') as data:
        json.dump(filename, data)
