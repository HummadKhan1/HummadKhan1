from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_dict = Counter(s)
        unique = set(s)
        res = 0
        mid_found = False
        for c in unique:
            if count_dict[c]%2 == 0:
                res += count_dict[c]
            else:
                if not mid_found:
                    res += count_dict[c]
                    mid_found = True
                else:
                    res += count_dict[c]-1
        return res