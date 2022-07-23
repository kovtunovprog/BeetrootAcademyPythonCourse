def update_users_balances(users: list) -> list:
    for user in users:
        print(f'Updating balance for user id:{user["id"]} name: {user["name"]}')
        user['balance'] = (int(user['level']) + int(user['kills'])) * 1000 - int(user['spent'])
    return users
