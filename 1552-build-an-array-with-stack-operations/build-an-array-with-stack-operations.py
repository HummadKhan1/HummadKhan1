class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        new_list = []
        j = 0
        for i in range(1, n+1):
            if new_list == target:
                break
            res.append("Push")
            new_list.append(i)
            if i != target[j]:
                res.append("Pop")
                new_list.pop(j)
                j -= 1
            j += 1
        return res