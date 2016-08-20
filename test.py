import stock_filter

for stock in stock_filter.getListByFilter(stock_filter.getFilter().MACD()):
    print stock

print '--------'

for stock in stock_filter.getListByFilter(stock_filter.getFilter().MACD().rankLT(4),
                                          stock_filter.getFilter().MACD().rankGT(3)):
    print stock
