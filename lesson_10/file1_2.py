def oops2():
    raise KeyError()
    print(list(range(2))[2])


def call_oops2():
    try:
        oops2()
    except IndexError:
        print('Error was caught!')
    finally:
        print('Unexpectedly!')


call_oops2()
