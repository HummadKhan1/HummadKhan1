class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixSums = {0:-1}
        prefix = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                prefix += 1
            else:
                prefix -= 1
            
            if prefix in prefixSums:
                res = max(res, i-prefixSums[prefix])
            else:
                prefixSums[prefix] = i
        return res