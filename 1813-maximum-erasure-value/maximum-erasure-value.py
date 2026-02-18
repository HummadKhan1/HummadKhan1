class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        dup_set = set()
        L = 0
        score = 0
        max_score = 0
        
        for R in range(len(nums)):
            while nums[R] in dup_set:
                score -= nums[L]
                dup_set.remove(nums[L])
                L += 1
            dup_set.add(nums[R])
            score += nums[R]
            max_score = max(max_score, score)
        return max_score