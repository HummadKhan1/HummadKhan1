class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        '''
        parameters: arr of pos ints.
        return: int score (sum of all elements in subarr)
        Really asking: Sliding window problem
        '''
        nums_set = set()
        max_sum = 0
        cur_sum = 0
        L = 0

        for R in range(len(nums)):
            while nums[R] in nums_set:
                nums_set.remove(nums[L])
                cur_sum -= nums[L]
                L += 1
            nums_set.add(nums[R])
            cur_sum += nums[R]
            max_sum = max(max_sum, cur_sum)
        return max_sum