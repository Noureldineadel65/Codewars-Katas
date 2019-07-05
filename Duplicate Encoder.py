import collections
def duplicate_encode(word):
    '''The goal of this exercise is to convert a string to a new string 
    where each character in the new string is "(" 
    if that character appears only once in the original string, 
    or ")" if that character appears more than once in the original string. Ignore capitalization when determining 
    if a character is a duplicate.'''
    counted = collections.Counter(word.lower())
    newstring = ""
    for i in word:
        if counted[i] == 1:
            newstring += "("
        else:
            newstring += ")"
    return newstring

print(duplicate_encode('recede'))
