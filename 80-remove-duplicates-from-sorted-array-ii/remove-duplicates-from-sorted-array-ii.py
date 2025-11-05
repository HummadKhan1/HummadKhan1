class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0

        for n in nums:
            if L < 2 or n != nums[L-2]:
                nums[L] = n
                L += 1
        return L