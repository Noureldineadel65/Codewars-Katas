def camel_case(string):
    '''Write simple .camelCase method (camel_case function in PHP, CamelCase in C# or camelCase in Java) for strings. All words must have their first letter capitalized without spaces.'''
    '''https://www.codewars.com/kata/camelcase-method/train/python'''
    return string.title().replace(" ", "")


print(camel_case('ok wow'))
