# coding=utf-8
import numpy


def EMA(stock_prices, cycle):
    """
    :param stock_prices:
    :param cycle:
    :return:
    """
    # check inputs
    assert cycle > 1

    ema = [stock_prices[0]]

    for i in range(1, len(stock_prices)):
        ema.append(ema[i - 1] * float(cycle - 1) / float(cycle + 1) + stock_prices[i] * 2.0 / float(cycle + 1))

    return ema
