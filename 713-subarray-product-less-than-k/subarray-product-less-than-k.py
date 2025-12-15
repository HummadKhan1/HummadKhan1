class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        parameters: int arr nums, int k.
        return: NUMBER OF subarray.
        Really asking: Sliding WIndow, res += R-L+1
        constraints:
        '''
        if k == 0:
            return 0
        L = 0
        res = 0
        curProd = 1
        for R in range(len(nums)):
            curProd *= nums[R]
            
            while curProd >= k and L <= R:
                curProd //= nums[L]
                L += 1

            if curProd < k:
                res += R-L+1

        return res
