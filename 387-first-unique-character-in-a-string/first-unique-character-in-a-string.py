from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = Counter(s)

        for i in range(len(s)):
            if count_dict[s[i]] == 1:
                return i
        return -1