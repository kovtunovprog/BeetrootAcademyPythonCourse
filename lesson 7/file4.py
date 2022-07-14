days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
my_dict_1 = {key:value for key,value in enumerate(days, start=1)}
my_dict_2 = {value:key for key,value in enumerate(days, start=1)}
print(my_dict_1)
print(my_dict_2)