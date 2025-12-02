class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        parameters: arr of ints, int k.
        return: number of subarrays where prod of elements < k.
        Really asking: sliding window. res += (R-L+1)*2
        constraints: Elements are positive
        '''
        L = 0
        res = 0
        cur_sum = 1
        for R in range(len(nums)):
            cur_sum *= nums[R]
            while cur_sum >= k:
                cur_sum //= nums[L]
                L += 1
                if L > R:
                    break
            res += R-L+1
        return res