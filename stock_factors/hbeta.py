# coding=utf-8
import numpy


def HBETA(stock_prices, index_prices):
    """
    :param stock_prices: 格式化之后股票价格
    :param index_prices: 股指 时间间隔与股票价格相同
    :return: beta
    """
    # check inputs
    assert len(stock_prices) == len(index_prices)

    sp_returns = [(numpy.log(stock_prices[i + 1]) - numpy.log(stock_prices[i])) for i in
                  range(0, len(stock_prices) - 1)]
    ip_returns = [(numpy.log(index_prices[i + 1]) - numpy.log(index_prices[i])) for i in
                  range(0, len(index_prices) - 1)]

    covar = numpy.cov(sp_returns, ip_returns)
    beta = covar[0][1] / covar[0][0]

    return beta
