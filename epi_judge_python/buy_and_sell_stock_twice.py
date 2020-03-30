from typing import List

from test_framework import generic_test


def buy_and_sell_stock_twice(prices: List[float]) -> float:
    max_total_profit, lowest_price = 0.0, float('inf')
    first_stock_sell_profits = [0.0] * len(prices)

    for idx, price in enumerate(prices):
        if lowest_price > price:
            lowest_price = price
        else:
            max_total_profit = max(max_total_profit, price - lowest_price)
        first_stock_sell_profits[idx] = max_total_profit

    current_max_price = float('-inf')

    for i, price in reversed(list(enumerate(prices[1:], 1))):
        if current_max_price < price:
            current_max_price = price
        else:
            max_total_profit = max(
                    max_total_profit,
                    current_max_price - price + first_stock_sell_profits[i-1])

    return max_total_profit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock_twice.py',
                                       'buy_and_sell_stock_twice.tsv',
                                       buy_and_sell_stock_twice))
