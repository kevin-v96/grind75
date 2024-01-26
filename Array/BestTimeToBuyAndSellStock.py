#solution for https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #keep track of the minimum price
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:]:
            #profit is the maximum of the last maximum profit or the profit according to the current price
            max_profit = max(max_profit, price - min_price)
            #keep changing the minimum price based on what we encounter
            min_price = min(min_price, price)

        return max_profit