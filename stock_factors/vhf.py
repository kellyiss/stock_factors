# coding=utf-
import numpy as np


def VHF(price_list, cycle):
    """

    :param price_list:[wClose...]
    :param cycle:
    :return:
    """
    VHF_list = []
    dif = [abs((price_list[i] - price_list[i - 1])) for i in range(1, len(price_list))]
    abs_list = [(max(price_list[i - cycle:i]) - min(price_list[i - cycle:i])) for i in
                range(cycle, len(price_list) + 1)]
    sum_list = [sum(dif[i - cycle + 1:i]) for i in range(cycle - 1, len(dif) + 1)]
    VHF_list = (np.array(abs_list) / np.array(sum_list)).tolist()
    return VHF_list
