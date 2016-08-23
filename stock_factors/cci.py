# coding=utf-8
import ma
import numpy as np


def CCI(stock_list, cycle):
    """
    :param stock_list: [[wHigh,wLow,wClose]...]
    :param cycle:
    :return:返回cycle-1个值
    """
    TP = []
    closePrice = []
    temp1 = []
    MD_list = []
    CCI_list = []

    for i in range(0, len(stock_list)):
        TP.append(stock_list[i][0] + stock_list[i][1] + stock_list[i][2])
        closePrice.append(stock_list[i][2])

    MA_list = ma.MA(closePrice, cycle)
    for i in range(0, len(MA_list)):
        MD_list.append(abs(MA_list[i] - closePrice[i]))

    for i in range(0, len(MD_list)):
        CCI_list.append((TP[i] - MA_list[i]) / (0.015 * MD_list[i]))

    return CCI_list

    return
