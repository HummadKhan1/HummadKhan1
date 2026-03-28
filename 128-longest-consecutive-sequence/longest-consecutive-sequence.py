from collections import Counter
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        for n in nums_set:
            if n-1 in nums_set:
                continue
            cur_num = n
            cur_len = 0
            while cur_num in nums_set:
                cur_len += 1
                cur_num += 1
            max_len = max(max_len, cur_len)
        return max_len