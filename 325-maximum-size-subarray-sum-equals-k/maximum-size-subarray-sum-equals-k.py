class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum = {}
        prefix = 0
        max_len = 0
        for i in range(len(nums)):
            prefix += nums[i]
            find = prefix - k

            if prefix == k:
                max_len = max(max_len, i+1)

            if find in prefixSum:
                max_len = max(max_len, i-prefixSum[find])

            if prefix not in prefixSum:
                prefixSum[prefix] = i
        return max_len
