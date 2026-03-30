class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        parameters: int height.
        return: # of trapped tiles.
        Actually asking: prefix sum problem. min(maxLeft[i], maxRight[i]) - height[i]
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

        res = 0
        for i in range(len(height)):
            minHeight = min(maxLeft[i], maxRight[i])
            res += max(0, minHeight-height[i])
        return res