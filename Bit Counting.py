def countBits(n):
    result = sum([int(i) for i in "{0:b}".format(n) if i == "1"])
    return result

print(countBits(4))