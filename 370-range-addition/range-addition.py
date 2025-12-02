class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        '''
        parameters: int length, 2D arr updates.
        returns: int arr.
        Really asking: Difference Array problem.
        constraints:
        '''
        diff = [0]*(length+1)

        for start, end, incr in updates:
            diff[start] += incr
            diff[end+1] -= incr

        for i in range(1, length):
            diff[i] += diff[i-1]
        
        return diff[:length]