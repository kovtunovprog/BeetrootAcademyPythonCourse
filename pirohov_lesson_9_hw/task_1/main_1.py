from pirohov_lesson_9_hw.task_1.user_balance_fix import balance_fix


def from_tuple_to_dict(users: list) -> list:
    head = users.pop(0)
    for ind, user in enumerate(users):
        users[ind] = {}
        for i in range(len(head)):
            users[ind][head[i]] = user[i]
    return users


def spent_add(users: list) -> list:
    for i in users:
        i['spent'] = 0
    return users


def from_dict_to_tuple(users: list) -> list:
    head = tuple([i for i in users[0]])
    for ind, user in enumerate(users):
        users[ind] = tuple([i for i in user.values()])
    users.insert(0, head)
    return users


def main():
    from alphabase import users_2 as users

    users = list(users)

    if type(users[0]) == tuple:
        users = from_tuple_to_dict(users)

    if 'spent' not in users[0]:
        spent_add(users)

    users = balance_fix(users)

    how_to_output = input('How to output? (1) - Tuple (tuples) or (2) - Tuple (dicts)\n')

    if how_to_output == '1':
        print(tuple(from_dict_to_tuple(users)))
    else:
        print(tuple(users))


if __name__ == '__main__':
    main()
