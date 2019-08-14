def function(mapping):
    """ Interprets a dictionary as a function.

    :param mapping: Dictionary.
    :return: Constructed function.

    >>> f = function({1: -1, 2: -2})
    >>> f(1) + f(2)
    -3

    >>> f = function({(1, 2): 3})
    >>> f(1, 2)
    3

    >>> f = function({1: 2})
    >>> f(42)
    Traceback (most recent call last):
        ...
    KeyError: 42
    """

    def value(*key):
        return \
            mapping[key[0]] if len(key) == 1 else \
            mapping[key]

    return value


def measure(f):
    """ Measures execution time of the specified function.

    :param f: Function to measure.
    :return: Execution time in seconds.
    """

    from time import time

    x = time()
    f()
    y = time()

    return y - x
