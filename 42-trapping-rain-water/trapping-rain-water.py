class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxHeight = 0
        for n in height:
            maxLeft.append(maxHeight)
            maxHeight = max(maxHeight, n)
        
        print(maxLeft)
        maxRight = [0]*len(height)
        maxHeight = 0
        for i in range(len(height)-1,-1,-1):
            maxRight[i] = maxHeight
            maxHeight = max(maxHeight, height[i])
        print(maxRight)

        res = 0
        for i in range(len(height)):
            diff = min(maxLeft[i], maxRight[i]) - height[i]
            if diff > 0:
                res += diff
        return res