# coding=utf-8
from __future__ import division

def AROON(stock_prices, n_day):
    """
    :param stock_prices: A list of prices, the last one is data of yesterday
    :param n_day: An int indicating how many days the user is interested in
    :return: A tuple of such form (Arron-up, Arron-down)
    """
    assert n_day < len(stock_prices)

    # analyses the last (n_day+1) days only (in reverse order)
    n_prices = stock_prices[: -1 - (n_day + 1) : -1]

    maximum_index = n_prices.index(max(n_prices))
    minimum_index = n_prices.index(min(n_prices))

    return (100 - 100 * maximum_index / n_day,
            100 - 100 * minimum_index / n_day)
