from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = Counter(s1)
        s2_dict = {}
        L = 0

        for R in range(len(s2)):
            s2_dict[s2[R]] = s2_dict.get(s2[R], 0)+1
            while (R-L+1) > len(s1):
                s2_dict[s2[L]] -= 1
                if s2_dict[s2[L]] == 0:
                    del s2_dict[s2[L]]
                L += 1
            if s2_dict == s1_dict:
                return True
        return False