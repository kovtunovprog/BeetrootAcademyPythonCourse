#Make a program that has some sentence (a string) on input and returns
#a dict containing all unique words as keys and the number of occurrences as values.

str = 'a big black cat jumped on a big dog that doesnt like big black cats'
counts = dict()
words = str.split()
for i in words:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
print(counts)