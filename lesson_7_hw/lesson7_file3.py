# List comprehension exercise

list_of_tuples = [(i, i**2 ) for i in range(1, 11)]
list_of_tuples2 = [(i,j) for i in range(1, 11) for j in range(1, 101) if j == i**2]
print(list_of_tuples)
print(list_of_tuples2)
