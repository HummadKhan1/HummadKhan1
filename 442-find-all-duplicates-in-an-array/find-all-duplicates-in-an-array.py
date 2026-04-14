from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        num_dict = Counter(nums)
        unique = set(nums)
        res = []

        for u in unique:
            if num_dict[u] > 1:
                res.append(u)
        return res