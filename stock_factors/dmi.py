# coding=utf-8
import numpy as np


def dmiPerDay(dif_list, cycle):
    pos = []
    neg = []
    for i in range(0, len(dif_list)):
        if (dif_list[i] > 0):
            pos.append(dif_list[i])
        else:
            neg.append(dif_list[i])
    up = np.sum(pos) / cycle + 1
    down = np.sum(neg) / cycle + 1
    result = 100 - 100 / ((1 + up / down))
    return result


def DMI(stock_list, cycle):
    """
    :param stock_list:[wopen...]
    :param cycle:
    :return:dmi list
    """
    DMI_list = []
    dif = []
    for i in range(1, len(stock_list)):
        dif.append(stock_list[i] - stock_list[i - 1])

    for i in range(cycle - 1, len(dif) + 1):
        DMI_list.append(dmiPerDay(dif[i - (cycle - 1):i], cycle - 1))

    return DMI_list
