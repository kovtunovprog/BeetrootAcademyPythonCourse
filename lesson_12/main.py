from lesson_12.find_cheaters import find_cheaters
from lesson_12.update_balance import update_users_balances
from lesson_12.utils import parse_users_form_json_file


FILENAME: str = ""  # TODO: Set value to run program


def main():
    users = parse_users_form_json_file(FILENAME)
    cheaters = find_cheaters(users)
    update_users_balances(cheaters)
