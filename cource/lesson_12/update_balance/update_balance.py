def update_users_balances(users: list) -> list:
    for i in users:
        if int(i["balance"] != i[("level" + "kills") * 1000 - "spent"]):
            return
