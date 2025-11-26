class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        parameters: int arr nums
        return: subarray with largest product
        constraints: elements could be negative
        reall asking: 
        '''
        max_prod = nums[0]
        min_prod = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            temp = max_prod
            max_prod = max(max_prod*nums[i], min_prod*nums[i], nums[i])
            min_prod = min(min_prod*nums[i], temp*nums[i], nums[i])
            res = max(max_prod, res)
        return res