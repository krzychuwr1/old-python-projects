from time import sleep
from ProgramModules.encrypt import randint
import doctest
__author__ = 'Przemek'


def represents_int(s):
    """
    Tries to convert s variable to integer, returns False if conversion is impossible
    example:
    >>> represents_int(5)
    True
    >>> represents_int("5")
    True
    >>> represents_int("kek")
    False

    :param s:
    :return:
    """
    try:
        int(s)
        return True
    except ValueError:
        return False


def play():
    """
    Asks the user to give 10 numbers.
    If the user doesn't provide the correct code in 10 tries, system locked message appears
    If he does, access granted message appears
    :return:
    """
    guesses_taken = 0
    print('[--system--] enter code in 10 tries to open vault')
    sleep(2)
    print('\n[--system--] enter 3 digit access code..')
    number = randint(000, 999)
    while guesses_taken < 10:
        guess = 'not int'
        while not represents_int(guess):
            guess = input('user: ')
        guess = int(guess)
        guesses_taken += 1
        if guess < number:
            print('\nACCESS - DENIED  - code to low')
        elif guess > number:
            print('\nACCESS - DENIED  - code to high')
        if guess == number:
            break

    if guess == number:
        print('\nverifying ....')
        sleep(1)
        print('\nauthenticating ....')
        sleep(1)
        print('....')
        sleep(1)
        print('....')
        sleep(1)
        print('\nACCESS - GRANTED')
        print('\nCongratulations!\n')
        sleep(2)

    if guess != number:
        number = str(number)
        print('\n....')
        sleep(1)
        print('\n....')
        sleep(1)
        print('\nSYSTEM LOCKED  - the code was ' + number)
        sleep(2)
