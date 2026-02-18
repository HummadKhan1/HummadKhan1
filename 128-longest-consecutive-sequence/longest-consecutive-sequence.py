class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        L = 0
        max_len = 0
        for n in unique:
            if n-1 in unique:
                continue
            cur_len = 0
            cur_n = n
            while cur_n in unique:
                cur_len += 1
                cur_n += 1
            max_len = max(max_len, cur_len)
        return max_len
            
