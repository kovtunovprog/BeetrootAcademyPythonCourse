# Створити лист із днями тижня.
# В один рядок (ну або як завжди) створити словник виду: {1: “Monday”, 2:...
# Також в один рядок або як вдасться створити зворотний словник {“Monday”: 1,

a = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

b = {}
for c in range(0, len(a)):
    b.update({c + 1: a[c]})
print(b)

# Reverse
d = {}
for e in range(0, len(a)):
    d.update({a[e]: e + 1})
print(d)
