# coding=utf-8

def PVI(wprice_list, wvolumn_list):
    rate = [(1 - wprice_list[i - 1] / wprice_list[i]) for i in range(1, len(wprice_list))]
    volumn = [wvolumn_list[i] - wvolumn_list[i - 1] for i in range(1, len(wvolumn_list))]
    pvi = [1000.0000]
    for i in range(1, len(wprice_list)):
        if (volumn[i - 1] < 0):
            pvi.append(pvi[i - 1])
        else:
            pvi.append(pvi[i - 1] + rate[i - 1] * pvi[i - 1])

    return pvi
