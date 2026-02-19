class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        '''
        paramters: pos int arr nums, pos int target.
        returns: MIN LEN of subarray whose sum >= target.
        Really asking: Sliding Window.
        Constraints: if no subarray return 0.
        '''
        min_len = float("inf")
        cur_sum = 0
        L = 0

        for R in range(len(nums)):
            cur_sum += nums[R]
            while cur_sum >= target:
                min_len = min(min_len, R-L+1)
                cur_sum -= nums[L]
                L += 1
        if min_len == float("inf"):
            return 0
        return min_len