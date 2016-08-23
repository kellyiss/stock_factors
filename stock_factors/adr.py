# coding=utf-8
import ma


def ADR(wprice_list, cycle):
    """

    需知昨天的adr十日平均值以及今日收盘后算出今日adr十日平均值，才确定明日是否开仓
    :param wprice_list:
    :param circle
    :return:两天的adr十日平均值
    """
    # check inputs
    assert cycle <= len(wprice_list)
    temp = []
    adr_list = []
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
        adr_list.append(pos / neg)

    return ma.MA(adr_list, cycle)
