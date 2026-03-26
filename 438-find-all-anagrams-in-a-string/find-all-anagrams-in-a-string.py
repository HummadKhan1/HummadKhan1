from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_dict = {}
        p_dict = Counter(p)
        L = 0
        res = []
        for R in range(len(s)):
            s_dict[s[R]] = s_dict.get(s[R], 0)+1
            while (R-L+1) > len(p):
                s_dict[s[L]] -= 1
                if s_dict[s[L]] == 0:
                    del s_dict[s[L]]
                L += 1
            if s_dict == p_dict:
                res.append(L)
        return res