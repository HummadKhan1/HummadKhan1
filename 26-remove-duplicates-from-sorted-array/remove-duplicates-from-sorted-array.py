class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dup_set = set()
        for n in nums[:]:
            if n in dup_set:
                nums.remove(n)
            else:
                dup_set.add(n)
        return len(nums)