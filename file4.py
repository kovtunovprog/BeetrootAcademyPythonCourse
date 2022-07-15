#Task 4
#Створити лист із днями тижня.
#В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
#Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,
lst = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
week_dict1 = {}
week_dict2 = {}
for key in range(0, 7):
    week_dict1[key] = lst[key]
print(week_dict1)
week_dict2 = {value: key for key, value in week_dict1.items()}
print(week_dict2)