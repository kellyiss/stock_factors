#coding=utf-8
import numpy as np

def list_sum(list):
    sum=0.00
    for i in range(0,len(list)):
        sum=sum+list[i]
    return sum

def TRIN(wprice_list,wvolumn_list):
    """
    :param wprice_list:
    :return:
    """
    temp = []
    pos_list=[]
    neg_list=[]
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
        pos_list.append(pos)
        neg_list.append(neg)

    for i in range(0,len(temp[0])):
        for j in range(0,len(temp)):
            if temp[j][i]>0:
                temp[j][i]=1
            else:
                temp[j][i]=0

    up=np.array(temp,dtype=float)
    volumn=np.array(wvolumn_list)
    upVolumn=up*volumn
    upList=[]
    for i in range(0,len(upVolumn.tolist()[0])):
        sum1=0
        for j in range(0,len(upVolumn.tolist())):
            sum1=sum1+upVolumn[j][i]
        upList.append(sum1)

    down=np.ones_like(up,dtype=float)-up
    downVolumn=down*volumn
    downList = []
    for i in range(0,len(downVolumn.tolist()[0])):
        sum2=0
        for j in range(0,len(downVolumn.tolist())):
            sum2=sum2+downVolumn[j][i]
        downList.append(sum2)

    molecule=list_sum(pos_list)/list_sum(neg_list)
    denominator=list_sum(upList)/list_sum(downList)

    return molecule/denominator

