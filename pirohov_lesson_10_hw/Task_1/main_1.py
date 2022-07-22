def oops():
    raise IndexError

def catch():
    try:
        oops()
    except IndexError:
        print('Error caught in function oops!')

catch()


def oops2():
    raise KeyError

def catch2():
    try:
        oops2()
    except IndexError:
        print('Error caught!')


catch2()