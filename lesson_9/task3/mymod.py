def count_lines(name):
    f = open(name, "r")
    print('Кількість рядків: ', len(f.readlines()))
    return len(f.readlines())

def count_chars(name):
    f = open(name, "r")
    my_str = f.read()
    print('Кількість символів включно з пробілами: ', len(my_str))
    return len(my_str)

def test(name):
    count_lines(name)
    count_chars(name)