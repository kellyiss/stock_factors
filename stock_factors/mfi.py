# coding=utf-8

def MFI(stock_list):
    """
    :param stock_list: (一条时间线的stocklist)[[wHigh],[wLow],[wVolumn]...]
    :return:
    """
    MFI_list = []
    for i in range(0, len(stock_list)):
        MFI_list.append((stock_list[i][0] - stock_list[i][1]) / stock_list[i][2])

    return MFI_list
