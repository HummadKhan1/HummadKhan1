class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        parameters: int arr nums.
        return: product
        Really asking: total, globMin, globMax
        constraints:
        edge cases: 
        '''
        res = max(nums)
        curMax = 1
        curMin = 1
        for n in nums:
            tmp = curMax * n
            curMax = max(n, curMax*n, curMin*n)
            curMin = min(n, curMin*n, tmp)
            res = max(curMax, res)
        return res
