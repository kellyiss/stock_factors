# coding=utf-8
import numpy as np


def ADVR(wprice_list, wvolumn_list):
    """
    :param wprice_list: n+1天
    :param wvolumn_list: n天
    :return:
    """
    temp = []

    for pricesPerStock in wprice_list:
        temp.append([(pricesPerStock[i] - pricesPerStock[i - 1]) for i in range(1, len(pricesPerStock))])

    for i in range(0, len(temp[0])):
        for j in range(0, len(temp)):
            if temp[j][i] > 0:
                temp[j][i] = 1
            else:
                temp[j][i] = 0

    up = np.array(temp, dtype=float)
    volumn = np.array(wvolumn_list)
    upVolumn = up * volumn
    upList = []
    for i in range(0, len(upVolumn.tolist()[0])):
        sum1 = 0
        for j in range(0, len(upVolumn.tolist())):
            sum1 = sum1 + upVolumn[j][i]
        upList.append(sum1)

    down = np.ones_like(up, dtype=float) - up
    downVolumn = down * volumn
    downList = []
    for i in range(0, len(downVolumn.tolist()[0])):
        sum2 = 0
        for j in range(0, len(downVolumn.tolist())):
            sum2 = sum2 + downVolumn[j][i]
        downList.append(sum2)

    result = [upList[k] / downList[k] for k in range(0, len(upList))]
    return result
