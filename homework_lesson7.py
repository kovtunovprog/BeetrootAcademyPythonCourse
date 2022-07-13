
# Task 1
# sentence = input('Please enter a sentence:_')
# x = sentence.split()
# y = list(x)
# w = {}
# for i in y:
#     q = y.count(i)
#     print(q)
#     z = {i: q}
#     w[i] = q
#
# print(w)

# Task 2
#
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
#
# x = [stock[num]*prices[num] for num in stock]
# y = sum(x)
# print(y)

# Task 3
#
# x = [(i, i**2) for i in range(10)]
# print(x)

# Task 4

x = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
y = {}
z = {}
for k, day in enumerate(x):
    y[k+1] = day
    z[day] = k+1

print(y)
print(z)