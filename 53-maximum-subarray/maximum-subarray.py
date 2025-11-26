class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        parameters: int arr nums.
        return: subarray with largest sum.
        constraints: nums[i] could be negative.
        kadane's algorithm
        '''
        L = 0
        max_sum = float('-inf')
        cur_sum = 0
        for n in nums:
            cur_sum = max(cur_sum, 0)

            cur_sum += n

            max_sum = max(max_sum, cur_sum)
        return max_sum
