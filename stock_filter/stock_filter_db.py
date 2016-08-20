# encoding=utf-8
import MySQLdb
import json
import stock_filter_node

config_file_path = 'stock_config.json'

db_host = 'localhost'
db_port = 3306
db_user = 'root'
db_pwd = '123456'
db_name = 'stockbots'


def getAllStockPrices():
    stock_id_list = getJSONValue("stocks")

    db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_pwd, port=3306, db=db_name, charset='utf8')
    cursor = db.cursor()

    stock_list = []

    for stock_id in stock_id_list:
        sql = 'select wName,wClose from stock where wSymbol="{}" order by wTime'.format(stock_id)
        cursor.execute(sql)

        res = cursor.fetchall()
        stock_prices = []

        for row in res:
            stock_prices.append(row[1])

        stock_list.append(stock_filter_node.StockNode(stock_id, res[0][0], stock_prices, 0))

    db.close()

    return stock_list


def getCompositePrices():
    composite_id = getJSONValue("composite")

    db = MySQLdb.connect(host=db_host, user=db_user, passwd=db_pwd, port=3306, db=db_name, charset='utf8')
    cursor = db.cursor()

    sql = 'select wName,wClose from stock where wSymbol="{}" order by wTime'.format(composite_id)
    cursor.execute(sql)

    res = cursor.fetchall()
    stock_prices = []

    for row in res:
        stock_prices.append(row[1])

    return stock_filter_node.StockNode(composite_id, res[0][0], stock_prices, 0)


def getJSONValue(key):
    config_file = open(config_file_path)

    json_object = json.loads(config_file.read())

    config_file.close()

    return json_object[key]
