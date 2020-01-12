
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = 0
        sums = 0 
        min_num = float("inf")
        for i in range(len(prices)):
            stack+=1
            if prices[i] > min_num:
                sums += (prices[i]-min_num)
                stack = 0
                min_num = float("inf")
            if min_num>prices[i]:
                min_num = prices[i]

            print(prices[i], min_num, sums)
        return sums
            
                
            
