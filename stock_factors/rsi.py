# coding=utf-8
import numpy


def RSI(stock_prices, cycle):
    """
    :param stock_prices:
    :param cycle:
    :return: RSI
    """
    rising_prices = [(stock_prices[i + 1] - stock_prices[i]) if (stock_prices[i + 1] - stock_prices[i]) > 0 else 0
                     for i in range(0, len(stock_prices) - 1)]
    falling_prices = [-(stock_prices[i + 1] - stock_prices[i]) if (stock_prices[i + 1] - stock_prices[i]) < 0 else 0
                      for i in range(0, len(stock_prices) - 1)]

    rising_mean = []
    falling_mean = []

    rising_mean.append(numpy.mean(rising_prices[0: cycle]))
    falling_mean.append(numpy.mean(falling_prices[0: cycle]))

    for i in range(cycle, len(stock_prices)):
        rising_mean.append(
            (1 / float(cycle) * rising_prices[i - 1]) + ((1 - 1 / float(cycle)) * rising_mean[i - cycle]))
        falling_mean.append(
            (1 / float(cycle) * falling_prices[i - 1]) + ((1 - 1 / float(cycle)) * falling_mean[i - cycle]))

    rsi = []

    for i in range(0, len(rising_mean)):
        rsi.append(100 - 100 / (rising_mean[i] / falling_mean[i] + 1))

    return rsi
