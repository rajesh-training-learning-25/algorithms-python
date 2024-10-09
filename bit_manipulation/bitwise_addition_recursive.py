"""
Bit düzeyinde operatörler kullanarak iki negatif olmayan tam sayının toplamını hesaplar
Wikipedia açıklaması: https://en.wikipedia.org/wiki/Binary_number
"""


def bitwise_addition_recursive(number: int, other_number: int) -> int:
    """
    >>> bitwise_addition_recursive(4, 5)
    9
    >>> bitwise_addition_recursive(8, 9)
    17
    >>> bitwise_addition_recursive(0, 4)
    4
    >>> bitwise_addition_recursive(4.5, 9)
    Traceback (most recent call last):
        ...
    TypeError: Her iki argüman da tam sayı olmalıdır!
    >>> bitwise_addition_recursive('4', 9)
    Traceback (most recent call last):
        ...
    TypeError: Her iki argüman da tam sayı olmalıdır!
    >>> bitwise_addition_recursive('4.5', 9)
    Traceback (most recent call last):
        ...
    TypeError: Her iki argüman da tam sayı olmalıdır!
    >>> bitwise_addition_recursive(-1, 9)
    Traceback (most recent call last):
        ...
    ValueError: Her iki argüman da negatif olmamalıdır!
    >>> bitwise_addition_recursive(1, -9)
    Traceback (most recent call last):
        ...
    ValueError: Her iki argüman da negatif olmamalıdır!
    """

    if not isinstance(number, int) or not isinstance(other_number, int):
        raise TypeError("Her iki argüman da tam sayı olmalıdır!")

    if number < 0 or other_number < 0:
        raise ValueError("Her iki argüman da negatif olmamalıdır!")

    bitwise_sum = number ^ other_number
    carry = number & other_number

    if carry == 0:
        return bitwise_sum

    return bitwise_addition_recursive(bitwise_sum, carry << 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
