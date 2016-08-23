# coding=utf-8

def ABI(all_prices):
    """
    :param all_prices:
    1 2 3
    4 5 6
    7 8 9
    :return:
    """
    temp = []
    result = []
    pos = 0
    neg = 0

    for pricesPerStock in all_prices:
        temp.append([(pricesPerStock[i] - pricesPerStock[i - 1]) for i in range(1, len(pricesPerStock))])

    for j in range(0, len(temp[0])):
        pos = 0
        neg = 0
        for k in range(0, len(temp)):
            if temp[k][j] > 0:
                pos = pos + 1
            else:
                neg = neg + 1
        result.append(abs(pos - neg))

    return result
