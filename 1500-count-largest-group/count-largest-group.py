class Solution:
    def countLargestGroup(self, n: int) -> int:
        '''
        parameters: int n.
        return: number of groups.
        Really asking: dictionary grouping problem.
        '''
        group_dict = {}
        max_size = 0
        res = 0
        for i in range(1, n+1):
            total = 0
            str_n = str(i)
            for num in str_n:
                total += int(num)
            print(total)
            if total in group_dict:
                group_dict[total].append(i)
            else:
                group_dict[total] = [i]

            max_size = max(max_size, len(group_dict[total]))
        
        new_list = list(group_dict.values())
        for group in new_list:
            if len(group) == max_size:
                res += 1
        return res