def filter_list(l):
    '''In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.'''
    '''https://www.codewars.com/kata/list-filtering/train/python'''
    result = [i for i in l if isinstance(i, int) or isinstance(i, float)]
    return result
