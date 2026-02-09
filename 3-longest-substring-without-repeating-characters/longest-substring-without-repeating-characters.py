class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        parameters: string s.
        return: length of the longest substring.
        Really asking: sliding window
        '''

        dup_set = set()
        max_len = 0
        cur_len = 0
        L = 0
        for R in range(len(s)):
            max_len = max(max_len, cur_len)
            while s[R] in dup_set:
                dup_set.remove(s[L])
                L += 1
                cur_len -= 1
            dup_set.add(s[R])
            cur_len += 1
        max_len = max(max_len, cur_len)
        return max_len