class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        parameters: string s.
        returns: LENGTH of longest substring.
        Really asking: Sliding window with set(). 
        Variables: dup_set, L, R, max_len, (R-L+1)
        Constraints: len(s) could be 0.
        '''
        dup_set = set()
        L = 0
        max_len = 0
        
        for R in range(len(s)):
            while s[R] in dup_set:
                dup_set.remove(s[L])
                L+=1
            dup_set.add(s[R])
            max_len = max(max_len, R-L+1)
        return max_len