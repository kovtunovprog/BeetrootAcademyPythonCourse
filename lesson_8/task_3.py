def make_operation(arithmetic_operator, *args):
    result = args[0]
    for i in args[1:]:
        if arithmetic_operator == "+":
            result += i
        if arithmetic_operator == "-":
            result -= i
        if arithmetic_operator == "*":
            result *= i
    return result
print(make_operation("+", 1, 1, 1))
print(make_operation("+", 7, 7, 2))
print(make_operation("-", 5, 5, -10, -20))
print(make_operation("*", 7, 6))