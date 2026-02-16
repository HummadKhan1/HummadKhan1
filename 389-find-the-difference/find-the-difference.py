from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)

        diff = t_dict - s_dict


        return ''.join(list(diff.keys()))