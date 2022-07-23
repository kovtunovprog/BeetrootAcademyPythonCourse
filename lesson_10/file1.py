def oops():
    print(list(range(2))[2])


def call_oops():
    try:
        oops()
    except IndexError:
        print('Error was caught!')


call_oops()
