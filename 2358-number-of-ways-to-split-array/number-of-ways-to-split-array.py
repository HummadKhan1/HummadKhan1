class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        '''
        parameters: int arr nums.
        returns: number of valid splits. Valid split is where maxLeft[i] >= maxRight[i]
        constraints: At least one element to the right of i.
        '''
        maxLeft = []
        total = 0
        for n in nums:
            total += n
            maxLeft.append(total)
        
        maxRight = [0]*len(nums)
        total = 0
        for i in range(len(nums)-1,-1,-1):
            maxRight[i] = total
            total += nums[i]
        
        res = 0
        for i in range(len(nums)-1):
            if maxLeft[i] >= maxRight[i]:
                res += 1
        return res