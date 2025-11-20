class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixSum = {}
        prefix = 0
        max_len = 0
        for i in range(len(nums)):
            if nums[i] < 1:
                prefix -= 1
            else:
                prefix += 1

            if prefix == 0:
                max_len = max(max_len, i+1)

            if prefix in prefixSum:
                max_len = max(max_len, i-prefixSum[prefix])
            
            if prefix not in prefixSum:
                prefixSum[prefix] = i
        return max_len