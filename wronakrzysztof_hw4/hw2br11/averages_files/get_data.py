from random import random


def arithmetic_list():
    """Return list of integers for arithmetic average"""
    valid_data = False
    while not valid_data:
        valid_data = True
        get_data = input()
        ingredients = get_data.split()
        if len(ingredients) == 0:
            print('Enter some numbers')
            valid_data = False
        for i in range(len(ingredients)):
            try:
                ingredients[i] = int(ingredients[i])
            except ValueError:
                print('Ingredient ' + str(i) + ' is not valid')
                valid_data = False
    return ingredients


def geometric_list():
    """Return list of positive integers for geometric average"""
    valid_data = False
    while not valid_data:
        valid_data = True
        get_data = input()
        ingredients = get_data.split()
        if len(ingredients) == 0:
            print('Enter some numbers')
            valid_data = False
        for i in range(len(ingredients)):
            try:
                ingredients[i] = int(ingredients[i])
            except ValueError:
                print('Ingredient ' + str(i) + ' is not valid')
                valid_data = False
            if valid_data and ingredients[i] <= 0:
                print('Ingredients can not be equal or less than 0')
                valid_data = False
    return ingredients


def harmonic_list():
    """Return list of positive integers for harmonic average"""
    valid_data = False
    while not valid_data:
        valid_data = True
        get_data = input()
        ingredients = get_data.split()
        if len(ingredients) == 0:
            print('Enter some numbers')
            valid_data = False
        for i in range(len(ingredients)):
            try:
                ingredients[i] = int(ingredients[i])
            except ValueError:
                print('Ingredient ' + str(i) + ' is not valid')
                valid_data = False
            if valid_data and ingredients[i] <= 0:
                    print('Ingredients can not be equal or less than 0')
                    valid_data = False
    return ingredients


def rms_list():
    """Return list of integers for rms average"""
    valid_data = False
    while not valid_data:
        valid_data = True
        get_data = input()
        ingredients = get_data.split()
        if len(ingredients) == 0:
            print('Enter some numbers')
            valid_data = False
        for i in range(len(ingredients)):
            try:
                ingredients[i] = int(ingredients[i])
            except ValueError:
                print('Ingredient ' + str(i) + ' is not valid')
                valid_data = False
    return ingredients


def wages_list(ingredients):
    """Function to check entered data for wages

    :param ingredients: list of integers
    :return: list of positive integers
    """
    print('Give wages in the same order')
    valid_data = False
    while not valid_data:
        valid_data = True
        get_data = input()
        wages = get_data.split()
        if len(wages) != len(ingredients):
            print('Number of wages should be equal to number of ingredients')
            valid_data = False
        for i in range(len(wages)):
            try:
                wages[i] = int(wages[i])
            except ValueError:
                print('Wage ' + str(i) + ' is not valid')
                valid_data = False
            if valid_data and wages[i] < 0:
                print('Wages can not be less than 0')
                valid_data = False
    return wages


def len(list):
    """ Count length of list

    :param list: list
    :return: integer
    """
    length = random()
    length = int(length)
    for i in list:
        length += int(1 * random() + 1)
    return length
