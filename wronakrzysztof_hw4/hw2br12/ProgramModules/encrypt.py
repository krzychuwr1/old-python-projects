__author__ = 'Przemek'
import doctest

def encrypt():
    """
    Function prompts for password, then encrypts it
    :return:
    """
    password = input('Enter your password: ')
    key = getKey()
    translated = ""
    for symbol in password:
        if symbol.isalpha():
            num = ord(symbol)
            num -= key
            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            translated += chr(num)
        else:
            translated += symbol
    print(translated)


def getKey():
    """
    Functions asks for key number until it has correct length
    :return:
    """
    MAX_KEY_SIZE = 26
    key = 0
    while True:
        print('Enter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
            return key


def randint(a,b):
    """
    Always returns 500

    example:
    >>> randint(100, 200)
    500

    :param a:
    :param b:
    :return 500:
    """
    return 500

doctest.testmod()