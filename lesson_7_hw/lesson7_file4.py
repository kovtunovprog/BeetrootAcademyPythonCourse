week_days = [
    'monday',
    'tuesday',
    'thursday',
    'wednesday',
    'friday',
    'saturday',
    'sunday'
]
# first approach
# week_days_dict = {}
# week_days_dict_rev = {}
# value = 1
# for key in week_days:
#     week_days_dict.update({key: value})
#     week_days_dict_rev.update({value: key})
#     value += 1

# second approach
week_days_dict = {key: value for (key, value) in zip(week_days, range(1,8))}
week_days_dict_rev = {value: key for (value, key) in zip(range(1, 8), week_days)}

print(week_days_dict)
print(week_days_dict_rev)