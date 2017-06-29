__author__ = 'krzychuwr'

i = 1  # module id
fibonacci_tuple = {'fibo', 'fibonacci', 'fib', 'fi', '1', 'first choice', 'first', 'f'}
print("Module number:", i, "has been loaded.")  # prints this when module has been loaded


def print_tuple():  # prints strings which result in choosing fibonacci option
    print(fibonacci_tuple)


def is_fibonacci(user_input):  # analyze user input
    return user_input in fibonacci_tuple
