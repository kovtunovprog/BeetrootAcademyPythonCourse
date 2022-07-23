from cource.lesson_12.usefull_function import pop_incorrect_data,from_tuple_to_dict, spent_add, collect_cheaters


def find_cheaters(users: list) -> list or str:

    incorrect_users = pop_incorrect_data(users)  # I think we will need incorrect users in the future

    if type(users[0]) == tuple:
        from_tuple_to_dict(users)

    if 'spent' not in users[0]:
        spent_add(users)

    cheaters = collect_cheaters(users)

    return cheaters if cheaters else print('There is no cheaters!')


find_cheaters(users_2)