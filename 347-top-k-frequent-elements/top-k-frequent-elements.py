from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_list = []

        for num, count in freq.items():
            sorted_list.append([count, num])
        
        sorted_list.sort()

        res = []
        for i in range(k):
            res.append(sorted_list.pop()[-1])
        return res
