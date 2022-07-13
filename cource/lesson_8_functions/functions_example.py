users = (
    ("id", "name", "balance", "level", "kills"),
    ("1", "Bilbo", "4000", "2", "4"),
    ("2", "Indigo", "42600", "40", "100"),
    ("3", "Farmer", "5000", "3", "2"),
    ("4", "O'rizotto", "5000", "1", "0"),
    ("5", "Bilbo-1", "0", "1", "0"),
    ("6", "Bilbo-2", "0", "1", "0"),
    ("7", "Bilbo-3", "0", "1", "0"),
    ("8", "O'rizotto-1", "0", "1", "0"),
    ("9", "O'rizotto-2", "0", "1", "0"),
    ("10", "O'rizotto-3", "0", "1", "0"),
    ("11", "O'rizotto-4", "0", "1", "0"),
    ("12", "Bilbo-1", "4200", "2", "1"),
    ("13", "GlobalLogic", "720500", "353", "440")
)


def check_user_is_cheater(user) -> bool:
    # return True or False
    # user example ("1", "Bilbo", "4000", "2", "4")
    ...


def update_user_balance(user):
    ...


def format_input_to_list(users_table):
    return []  # TODO: Not NotImplemented


def report_user_status(user, status):
    ...


def main():
    for user in format_input_to_list(users):
        # handle header

        is_cheater = check_user_is_cheater(user)
        if is_cheater:
            update_user_balance(user)
        report_user_status(user, is_cheater)


if __name__ == '__main__':
    main()
