# Make a program that has some sentence (a string) on input
# and returns a dict containing all unique words as keys and the number of occurrences as values.


sentence = (input('Enter your sentence:\n').split(' '))
dict_sentence = {}

for value in sentence:
    dict_sentence.update({value: sentence.count(value)})

print(dict_sentence)