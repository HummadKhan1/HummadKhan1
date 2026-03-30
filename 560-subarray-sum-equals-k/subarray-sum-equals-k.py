class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        parameters: array of ints, int k.
        return: NUMBER OF subarrays whose sum equals to k.
        Really asking: Prefix sum. 
        '''

        nums_dict = {0:1}
        cur_sum = 0
        res = 0
        
        for n in nums:
            cur_sum += n
            prefix = cur_sum - k

            if prefix in nums_dict:
                res += nums_dict[prefix]
            
            nums_dict[cur_sum] = nums_dict.get(cur_sum, 0) + 1
        
        return res