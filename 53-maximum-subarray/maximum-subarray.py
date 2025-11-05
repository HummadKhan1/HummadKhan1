class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        L = 0
        cur_sum = 0
        max_sum = nums[0]
        maxL, maxR = 0,0
        for R in range(len(nums)):
            if cur_sum < 0:
                cur_sum = 0
                L = R
            cur_sum += nums[R]
            if cur_sum > max_sum:
                max_sum = cur_sum
                maxL, maxR = L, R
        print(nums[maxL:maxR+1])
        return max_sum