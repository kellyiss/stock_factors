# coding=utf-8
import numpy as np


def CO(stock_list, cycle):
    """
    :param stock_list: [wHigh,wLow,wClose,wVolumn]
    :return: 一条时间线的C值
    """
    assert cycle < len(stock_list)

    temp1 = []
    temp2 = []
    AC_list = [0]
    for i in range(0, len(stock_list)):
        x = (stock_list[i][2] - stock_list[i][1] -
             stock_list[i][0] + stock_list[i][2]) / \
            (stock_list[i][0] - stock_list[i][1]) \
            * stock_list[i][3]
        temp1.append(x)

    for i in range(cycle, len(temp1) + 1):
        temp2.append(np.sum(temp1[i - cycle:i]))

    for i in range(1, len(temp2) + 1):
        AC_list.append(AC_list[i - 1] + temp2[i - 1])

    return AC_list;
