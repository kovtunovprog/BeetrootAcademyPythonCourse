days = [
    'Monday', 'Tuesday', 'Wednesday',
    'Thursday', 'Friday', 'Saturday', 'Sunday'
]

dict_of_days = {i+1: days[i] for i in range(len(days))}
reversed_dict = {value: key for key, value in dict_of_days.items()}
'did not use line break or making the conditions of the task'

print(dict_of_days)
print(reversed_dict)
