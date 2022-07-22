# Write a function called oops that explicitly raises an IndexError exception when called. 
# Then write another function that calls oops inside a try/except state­ment to catch the error.
# What happens if you change oops to raise KeyError instead of IndexError?

def oops():
    # cats_count = {'Nat': 3, 'Sam': 2, 'Ivan': 73}
    # cats_count['Lera']
    # KeyError

    name = []
    name[1]
    IndexError

def press_f():
    try:
        oops() 
    except IndexError:
        print('IndexError - done')
    except:
        print('KeyError - done')
press_f()


