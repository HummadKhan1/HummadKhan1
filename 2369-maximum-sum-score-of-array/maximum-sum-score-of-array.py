class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        '''
        parameters: int arr nums.
        return: max sum score.
        Really asking: max_sum = max(max_sum, max(maxLeft, maxRight))
        constraints: 
        '''
        maxLeft = []
        total = 0
        for n in nums:
            total += n
            maxLeft.append(total)
        
        maxRight=[0]*len(nums)
        total = 0
        for i in range(len(nums)-1,-1,-1):
            total += nums[i]
            maxRight[i] = total
        
        max_sum = nums[0]
        for i in range(len(nums)):
            max_sum = max(max_sum, max(maxLeft[i], maxRight[i]))
        return max_sum