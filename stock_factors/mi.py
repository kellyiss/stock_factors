# coding=utf-8
import ema
import numpy as np


def MI(stock_list, cycle):
    """
    :param stock_list: [[wHigh,wLow,wClose]...]
    :return:
    """
    assert cycle < len(stock_list)
    MI_list = []
    temp1 = []
    for i in range(0, len(stock_list)):
        temp1.append(stock_list[i][0] - stock_list[i][1])

    v1 = ema.EMA(temp1, 9)
    v2 = ema.EMA(v1, 9)
    v1_array = np.array(v1)
    v2_array = np.array(v2)
    v3 = (v1_array / v2_array).tolist()

    for i in range(cycle, len(v3) + 1):
        MI_list.append(np.sum(v3[i - cycle:i]))

    return MI_list
