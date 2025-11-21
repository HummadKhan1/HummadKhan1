class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        parameters: int arr prices.
        return: maximum profit if no profit then return 0.
        Actually looking for: find the biggest diff of two points where the first i is a smaller value than the second i
        
        1. Initialize min_price, max_price.
        2. 
        '''
        max_diff = 0
        cur_min = float("inf")
        for i in range(len(prices)):
            if prices[i] < cur_min:
                cur_min = prices[i]
                continue
            if prices[i]-cur_min > max_diff:
                max_diff = prices[i]-cur_min
        return max_diff

        