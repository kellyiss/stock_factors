# coding=utf-8
import numpy


def MA(stock_prices, cycle):
    """
    :param stock_prices:
    :param cycle:
    :return: MA
    """
    # check inputs
    assert cycle <= len(stock_prices)

    ma = []
    for i in range(cycle, len(stock_prices) + 1):
        ma.append(numpy.mean(stock_prices[i - cycle:i]))

    return ma
