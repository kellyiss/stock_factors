# coding=utf-8

def STIX(wprice_list):
    """

    :param wprice_list:
    :return:
    """
    temp = []
    ad_list = []

    for pricesPerStock in wprice_list:
        temp.append([(pricesPerStock[i] - pricesPerStock[i - 1]) for i in range(1, len(pricesPerStock))])

    for j in range(0, len(temp[0])):
        pos = 0
        neg = 0
        for k in range(0, len(temp)):
            if temp[k][j] > 0:
                pos = pos + 1
            else:
                neg = neg + 1
        ad_list.append(pos / neg)

    stix = [ad_list[0] * 0.09]
    for i in range(1, len(ad_list)):
        stix.append(ad_list[i] * 0.09 + stix[i - 1] * 0.91)

    return stix
