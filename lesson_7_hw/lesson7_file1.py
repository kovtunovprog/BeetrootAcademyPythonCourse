import re
from pprint import pprint

inp_str = input("Write a sentence: ")
inp_str = inp_str.lower()            #make all chars in lower case
opt_str = re.sub(r'[^\w\s]','', inp_str) #remove all punctuation
inp_list = opt_str.split() # slice str by " "
my_dict = dict()
for key in inp_list:  #add all el in list as keys with counts in list as values
    my_dict.update({key: inp_list.count(key)})


pprint(my_dict)
