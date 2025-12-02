class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        parameters: int arr height.
        return: total amount of water.
        really asking: min(height[L], height[R]) - nums[i]
        constraints: 
        '''
        maxLeft = []
        max_height = 0
        for n in height:
            maxLeft.append(max_height)
            max_height = max(max_height, n)
        
        maxRight=[0]*len(height)
        max_height = 0
        for i in range(len(height)-1,-1,-1):
            maxRight[i] = max_height
            max_height = max(max_height, height[i])
        res = 0
        for i in range(len(height)):
            cur_height = min(maxLeft[i],maxRight[i])-height[i]
            if cur_height > 0:
                res += cur_height
        return res
            