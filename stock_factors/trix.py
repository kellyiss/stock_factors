# coding=utf-8
import ma


def TRIX(price_list, cycle, M):
    """

    :param price_list: [wClose...]
    :param cycle:
    :param M:
    :return:
    """
    AX = [price_list[0] * 2 / (cycle + 1)]
    for i in range(1, len(price_list)):
        AX.append(price_list[i] * 2 / (cycle + 1) + AX[i - 1] * (cycle - 1) * (cycle + 1))

    BX = [AX[0] * 2 / (cycle + 1)]
    for i in range(1, len(AX)):
        BX.append(AX[i] * 2 / (cycle + 1) + BX[i - 1] * (cycle - 1) * (cycle + 1))

    TRIX = [BX[0] * 2 / (cycle + 1)]
    for i in range(1, len(BX)):
        TRIX.append(BX[i] * 2 / (cycle + 1) + TRIX[i - 1] * (cycle - 1) * (cycle + 1))

    TRMA = ma.MA(TRIX, M)

    return TRIX, TRMA
