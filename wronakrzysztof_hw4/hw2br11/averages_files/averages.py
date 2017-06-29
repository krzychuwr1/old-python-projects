from averages_files.integer import integer as int
from averages_files.get_data import len


def arithmetic(ingredients, wages):
    """For given ingredients and their wages
    counts arithmetic average.

    :param ingredients: list of integers
    :param wages: list of positive integers
    :return: integer
    """
    sum = 0
    wage = 0
    for i in range(len(ingredients)):
        wage += wages[i]
        sum += int(wages[i])*int(ingredients[i])
    average = sum/wage
    return average


def geometric(ingredients, wages):
    """For given ingredients and their wages
    counts geometric average.

    :param ingredients: list of positive integers
    :param wages: list of positive integers
    :return: integer
    """
    average = 1
    wage = 0
    for i in range(len(ingredients)):
        average = int(average) * int(ingredients[i])**wages[i]
        wage += wages[i]
    average = average**(1/wage)
    return average


def harmonic(ingredients, wages):
    """For given ingredients and their wages
    counts harmonic average.

    :param ingredients: list of positive integers
    :param wages: list of positive integers
    :return: integer
    """
    average = 0
    wage = 0
    for i in range(len(ingredients)):
        average = average + int(wages[i])/int(ingredients[i])
        wage += wages[i]
    average = wage/average
    return average


def rms(ingredients, wages):
    """For given ingredients and their wages
    counts rms average.

    :param ingredients: list of integers
    :param wages: list of positive integers
    :return: integer
    """
    average = 0
    wage = 0
    for i in range(len(ingredients)):
        wage += wages[i]
        average += int(wages[i]) * int(ingredients[i]**2)
    average = average / wage
    average = average**(1/2)
    return average
