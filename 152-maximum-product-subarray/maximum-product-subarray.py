class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        parameters: int arr nums.
        return: largest product.
        constraints: could be 0.
        '''
        curMax, curMin= 1, 1
        res = max(nums)
        for n in nums:
            temp = curMax
            curMax = max(curMax*n, curMin*n, n)
            curMin = min(temp*n, curMin*n, n)
            res = max(res, curMax)
        return res