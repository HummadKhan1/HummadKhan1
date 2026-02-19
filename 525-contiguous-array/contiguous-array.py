class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        Parameters: binary arr nums.
        returns: max length of a contiguous subararray with equal num of 0s and 1s.
        Really asking: prefix sum problem where if prefix exists in dict then it is a vaild subarray.
        '''
        num_dict = {0:-1}
        prefix = 0
        max_length = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1

            if prefix in num_dict:
                max_length = max(max_length, i-num_dict[prefix])
            else:
                num_dict[prefix] = i
        return max_length