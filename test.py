import stock_factors

test_sp = [6.5313,6.5625,6.4688,6.4375,6.2188,6.2500,6.1250]
test_ip = [10500,6492,6540,8924,5416,4588,16236]
test_h = range(1, 36)
test_price = [[1,2,3],[7,3,1],[4,3,2],[5,6,7]]
test_volumn = [[1,1],[2,2],[2,2],[1,1]]
test_stock = [[1,2,3,4],[4,6,8,9],[7,3,5,6],[6,3,7,3]]

print stock_factors.mi.MI(test_price,2)

