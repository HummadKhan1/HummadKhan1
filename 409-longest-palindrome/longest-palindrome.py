from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        s_dict = Counter(s)
        unique_elements = set(s)
        mid_found = False
        res = 0

        for u in unique_elements:
            if s_dict[u]%2 == 0:
                res += s_dict[u]
            else:
                if not mid_found:
                    res += s_dict[u]
                    mid_found = True
                else:
                    res += s_dict[u]-1
        return res