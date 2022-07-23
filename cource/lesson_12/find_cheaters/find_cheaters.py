def find_cheaters(users: list) -> list:
    cheaters = []
    for i in users:
        print(f'Checking user id:{i["id"]} name: {i["name"]}')
        if int(i['balance']) != (int(i['level']) + int(i['kills'])) * 1000 - int(i['spent']):
            print(f'User ID:{i["id"]} name: {i["name"]} is cheater')
            cheaters.append(i)
        else:
            print(f'User id:{i["id"]} name: {i["name"]} is not a cheater')
    return cheaters
