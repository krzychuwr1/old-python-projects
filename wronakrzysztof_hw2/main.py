from fibo_range import *
__author__ = 'krzychuwr'

print()  # print short instruction for the user
print("What do you want to print? Range of fibonacci numbers or just a range of numbers?")
print("For fibonacci numbers write one of the following, for normal anything else:")
choice.print_tuple()
user_choice = input()  # get user choice of numbers

minimum = 0  # minimum is defined here so that it's visible outside try
while True:  # keep asking for beginning of range >= 0
    print("Beginning of the range has to be at least 0.")
    try:
        minimum = int(input("Beginning of the range:"))
        if minimum >= 0:
            break
    except:
        print("Incorrect string, please try again.")

maximum = 0  # maximum is defined here so that it's visible outside try
while True:  # keep asking for end of range >= beginning
    print("End of the range can't be smaller than the beginning.")
    try:
        maximum = int(input("End of the range: "))+1
        if maximum > minimum: break
    except:
        print("Incorrect string, please try again.")


if choice.is_fibonacci(user_choice):  # if user chose fibonacci numbers, prints range of them
    fibo_numbers.print_range(minimum, maximum)
else:  # if user chose normal numbers, prints range of them
    normal_numbers.print_range(minimum, maximum)
