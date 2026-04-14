class Solution:
    def countLargestGroup(self, n: int) -> int:
        group_dict = {}
        max_len = 0
        for i in range(1, n+1):
            str_i = str(i)
            if len(str_i) == 0:
                sum = i
            else:
                sum = 0
                for j in range(len(str_i)):
                    sum += int(str_i[j])
                
                if sum in group_dict:
                    group_dict[sum].append(i)
                else:
                    group_dict[sum] = [i]
            max_len = max(max_len, len(list(group_dict[sum])))
        group_list = list(group_dict.values())
        res = 0
        for l in group_list:
            if len(l) == max_len:
                res += 1
            
        return res
