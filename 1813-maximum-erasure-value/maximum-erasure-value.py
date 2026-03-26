class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        max_score = 0
        cur_score = 0
        s_set = set()
        L = 0

        for R in range(len(nums)):
            while nums[R] in s_set:
                s_set.remove(nums[L])
                cur_score -= nums[L]
                L += 1
            s_set.add(nums[R])
            cur_score += nums[R]
            max_score = max(max_score, cur_score)
        return max_score
