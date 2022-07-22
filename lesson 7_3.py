# List comprehension exercise
#
# Use a list comprehension to make a list containing tuples (i, j)
# where `i` goes from 1 to 10 and `j` is corresponding to `i` squared.

import random
lst = []
k = 0
while k < 5:
    i = random.randrange(1, 10)
    j = i * i
    lst.insert(k, (i, j))
    k += 1

print(lst)