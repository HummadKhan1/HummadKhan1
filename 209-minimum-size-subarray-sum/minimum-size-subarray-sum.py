class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        parameters: arr of ints nums, pos int target.
        return: min_len of subarr where sum >= target.
        constraints: 
        really asking: Sliding Window problem. 
        '''
        L = 0
        cur_sum = 0
        min_len = float("inf")

        for R in range(len(nums)):
            cur_sum += nums[R]
            while cur_sum >= target:
                min_len = min(min_len, R-L+1)
                cur_sum -= nums[L]
                L += 1
        if min_len == float("inf"):
            return 0
        return min_len
