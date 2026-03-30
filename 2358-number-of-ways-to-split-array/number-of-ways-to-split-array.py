class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        maxLeft = []
        total = 0
        for n in nums:
            total += n
            maxLeft.append(total)

        maxRight = [0]* len(nums)
        total = 0
        for i in range(len(nums)-1,-1,-1):
            maxRight[i] = total
            total += nums[i]
        
        res = 0
        for i in range(len(nums)):
            if i == len(nums)-1:
                continue
            if maxRight[i] <= maxLeft[i]:
                res += 1
        return res