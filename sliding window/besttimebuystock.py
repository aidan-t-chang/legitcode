# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and 
# choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

def besttime(prices):
    l, r = 0, 1
    max1 = 0
    while r < len(prices):
        if prices[l] <= prices[r]:
            max1 = max(max1, (prices[r] - prices[l])) 
        else:
            l = r
        r += 1     
    return max1