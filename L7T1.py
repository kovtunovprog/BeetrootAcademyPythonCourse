# Make a program that has some sentence (a string) on input and returns
# a dict containing all unique words as keys and the number of occurrences as values.

a = (input('Enter your text here:\n').split(' '))
b = {}

for i in a:
    b.update({i: a.count(i)})

print(b)
