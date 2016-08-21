# coding=utf-8
from __future__ import division
import operator

def QStick(wopen_list, wclose_list, n_day):
    """
    :param n_day: An int indicating how many days the user is interested in
    :return: Q stick
    """
    assert n_day <= len(wclose_list) and n_day <= len(wopen_list)

    # analyses the last n_day days only
    n_open  = wopen_list[-n_day:]
    n_close = wclose_list[-n_day:]

    return sum(map(operator.sub, n_open, n_close)) / n_day
