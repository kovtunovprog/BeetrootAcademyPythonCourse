def count_lines(name):
    file = open(name, 'r')
    return len(file.readlines())
def count_chars(name):
    count_of_lines = len(open(name, 'r').readlines())
    count_of_chars_with_enters = len((open(name, 'r').read()))
    count_of_chars = count_of_chars_with_enters - count_of_lines + 1
    return count_of_chars
def test(name):
    print(count_lines(name))
    print(count_chars(name))
