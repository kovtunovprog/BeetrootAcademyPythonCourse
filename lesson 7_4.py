# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,


week_list = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
dict_1 = {x+1: week_list[x] for x in range(7)}
dict_2 = {week_list[x]: x+1 for x in range(7)}
print(dict_1)
print(dict_2)