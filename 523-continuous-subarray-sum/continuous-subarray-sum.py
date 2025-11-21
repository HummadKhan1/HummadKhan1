class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        parameters: int arr nums, int k.
        Return: boolean
        note: 
        prefix sums
        '''
        prefixSum = {0:-1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            prefix = prefix % k

            if prefix == 0:
                if i >= 2:
                    return True  
                
            
            if prefix in prefixSum:
                if i-prefixSum[prefix]>= 2:
                    return True
                
            
            if prefix not in prefixSum:
                prefixSum[prefix] = i
        return False