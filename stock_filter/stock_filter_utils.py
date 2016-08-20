# encoding=utf-8
import stock_filter
import stock_filter_db


def getFilter():
    return stock_filter.StockFilter(stock_filter_db.getAllStockPrices(), stock_filter_db.getCompositePrices())


def getListByFilter(*filter):
    if len(filter) == 1:
        return filter[0].stock_list
    elif len(filter) > 1:
        res = filter[0].stock_list

        for i in range(1, len(filter)):
            res = [j for j in res if j.id in [k.id for k in filter[i].stock_list]]

        return res
    else:
        return []
