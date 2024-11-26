#!/usr/bin/python3
"""
This module defines a function `makeChange` that determines the fewest number of coins
needed to meet a given total using coins of different denominations.
"""

def makeChange(coins, total):
    """Determine the fewest number of coins needed to meet total."""
    if total <= 0:
        return 0

    # Initialize a list to store the minimum coins needed for each amount
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # Base case: 0 coins are needed to make 0 total

    # Process each coin denomination
    for coin in coins:
        for amount in range(coin, total + 1):
            if min_coins[amount - coin] != float('inf'):
                min_coins[amount] = min(min_coins[amount], min_coins[amount - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1
