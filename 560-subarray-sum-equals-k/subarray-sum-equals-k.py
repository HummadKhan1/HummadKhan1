class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSum = {0:1}
        prefix = 0
        res = 0 
        for n in nums:
            prefix += n
            find = prefix-k
            if find in prefixSum:
                res += prefixSum.get(find)
            prefixSum[prefix] = prefixSum.get(prefix, 0)+1
        return res