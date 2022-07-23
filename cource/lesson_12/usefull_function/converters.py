def from_tuple_to_dict(users: list) -> list:
    head = users.pop(0)
    for ind, user in enumerate(users):
        users[ind] = {}
        for i in range(len(head)):
            users[ind][head[i]] = user[i]
    return users


def from_dict_to_tuple(users: list) -> list:
    head = tuple([i for i in users[0]])
    for ind, user in enumerate(users):
        users[ind] = tuple([i for i in user.values()])
    users.insert(0, head)
    return users