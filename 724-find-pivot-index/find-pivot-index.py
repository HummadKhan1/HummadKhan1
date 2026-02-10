class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        max_left = []
        total = 0
        for n in nums:
            max_left.append(total)
            total += n
        
        max_right = [0]*len(nums)
        total = 0
        for i in range(len(nums)-1,-1,-1):
            max_right[i] = total
            total += nums[i]
        
        for i in range(len(nums)):
            if max_left[i] == max_right[i]:
                return i
        return -1