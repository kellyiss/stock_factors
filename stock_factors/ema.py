# coding=utf-8
import numpy


def EMA(stock_prices, cycle):
    """
    :param stock_prices:
    :param cycle:
    :return:
    """
    # check inputs
    assert cycle <= len(stock_prices)

    ema = []

    sum = numpy.sum(range(1, cycle + 1))

    for i in range(cycle, len(stock_prices) + 1):
        ema_index = 0.0
        for j in range(i - cycle, i):
            ema_index += float(cycle + 1 - i + j) / float(sum) * float(stock_prices[j])
        ema.append(ema_index)

    return ema


def EMA_from_zero(stock_prices, cycle):
    """
    :param stock_prices:
    :param cycle:
    :return:
    """
    # check inputs
    assert cycle > 1

    res = [stock_prices[0]]

    for i in range(1, len(stock_prices)):
        res.append(res[i - 1] * float(cycle - 1) / float(cycle + 1) + stock_prices[i] * 2.0 / float(cycle + 1))

    return res