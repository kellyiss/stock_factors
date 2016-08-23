# coding=utf-8
import ema


def MO(wprice_list):
    """
    :param wprice_list:
    :return:
    """
    temp = []
    dif = []
    pos = 0
    neg = 0

    for pricesPerStock in wprice_list:
        temp.append([(pricesPerStock[i] - pricesPerStock[i - 1]) for i in range(1, len(pricesPerStock))])

    for j in range(0, len(temp[0])):
        pos = 0
        neg = 0
        for k in range(0, len(temp)):
            if temp[k][j] > 0:
                pos = pos + 1
            else:
                neg = neg + 1
        dif.append(pos - neg)

    ema19 = ema.EMA(dif, 19)
    ema39 = ema.EMA(dif, 39)
    mo = ema19[len(ema19) - 1] - ema39[len(ema39) - 1]
    return mo
