from functools import reduce


def digital_root(n):
    '''In this kata, you must create a digital root function.

    A digital root is the recursive sum of all the digits in a number. Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced. This is only applicable to the natural numbers.'''

    n = [int(x) for x in str(n)]
    result = n if len(n) > 1 else 0
    while result != 0 and len(result) > 1:
        temp = reduce(lambda x, y: x + y, result)
        result = [int(x) for x in str(temp)]

    return sum(result) if result != 0 else 0
