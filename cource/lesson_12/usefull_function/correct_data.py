def pop_incorrect_data(users: list) -> tuple:
    incorrect_users = []
    for i in range(len(users)-1, -1, -1):
        if len(users[i]) != len(users[0]):
            incorrect_users.append(users.pop(i))
    if incorrect_users:
        print('Incorrect users:',*incorrect_users[::-1], sep='\n')
    return tuple(incorrect_users[::-1])


def spent_add(users: list) -> list:
    for user in users:
        user['spent'] = 0
    return users
