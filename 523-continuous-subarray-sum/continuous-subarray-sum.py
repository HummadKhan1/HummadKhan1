class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = {0:-1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if k != 0:
                prefix  = prefix % k 
            
                
            if prefix in prefixSum:
                if i-prefixSum[prefix] >= 2:
                    return True
            
            if prefix not in prefixSum:
                prefixSum[prefix] = i
        return False