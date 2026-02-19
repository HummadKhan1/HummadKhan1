class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        parameters: arr of int nums.
        return: total number of subarrays with sum of k.
        Really asking: Use dict to keep track of sums in current index. If cur_sum - k is in dict then that is a valid subarray.
        '''
        sum_dict = {0:1}
        cur_sum = 0
        res = 0
        for n in nums:
            cur_sum += n
            prefix = cur_sum - k

            if prefix in sum_dict:
                res += sum_dict.get(prefix)
            
            sum_dict[cur_sum] = sum_dict.get(cur_sum, 0)+1
        return res