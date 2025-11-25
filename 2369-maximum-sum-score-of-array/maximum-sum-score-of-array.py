class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        '''
        parameters: int arr nums.
        return: max sum of a subarray.
        constraints:
        '''
        maxLeft = []
        total = 0
        for n in nums:
            total += n
            maxLeft.append(total)
        
        maxRight = [0]*len(nums)
        total = 0
        for i in range(len(nums)-1,-1,-1):
            total += nums[i]
            maxRight[i] = total
        max_sum = nums[0]
        for i in range(len(nums)):
            cur_sum = max(maxLeft[i], maxRight[i])
            max_sum = max(max_sum, cur_sum)
        return max_sum