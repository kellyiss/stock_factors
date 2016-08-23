# -*- coding: utf-8 -*-

import numpy as np
import talib


def ADL(stock_list, cycle):
    """
    累积/派发线指标
    :param stock_list: 股票数据([[high, low, close, volume]])
    :param cycle: 周期(1到30)
    :return:
    """

    assert len(stock_list) >= cycle

    tmp = np.array(stock_list, dtype=float)
    high_list = []
    low_list = []
    close_list = []
    volume_list = []

    for item in tmp:
        high_list.append(item[0])
        low_list.append(item[1])
        close_list.append(item[2])
        volume_list.append(item[3])

    high = np.array(high_list, dtype=float)
    low = np.array(low_list, dtype=float)
    close = np.array(close_list, dtype=float)
    volume = np.array(volume_list, dtype=float)

    result = list(talib.AD(high=high, low=low, close=close, volume=volume))
    return result




