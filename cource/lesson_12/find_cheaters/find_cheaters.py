def find_cheaters(users: list) -> list:
    for i in users:
        balance_max = (i['level'] + i['kills']) * 1000 - i['spent']
        try:
            if i['balance'] != balance_max:
                raise NotImplementedError as err
        except NotImplementedError:
            print(err)
        continue
