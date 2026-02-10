class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        parameters: unsorted arr of ints nums.
        return: length of longest sequence.
        Really asking: set.
        '''
        nums_set = set(nums)
        max_seq = 0
        for n in nums_set:
            if n - 1 not in nums_set:
                cur_seq = 1
                cur_num = n
            
                while cur_num+1 in nums_set:
                    cur_num += 1
                    cur_seq += 1
                max_seq = max(max_seq, cur_seq)
        return max_seq