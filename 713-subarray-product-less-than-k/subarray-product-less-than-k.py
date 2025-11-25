class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        parameters: arr of ints nums, int k.
        return: number of subarray where product < k.
        constraints: k could be 0.
        '''
        if k == 0:
            return 0
        L = 0
        total = 1
        res = 0
        for R in range(len(nums)):
            total *= nums[R]
            while total >= k:
                total //= nums[L]
                L += 1
                if L > R:
                    break
            res += (R-L+1)
        return res