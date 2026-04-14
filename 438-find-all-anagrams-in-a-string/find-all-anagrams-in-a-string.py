from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        parameters: string s, string p.
        returns: array.
        Really asking: get len(dict) == len(p). add s[R]+=1 and s[L]-=1
        Variables: s_dict, L, R, res.
        Constraints: 
        '''
        s_dict = {}
        p_dict = Counter(p)
        L = 0
        res = []

        for R in range(len(s)):
            s_dict[s[R]] = s_dict.get(s[R], 0)+1
            while R-L+1 > len(p):
                s_dict[s[L]] -= 1
                if s_dict[s[L]] == 0:
                    del s_dict[s[L]]
                L += 1
            if s_dict == p_dict:
                res.append(L)
        return res