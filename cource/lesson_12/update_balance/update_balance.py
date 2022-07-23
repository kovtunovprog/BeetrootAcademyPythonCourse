def update_users_balances(users: list) -> list:
    for i in users:
        print(f'Updating balance for user id:{i["id"]} name: {i["name"]}')
        i['balance'] = (int(i['level']) + int(i['kills'])) * 1000 - int(i['spent'])
    return users
