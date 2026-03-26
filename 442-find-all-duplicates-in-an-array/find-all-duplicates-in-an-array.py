from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        unique = set(nums)
        res = []

        for u in unique:
            if count[u] == 2:
                res.append(u)
        return res