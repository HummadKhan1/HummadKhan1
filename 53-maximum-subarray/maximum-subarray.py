class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        parametersL int arr nums.
        return : sum of the largest subarray.
        constraints: elements could be negative.
        edge cases:
        1. Initialize L, R = 0, 0, curSum, max_sum
        2. while R < len(nums)
        3.  if curSum < 0:
        4.      curSum = 0
        5.      L = R
        6.  end loop
        7. curSum += nums[R]
        8. maxSum = max(curSum, maxSum)
        '''
        curSum = 0
        maxSum = nums[0]
        for n in nums:
            curSum = max(curSum, 0)

            curSum += n

            maxSum = max(maxSum, curSum)
        return maxSum