# coding=utf-8
__author__ = 'Arthur'


def max_profit(prices):
    # buy = True
    # total = 0
    # buy_price = 0
    # i = 0
    # while i < len(prices):
    #     if buy:
    #         while i < len(prices) - 1 and prices[i + 1] <= prices[i]:
    #             i += 1
    #         buy_price = prices[i]
    #         print('buy at: ', i, '  prices: ', buy_price)
    #         buy = False
    #         i += 1
    #     else:
    #         while i < len(prices) - 1 and prices[i + 1] >= prices[i]:
    #             i += 1
    #         total += (prices[i] - buy_price)
    #         print('sell at: ', i, '  prices: ', prices[i])
    #         buy = True
    #         i += 1
    # return total
    i = 0
    sum = 0
    while i < len(prices) - 1:
        if prices[i + 1] > prices[i]:
            sum += (prices[i + 1] - prices[i])
        i += 1
    return sum


prices = [1, 2, 1, 4]
stock = max_profit(prices)
print(stock)