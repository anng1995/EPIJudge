from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    max_profit, lowest_price = 0.0, float('inf')

    for price in prices:
        if price < lowest_price:
            lowest_price = price
        max_profit = max(max_profit, price - lowest_price)

    return max_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
