# encoding=utf-8
from stock_factors import *


class StockFilter:
    def __init__(self, all_stocks, cmp):
        self.stock_list = all_stocks
        self.composite = cmp
        pass

    def HBETA(self):
        for stock in self.stock_list:
            stock.value = hbeta.HBETA(stock.prices, self.composite.prices)

        self.__sort()

        return self

    def RSI(self):
        for stock in self.stock_list:
            stock.value = rsi.RSI(stock.prices)[-1]

        self.__sort()

        return self

    def MACD(self):
        for stock in self.stock_list:
            stock.value = macd.MACD(stock.prices)[-1]

        self.__sort()

        return self

    def MA(self, cycle):
        for stock in self.stock_list:
            stock.value = ma.MA(stock.prices, cycle)[-1]

        self.__sort()

        return self

    def MTM(self, cycle):
        for stock in self.stock_list:
            stock.value = mtm.MTM(stock.prices, cycle)[-1]

        self.__sort()

        return self

    def valueLT(self, value):
        i = len(self.stock_list) - 1

        while i > -1:
            if self.stock_list[i].value <= value:
                break
            i -= 1

        self.stock_list = self.stock_list[0: i + 1]
        return self

    def valueGT(self, value):
        i = 0
        while i < len(self.stock_list):
            if self.stock_list[i].value >= value:
                break
            i += 1

        self.stock_list = self.stock_list[i:]
        return self

    def percentLT(self, value):
        if value >= 0 and value <= 100:
            rank = int(float(len(self.stock_list)) / 100 * value)
            return self.rankLT(rank)
        return self

    def percentGT(self, value):
        if value >= 0 and value <= 100:
            rank = int(float(len(self.stock_list)) / 100 * value)
            return self.rankGT(rank + 1)
        return self

    def rankLT(self, value):
        if value < len(self.stock_list) and value > 0:
            self.stock_list = self.stock_list[0:value]
        return self

    def rankGT(self, value):
        if value > 0:
            self.stock_list = self.stock_list[value - 1:]
        return self

    def __sort(self):
        self.stock_list.sort(key=lambda stock: stock.value)
