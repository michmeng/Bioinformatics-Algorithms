import math

def change(money, coins):
    min_coins = [0] + [math.inf]*money
    for i in range(1, money + 1):
        for j in coins:
            if i >= j:
                num_coins = min_coins[i-j]+1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins
    return min_coins[money]

# print (change())
