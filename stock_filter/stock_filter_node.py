# encoding=utf-8

class StockNode:
    def __init__(self, stock_id, stock_name, stock_prices, stock_value):
        self.id = stock_id
        self.name = stock_name
        self.value = stock_value
        self.prices = stock_prices

    def __str__(self):
        return "id={id}, name={name}, value={value}, prices={prices}".format(id=self.id, name=self.name.encode('utf-8'),
                                                                             value=self.value, prices=self.prices)
