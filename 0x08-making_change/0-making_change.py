#!/usr/bin/python3
"""
Module to calculate the fewest number of coins needed to meet a total
"""

def makeChange(coins, total):
    """
    Calculate the fewest number of coins needed to meet total.

    Args:
        coins (list): A list of the values of the coins.
        total (int): The total amount to be met with coins.

    Returns:
        int: The fewest number of coins needed to meet total,
             -1 if total cannot be met by any number of coins,
             0 if total is 0 or less.
    """
    if total <= 0:
        return 0

    # Initialize a list to hold the minimum coins needed for each amount
    min_coins = 0
    temp = 0  # No coins needed to make 0

    coins.sort(reverse=True)
    # Iterate through each coin

    for coin in coins:
        while check < total:
            min_coins += coin
            temp += 1
            # Update the minimum coins needed for this amount
            if min_coins == total:
                return temp
            min_coins -= coin
            min_coins -= 1

    # If we can't make the total, return -1
    return -1