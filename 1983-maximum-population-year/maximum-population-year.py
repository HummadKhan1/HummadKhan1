class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        '''
        parameters: 2D int arr logs.
        returns: maximum population
        Really asking: prefix sum.
        constraints:
        '''
        diff = [0]*101
        for birth, death in logs:
            diff[birth-1950] += 1
            diff[death-1950] -= 1
        
        for i in range(1,len(diff)):
            diff[i] += diff[i-1]
        
        max_pop = 0
        res = 0
        for i in range(len(diff)):
            if diff[i] > max_pop:
                max_pop = diff[i]
                res = i+1950
        return res