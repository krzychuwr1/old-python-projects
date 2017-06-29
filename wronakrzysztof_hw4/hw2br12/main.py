from ProgramModules import game, sieve, encrypt
import doctest


__author__ = 'Przemek'


def display_menu():
    """
    Displays menu
    example:
    >>> display_menu()
    <BLANKLINE>
    Select module (or q to quit):
    1. Guessing game - break in to high security vault.
    2. Search for prime numbers.
    3. Encrypt your password.

    :return:
    """
    print("\nSelect module (or q to quit):")
    print("1. Guessing game - break in to high security vault.")
    print("2. Search for prime numbers.")
    print("3. Encrypt your password.")

doctest.testmod()
print("Author of this, so called \"program\", had no idea what to do, this is why it does everything, roughly speaking.")
while True:
    display_menu()
    str = input()
    if str == "1":
        game.play()
    elif str == "2":
        sieve.search()
    elif str == "3":


        encrypt.encrypt()
    elif str == "q":
        print("Bye bye!")
        exit(0)
    else:
        print("Wrong input! Try again.")
