class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        parameters: array of ints nums, int k.
        return: NUMBER OF contiguous subarrays where product < k.
        Really asking: Sliding Window 
        '''
        if k == 0:
            return 0
        L = 0
        cur_prod = 1
        res = 0

        for R in range(len(nums)):
            cur_prod *= nums[R]
            while cur_prod >= k and L <= R:
                cur_prod //= nums[L]
                L += 1
            res += (R-L+1)

        return res