# coding=utf-8
import ma


def RVI(stock_list, cycle):
    """
    惯性指标
    :param stock_list:[[wHigh,wLow,wOpen,wClose]...]
    :param cycle:
    :return:
    """
    temp = []
    for dayPrice in stock_list:
        temp.append(abs(dayPrice[3] - dayPrice[2]) / (dayPrice[0] - dayPrice[1]))

    return ma.MA(temp, cycle)
