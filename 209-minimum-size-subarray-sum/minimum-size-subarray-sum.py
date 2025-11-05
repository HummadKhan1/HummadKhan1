class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        cur_sum = 0
        min_len = float("inf")
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