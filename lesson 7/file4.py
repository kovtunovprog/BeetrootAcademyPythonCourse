# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days_dict = {n: name for n, name in enumerate(days, 1)}
days_dict_reverse = {name: n for n, name in days_dict.items()}
print(days_dict_reverse)
