class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        parameters: array of ints nums, int k.
        Return: number of subarrays whose sum is k
        constraints: 
        '''
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

        
        