def convert_str_to_dict():
    mytext = input('Put sentence for convert from str to dict:\n')
    mylist = [word for word in mytext.split()]
    return {key: value for (key, value) in zip(range(len(mylist)),mylist)}

print(convert_str_to_dict())
