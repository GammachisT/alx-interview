#!/usr/bin/python3
"""Making Change Problem"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given amount total."""
    if total <= 0:
        return 0

    current_total = 0
    used_coins = 0
    coins.sort(reverse=True)

    for coin in coins:
        num_coins = (total - current_total) // coin
        current_total += num_coins * coin
        used_coins += num_coins

        if current_total == total:
            return used_coins

    return -1