class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        parameters: binary arr nums.
        return: max len of subarray with an equal number of 0 and 1s.
        Actually means: 
        edge cases: 
        '''
        prefixSum = {0:-1}
        prefix = 0
        max_len = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                prefix += 1
            else:
                prefix -= 1
            if prefix in prefixSum:
                max_len = max(max_len, i-prefixSum[prefix])
            else:
                prefixSum[prefix] = i
        return max_len
            
            
