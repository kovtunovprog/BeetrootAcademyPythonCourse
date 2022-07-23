def find_cheaters(users: list) -> list:
    for i in users:
        balance_max = (int(i['level']) + int(i['kills'])) * 1000 - int(i['spent'])
        try:
            if int(i['balance']) != balance_max:
                raise NotImplementedError ('NotImplementedError')
        except NotImplementedError:
            print('NotImplementedError')
        continue

