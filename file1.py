#Task 1
#Make a program that has some sentence (a string) on input and returns a dict
#containing all unique words as keys and the number of occurrences as values.

string = input('Input your string, please\n').split()
k = set(string)
values = []
dictionary = {}
for element in k:
    dictionary[element] = string.count(element)
print(dictionary)