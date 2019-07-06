def iq_test(numbers):
    '''Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.'''
    '''https://www.codewars.com/kata/552c028c030765286c00007d/train/python'''
    numbers = numbers.split(' ')
    result = [int(i) for i in numbers if int(i) % 2 == 0]
    return numbers.index("".join(list(dict.fromkeys("".join([i for i in numbers if int(i) not in result]))))) + 1


print(iq_test("88 96 66 51 14 88 2 92 18 72 18 88 20 30 4 82 90 100 24 46"))
