from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)

        diff = t_count - s_count

        res = list(diff.keys())

        return res[0]