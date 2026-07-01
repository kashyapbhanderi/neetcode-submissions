class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        
        for price in prices:
            # If we find a new historical low, update it
            if price < min_price:
                min_price = price
            # Otherwise, check if selling today beats our best profit
            else:
                profit = price - min_price
                if profit > max_profit:
                    max_profit = profit
                    
        return max_profit
        