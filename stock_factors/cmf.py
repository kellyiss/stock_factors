# coding=utf-8
import numpy as np


def CMF(stock_list, cycle):
    """
    蔡金货币流量
    :param stock_list:[wHigh,wLow,wClose,wVolumn]
    :param cycle:
    :return:返回的是一个时间线的值
    """
    assert cycle < len(stock_list)
    temp = []
    C_list = []
    for i in range(0, len(stock_list)):
        x = (stock_list[i][2] - stock_list[i][1] -
             stock_list[i][0] + stock_list[i][2]) / \
            (stock_list[i][0] - stock_list[i][1]) \
            * stock_list[i][3]
        temp.append(x)

    for i in range(cycle, len(temp) + 1):
        C_list.append(np.sum(temp[i - cycle:i]) \
                      / np.sum(stock_list[3][i - cycle:i]))

    return C_list
