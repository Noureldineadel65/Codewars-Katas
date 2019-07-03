def array_diff(a, b):
    '''Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.'''
    '''https://www.codewars.com/kata/array-dot-diff/train/python'''
    result = [i for i in a if i not in b]
    return result


print(array_diff([1, 2], [1]))
