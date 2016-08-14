# coding=utf-8
import numpy

def MTM(stock_prices, cycle):
    mtm = []
    for i in range(cycle - 1, len(stock_prices)):
        mtm.append(stock_prices[i] - stock_prices[i - cycle + 1])
    return mtm