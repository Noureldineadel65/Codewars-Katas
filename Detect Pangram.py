import string


def is_pangram(s):
    '''A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).'''
    '''https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python'''
    return set(s.lower()) >= set(string.ascii_lowercase)
