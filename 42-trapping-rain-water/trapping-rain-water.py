class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        paramters: int arr height.
        return: total amount of water that will stay.
        Really asking: prefix sum problem where total amount of water that can be held in height[i] is = min(maxLeft[i], maxRight[i]) - height[i].
        '''
        maxLeft = []
        maxHeight = 0
        for n in height:
            maxLeft.append(maxHeight)
            maxHeight = max(maxHeight, n)
        
        maxRight = [0]*len(height)
        maxHeight = 0
        for i in range(len(height)-1,-1,-1):
            maxRight[i] = maxHeight
            maxHeight = max(maxHeight, height[i])
        
        total = 0
        for i in range(len(height)):
            diff = min(maxLeft[i], maxRight[i]) - height[i]
            if diff > 0:
                total += diff
        return total