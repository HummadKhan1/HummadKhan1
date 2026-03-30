class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix_sums = {0:-1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            remainder = prefix % k

            if remainder in prefix_sums:
                if i-prefix_sums[remainder] >= 2:
                    return True
            else:
                prefix_sums[remainder] = i
        return False