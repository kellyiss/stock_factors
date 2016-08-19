import stock_filter

for stock in stock_filter.getListByFilter(stock_filter.getFilter().MACD()):
    print stock

print stock_factors.cci.CCI(test_price,2)

for stock in stock_filter.getListByFilter(stock_filter.getFilter().MACD().rankLT(4),
                                          stock_filter.getFilter().MACD().rankGT(3)):
    print stock
