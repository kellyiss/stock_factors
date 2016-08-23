# coding=utf-8
import numpy as np


def IMI(price_list, cycle):
    """
    :param price_list:[[wOpen,wClose]...]
    :param cycle:
    :return:
    """
    dif_list = []
    all_list = []
    for pricePerDay in price_list:
        dif = pricePerDay[1] - pricePerDay[0]
        if (dif > 0):
            dif_list.append(dif)
        all_list.append(abs(dif))

    imi = np.sum(dif_list) / np.sum(all_list)

    return imi
