class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_dict = {}
        L = 0
        res = 0
        
        for R in range(len(s)):
            s_dict[s[R]] = s_dict.get(s[R], 0) + 1
            while (R-L+1) - max(s_dict.values()) > k:
                s_dict[s[L]] -= 1
                if s_dict[s[L]] == 0:
                    del s_dict[s[L]]
                L += 1
            res = max(res, R-L+1)
        return res