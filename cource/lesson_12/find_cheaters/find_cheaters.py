def find_cheaters(users: list) -> list:
    cheaters = []
    for i in users:
        print() # TODO: checking
        if i['balance'] != (int(i['level']) + int(i['kills'])) * 1000 - int(i['spent']):
            print(f'Found cheater ID:{i["id"]} {i["name"]}')
            cheaters.append(i)
    return cheaters

