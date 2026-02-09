class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup_set = set()
        for n in nums:
            if n in dup_set:
                return True
            dup_set.add(n)
        return False