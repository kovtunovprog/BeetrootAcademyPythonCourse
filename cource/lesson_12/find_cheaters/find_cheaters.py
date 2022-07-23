def find_cheaters(users: list) -> list:
    cheaters = []
    for user in users:
        print(f'Checking user id:{user["id"]} name: {user["name"]}')
        if int(user['balance']) != (int(user['level']) + int(user['kills'])) * 1000 - int(user['spent']):
            print(f'User ID:{user["id"]} name: {user["name"]} is cheater')
            cheaters.append(user)
        else:
            print(f'User id:{user["id"]} name: {user["name"]} is not a cheater')
    return cheaters
