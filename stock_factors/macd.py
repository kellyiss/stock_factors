# coding=utf-8
import numpy
import ema


def MACD(stock_prices, short_time=12, long_time=26, dea_time=9):
    """
    :param stock_prices:
    :param short_time:
    :param long_time:
    :param dea_time:
    :return:
    """
    # check inputs
    assert short_time < long_time

    EMA12 = ema.EMA(stock_prices, short_time)
    EMA26 = ema.EMA(stock_prices, long_time)

    DIF = []
    for i in range(0, len(EMA12)):
        DIF.append(EMA12[i] - EMA26[i])

    DEA = ema.EMA(DIF, dea_time)

    macd = []
    for i in range(0, len(EMA12)):
        macd.append(2.0 * (DIF[i] - DEA[i]))

    return macd
