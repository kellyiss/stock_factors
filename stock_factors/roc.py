# coding=utf-8
from __future__ import division

def ROC(stock_prices, n_day):
    """
    :param stock_prices: A list of prices
    :param n_day: An int. Compare today's price with n_day days ago
    :return: ROC
    """
    assert n_day < len(stock_prices)
    return stock_prices[-1] - stock_prices[-1 - n]
