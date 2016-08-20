# encoding=utf-8
import stock_filter
import stock_filter_db


def getFilter():
    return stock_filter.StockFilter(stock_filter_db.getAllStockPrices(), stock_filter_db.getCompositePrices())
