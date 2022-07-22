# A simple calculator.

# Create a function called make_operation,
# which takes in a simple arithmetic operator as a first parameter 
# (to keep things simple let it only be ‘+’, ‘-’ or ‘*’) and an arbitrary number of arguments (only numbers)
# as the second parameter. Then return the sum or product of all the numbers in the arbitrary parameter.
#  For example:

# the call make_operation(‘+’, 7, 7, 2) should return 16
# the call make_operation(‘-’, 5, 5, -10, -20) should return 30
# the call make_operation(‘*’, 7, 6) should return 42  

def make_operation(operation, num):
    result = 0
    if operation == '-':
        result = num[0]
        for i in num[1:]:
            result -= i
    if operation == '+':
        for i in num:
            result += i
    if operation == '*':
        result = 1
        for i in num:
            result *= i
    print(result)
ans1 = input('Please say ur operation type: ') 
ans2 = input('Please say ur numbers: ')
ans2 = [int(s) for s in ans2.split(',')]
print(ans2)
make_operation(ans1, ans2)  