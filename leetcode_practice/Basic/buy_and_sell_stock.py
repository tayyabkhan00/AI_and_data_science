# optimized approach O(n)
def maxProfit(prices):
    min_price = float('inf')     # 1
    max_profit = 0               # 2

    for price in prices:         # 3
        if price < min_price:    # 4
            min_price = price    # 5

        profit = price - min_price  # 6
        
        if profit > max_profit:     # 7
            max_profit = profit     # 8

    return max_profit              # 9


# brute force approach O(n^2)
stock = [1, 2, 3, 6, 5, 8, 3]

max_profit = 0

for i in range(len(stock)):           # i = buy day
    for j in range(i + 1, len(stock)):  # j = sell day
        profit = stock[j] - stock[i]   # calculate profit
        if profit > max_profit:        # update best profit
            max_profit = profit

print(max_profit)

        