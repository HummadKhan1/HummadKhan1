class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        parameters: string s, int k.
        returns: LENGTH of longest substring.
        Really asking: Sliding Window, while max(dict.values()) <= k.
        Variables: s_dict, L, R, max_len.
        Constraints: k could be 0:
        '''
        s_dict = {}
        L = 0
        max_len = 0

        for R in range(len(s)):
            s_dict[s[R]] = s_dict.get(s[R], 0)+1
            while (R-L+1)-max(s_dict.values()) > k:
                s_dict[s[L]] -= 1
                if s_dict[s[L]] == 0:
                    del s_dict[s[L]]
                L += 1
            max_len = max(max_len, (R-L+1))
        return max_len