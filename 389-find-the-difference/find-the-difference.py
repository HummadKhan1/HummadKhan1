from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_dict = Counter(s)
        t_dict = Counter(t)

        if len(s) > len(t):
            diff = s_dict - t_dict
        else:
            diff = t_dict - s_dict

        new_list = list(diff.keys())
        return new_list[0]

        