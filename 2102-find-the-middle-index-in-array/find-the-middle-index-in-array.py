class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        '''
        parameters: int arr nums.
        return: leftmost middleindex.
        Actually means: 
        edge cases: sum at i == len(nums) and i == 0 is 0.

        prefix Sums
        '''
        maxLeft= []
        total = 0
        for n in nums:
            maxLeft.append(total)
            total += n
        
        maxRight = [0]*len(nums)
        total = 0
        for i in range(len(nums)-1,-1,-1):
            maxRight[i] = total
            total += nums[i]
        
        for i in range(len(nums)):
            if maxLeft[i] == maxRight[i]:
                return i
        return -1