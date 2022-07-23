from cource.lesson_12.find_cheaters import find_cheaters
from cource.lesson_12.update_balance import update_users_balances
from cource.lesson_12.utils import parse_users_form_json_file, save_users_to_json_file

INPUT_FILENAME: str = "resources/incorrect_format_2.json"  #
OUTPUT_FILENAME: str = "result.json"


def main():
    users = parse_users_form_json_file(INPUT_FILENAME)

    cheaters = find_cheaters(users)

    updated_users = update_users_balances(cheaters)

    save_users_to_json_file(OUTPUT_FILENAME, updated_users)


if __name__ == '__main__':
    main()
