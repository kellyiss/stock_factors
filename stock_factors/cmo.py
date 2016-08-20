# coding=utf-8
from __future__ import division

def CMO(wclose_list, n_day):
    """
    :param wclose_list: A list of close prices
    :param n_day: An int indicating how many days the user is interested in
    :return: CMO index
    """
    assert n_day <= len(wclose_list)

    # analyses the last n_day days only
    n_prices = wclose_list[-n_day:]

    diff_list = [a - b for (a, b) in zip(n_prices[1:], n_prices[:-1])]
    (su, sd) = reduce(lambda s,x:
            (s[0] + x, s[1]) if x > 0 else (s[0], s[1] - x), diff_list, (0, 0))

    return 100 * (su - sd) / (su + sd)
