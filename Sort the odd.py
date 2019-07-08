def sort_array(source_array):
    '''You have an array of numbers.
    Your task is to sort ascending odd numbers but even numbers must be on their places.

    Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.'''
    '''https://www.codewars.com/kata/578aa45ee9fd15ff4600090d/train/python'''
    result = sorted(list(filter(lambda x: x % 2 != 0, source_array)))
    for i, x in enumerate(source_array):
        if x % 2 == 0:
            result[i:i] = [x]
    return result
