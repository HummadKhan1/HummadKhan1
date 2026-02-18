class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        '''
        parameters: int arr nums.
        return: arr.
        Really asking: 
        '''
        dup_set = set()
        res = []
        for n in nums:
            if n in dup_set:
                if n not in res:
                    res.append(n)
            else:
                dup_set.add(n)
        return res