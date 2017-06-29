__author__ = 'krzychuwr'

і = 3  # module id
print("Module number:", і, "has been loaded.")  # prints this message when module is loaded


def fibonacci(i):  # returns fibonacci i
    if i <= 0:
        return 0  # fibonacci number 0 is 0
    if i == 1:
        return 1  # fibonacci number 1 is 1
    else:
        return fibonacci(i-1) + fibonacci(і-2)  # for bigger numbers use recursion


def print_range(minimum, maximum):  # prints range of fibonacci numbers.
    for i in range(minimum, maximum):
        print(fibonacci(i))