"""
* Binary Exponentiation with Multiplication
* This is a method to find a*b in a time complexity of O(log b)
* This is one of the most commonly used methods of finding result of multiplication.
* Also useful in cases where solution to (a*b)%c is required,
* where a,b,c can be numbers over the computers calculation limits.
* Done using iteration, can also be done using recursion

* @author chinmoy159
* @version 1.0 dated 10/08/2017
"""


def b_expo(a: int, b: int) -> int:
    """
    Calculate the result of multiplying 'a' and 'b' using bitwise multiplication.
    Parameters:
    a (int): The first number.
    b (int): The second number.
    Returns:
    int: The result of 'a' multiplied by 'b'.
    Examples:
    >>> b_expo(2, 3)
    6
    >>> b_expo(5, 0)
    0
    >>> b_expo(3, 4)
    12
    >>> b_expo(10, 5)
    50
    >>> b_expo(0, 5)
    0
    >>> b_expo(2, 1)
    2
    >>> b_expo(1, 10)
    10
    """
    res = 0
    while b > 0:
        if b & 1:
            res += a

        a += a
        b >>= 1

    return res


if __name__ == "__main__":
    import doctest

    doctest.testmod()


def b_expo_mod(a: int, b: int, c: int) -> int:
    res = 0
    while b > 0:
        if b & 1:
            res = ((res % c) + (a % c)) % c

        a += a
        b >>= 1

    return res


"""
* Wondering how this method works !
* It's pretty simple.
* Let's say you need to calculate a ^ b
* RULE 1 : a * b = (a+a) * (b/2) ---- example : 4 * 4 = (4+4) * (4/2) = 8 * 2
* RULE 2 : IF b is ODD, then ---- a * b = a + (a * (b - 1)) :: where (b - 1) is even.
* Once b is even, repeat the process to get a * b
* Repeat the process till b = 1 OR b = 0, because a*1 = a AND a*0 = 0
*
* As far as the modulo is concerned,
* the fact : (a+b) % c = ((a%c) + (b%c)) % c
* Now apply RULE 1 OR 2, whichever is required.
"""
