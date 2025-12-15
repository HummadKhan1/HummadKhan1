class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        parameters: int arr nums.
        return: subarray with largest sum.
        really asking: if cur_sum < 0: cur_sum = 0
        constraints: 
        '''
        max_sum = nums[0]
        cur_sum = 0
        L = 0
        for n in nums:
            cur_sum = max(cur_sum, 0)

            cur_sum += n

            max_sum = max(max_sum, cur_sum)

        return max_sum