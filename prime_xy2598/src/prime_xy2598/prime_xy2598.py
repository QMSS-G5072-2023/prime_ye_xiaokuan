import math

def is_prime(n):
    """
    Checks if a given number is a prime number.

    Parameters:
    -----------
    n : int
        The integer to be checked for primality.

    Returns:
    -------
    bool
        Returns True if the integer is prime, otherwise returns False.

    Examples:
    --------
    >>> is_prime(2)
    True

    >>> is_prime(4)
    False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
