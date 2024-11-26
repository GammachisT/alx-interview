#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0
    
    # Initialize dp array with infinity
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make amount 0

    # Compute the minimum coins required for each amount up to total
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # If dp[total] is still infinity, we cannot make the total
    return dp[total] if dp[total] != float('inf') else -1