# https://leetcode.com/problems/best-time-to-buy-and-sell-stock
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # initialize the maximum selling price to -1 and the profit to 0
        max_sell = -1
        max_p = 0
        # loop in the reverse to get the maximum selling price and consequently max price, 
        # the logic is that the maximum selling price coupled with the lowest buying price is the maximum profit, so we calculate max profit at every step but update selling price only on the maximum
        for i in range(len(prices)-1,-1,-1):
            if max_sell< prices[i]:
                max_sell = prices[i]
            max_p =max(max_p,max_sell-prices[i])
            print(max_p)
        return max_p
