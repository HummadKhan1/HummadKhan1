class Solution:
    def countLargestGroup(self, n: int) -> int:
        '''
        parameters: int n
        return: NUMBER of groups that have largest size.
        Really asking: hashmap problem.

        '''
        group_dict = {}
        max_len = 0
        res = 0
        for i in range(1, n+1):
            str_i = str(i)
            total = 0
            for s in str_i:
                total += int(s)
            if total in group_dict:
                group_dict[total].append(i)
            else:
                group_dict[total] = [i]
            max_len = max(max_len, len(group_dict[total]))
        new_list = list(group_dict.values())
        for l in new_list:
            if len(l) == max_len:
                res += 1
        return res
            
