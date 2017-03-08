def hammingDistance(x, y):
    """
    :type x: int
    :type y: int
    :rtype: int
    """
    ret = 0
    xb = bin(x)
    yb = bin(y)
    if x.bit_length() < y.bit_length():
        xbe = '0b' + str('0' * (y.bit_length() - x.bit_length())) + xb[2:]
        ybe = yb
    else:
        xbe = xb
        ybe = '0b' + str('0' * (x.bit_length() - y.bit_length())) + yb[2:]
    for i in range(len(xbe)):
        print(xbe)
        if xbe[i] != ybe[i]:
            ret += 1
        else:
            pass
    return ret


print(hammingDistance(1, 4))
