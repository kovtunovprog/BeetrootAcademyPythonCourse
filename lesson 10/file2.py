# Write a function that takes in two numbers from the user via input(), 
# call the numbers a and b, and then returns the value of squared a divided by b, 
# construct a try-except block which raises an exception if the two values given 
# by the input function were not numbers, and if value b was zero (cannot divide by zero).    


def numbers():
    num = []
    for x in range(2):
       num.append(input('PLease write number #' + str(x+1) + ': '))
    try:
        a = int(num[0])
        b = int(num[1])
        num = a*a/b 
        print(num)
    except ValueError: 
        print('not a number')
    except ZeroDivisionError: 
        print('please don\'t use 0, or I will find you and divide you by 0')

numbers()
