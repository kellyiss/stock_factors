# coding=utf-8
import numpy as np


def ASI(stock_list, cycle):
    """
    eg:用户传进参数为n天，即计算出2n-1天的si，得到n天的asi，
       利用其中的n-1天做平滑化，根据第n天的数据判断是否突破
    :param stock_list: [wOpen,wHigh,wLow,wClose](矩阵)
    :return:asi
    """
    assert cycle < len(stock_list)
    l = 3
    si = []
    asi = []
    for i in range(1, len(stock_list)):
        a = abs(stock_list[i][1] - stock_list[i - 1][3])
        b = abs(stock_list[i][2] - stock_list[i - 1][3])
        c = abs(stock_list[i][1] - stock_list[i - 1][2])
        d = abs(stock_list[i - 1][3] - stock_list[i - 1][0])

        e = stock_list[i][3] - stock_list[i - 1][3]
        f = stock_list[i][3] - stock_list[i][0]
        g = stock_list[i - 1][3] - stock_list[i - 1][0]

        x = e + 1 / (2 * float(f)) + g
        k = max(a, b)
        if (max(a, b, c) == a):
            r = a + 1 / (2 * b) + 1 / (4 * d)
        elif (max(a, b, c) == b):
            r = b + 1 / (2 * a) + 1 / (4 * d)
        else:
            r = c + a / (4 * d)

        si.append(50 * x / r * k / l)

    for i in range(cycle, len(si) + 1):
        asi.append(np.sum(si[i - cycle:i]))

    return asi
