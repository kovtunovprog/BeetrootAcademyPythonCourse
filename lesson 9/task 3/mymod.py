
def count_lines(name):
    file = open(name,'r')
    print(len(file.readlines()))
def count_chars(name):
    file = open(name,'r')
    print(len(file.read()))
def test(name):
    count_lines(name)
    count_chars(name)

