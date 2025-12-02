class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        parameters:int arr nums, int k.
        return: total number of subarrays where the sum == k.
        Really asking: 
        constraints: elements can be negative.
        '''
        prefix_sums = {0:1}
        prefix = 0
        res = 0
        for n in nums:
            prefix += n
            diff = prefix - k
            if diff in prefix_sums:
                res += prefix_sums[diff]
            prefix_sums[prefix] = prefix_sums.get(prefix, 0)+1
            
        return res
