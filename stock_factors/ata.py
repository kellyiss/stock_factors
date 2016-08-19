#coding=utf-8
import ma

def ATA(stock_list,cycle):
    """
    平均真实区域
    :param stock_list: [wHigh,wLow,wClose]
    :param cycle:
    :return:注意传入的数据是cycle+1天，算出ata是cycle天，因此返回的是“今天”的十日平均值
    """

    assert cycle<len(stock_list)
    ata_list=[]

    for i in range(1,len(stock_list)):
        d1=abs(stock_list[i][0]-stock_list[i][1])
        d2=abs(stock_list[i-1][1]-stock_list[i][0])
        d3=abs(stock_list[i-1][2]-stock_list[i][2])
        ata=max(d1,d2,d3)
        ata_list.append(ata)

    ma_cycle=ma.MA(ata_list,cycle)[0]

    return ma_cycle

