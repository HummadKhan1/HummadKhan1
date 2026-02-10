from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        parameters: int arr nums.
        return: array of dups.
        Really asking: Using Dict and set.
        '''
        nums_dict = Counter(nums)
        unique = set(nums)
        res = []
        for u in unique:
            if nums_dict[u] > 1:
                res.append(u)
        return res