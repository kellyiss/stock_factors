import stock_factors

test_sp = [1, 2, 8, 7, 3, 6, 10, 12, 6, 8]
test_ip = [5, 6, 7]
test_h = range(1, 36)

print stock_factors.macd.MACD(test_h)
