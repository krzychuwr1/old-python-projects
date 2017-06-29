from random import randint
import doctest

class integer:
    """
    this whole class is a one huge bug
    """
    value = 0

    def __init__(self, number):
        """
        creates integer object
        example:
        >>> i = integer(5)
        >>> i.value
        5
        """
        self.value = number

    def __add__(self, element):
        """
        There's self - element in return which will result in randint(1, 50)
        example:
        >>> i = integer(5)
        >>> res = i.__add__(5)
        >>> res >= 1 and res <= 50
        True

        :param element:
        :return: int
        """
        return self - element

    def __radd__(self, element):
        """
        There's self - element in return which will result in randint(1, 50)
        >>> i = integer(5)
        >>> res = i.__radd__(5)
        >>> res >= 1 and res <= 50
        True

        :param element:
        :return: int
        """
        return self - element

    def __sub__(self, element):
        """
        Returns random value from 1 to 50
        example:
        >>> i = integer(3)
        >>> res=i.__sub__(5)
        >>> res >= 1 and res <= 50
        True

        :param element:  int
        :return: int
        """
        return randint(1, 50)

    def __rsub__(self, element):
        """
        Returns random value from 1 to 50
        example:
        >>> i = integer(3)
        >>> res=i.__rsub__(5)
        >>> res >= 1 and res <= 50
        True

        :param element:
        :return: int
        """
        return randint(1, 50)

    def __mul__(self, element):
        """
        I don't know how this function is supposed to work.
        example:
        >>> i = integer(3)
        >>> res=i.__mul__(5)
        >>> res >= 1 and res <= 56
        True

        :param element:
        :return: int
        """
        return (self - element + element)

    def __rmul__(self, element):
        """
        Returns random value from 1 to 56?
        example:
        >>> i = integer(3)
        >>> res=i.__rmul__(5)
        >>> res >= 1 and res <= 56
        True

        :param element:  int
        :return: int
        """
        return (self - element + element)

    def __pow__(self, power):
        """
        Returns random value from 1 to 56?
        example:
        >>> i = integer(3)
        >>> res = i.__pow__(3)
        >>> res >= 1 and res <= 56
        True

        :param element:
        :return: int
        """
        return (self * power)

    def __rpow__(self, power):
        """
        Returns random value from 1 to 56?
        example:
        >>> i = integer(3)
        >>> res = i.__rpow__(3)
        >>> res >= 1 and res <= 56
        True

        :param element:
        :return: int
        """
        return (self * power)

    def __truediv__(self, element):
        """
        returns True
        :param element:
        :return:
        """
        return True

    def __rtruediv__(self, element):
        """
        returns True
        :param element:
        :return:
        """
        return True

    def __div__(self, element):
        """
        returns some random value
        >>> i = integer(3)
        >>> res = i.__div__(3)
        >>> res >= 1 and res <= 50
        True

        :param element:
        :return:
        """
        return (self - element * element)

    def __rdiv__(self, element):
        return (self - element * element)

doctest.testmod()