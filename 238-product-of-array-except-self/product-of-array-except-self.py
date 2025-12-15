class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        maxLeft = []
        total = 1
        for n in nums:
            maxLeft.append(total)
            total *= n
        
        maxRight = [1]*len(nums)
        total = 1
        for i in range(len(nums)-1,-1,-1):
            maxRight[i] = total
            total *= nums[i]
        
        res = []
        for i in range(len(nums)):
            res.append(maxLeft[i]*maxRight[i])
        return res