class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        parameters: int arr nums, pos int k.
        return: boolean true or false
        constraints: 
        Really asking: (nums[i]-nums[j]) % k == 0
                       (nums[i] % k) - (nums[j] % k) == 0
                       nums[i] % k == nums[j] % k
        If we can find a 
        '''
        prefixSum = {0:-1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefix  = prefix % k
            
            if prefix in prefixSum:
                if i-prefixSum[prefix] >= 2:
                    return True
            else:
                prefixSum[prefix] = i
        return False