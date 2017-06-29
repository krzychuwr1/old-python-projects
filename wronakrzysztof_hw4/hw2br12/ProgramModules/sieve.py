__author__ = 'Przemek'


def search():
    """
    asks user for range limit and then prints all prime numbers smaller or equal to range limit.
    :return:
    """
    limit = input('How broad your range will be: ')
    limit = int(limit)
    numbers = list(range(2, limit + 1))
    for prime in numbers:
        for multiple in range(2 * prime, limit + 1, prime):
            if multiple in numbers:
                numbers.remove(multiple)
    print("Prime numbers in given range (max: {0}):".format(limit))
    print(numbers)