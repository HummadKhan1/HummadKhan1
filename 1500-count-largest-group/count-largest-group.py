class Solution:
    def countLargestGroup(self, n: int) -> int:
        #parameters: int n.
        #return: number of groups with the largest size.
        #constraints: 
        # 1. Initialize group dict.
        # 2. Loop through n
        # 3.    if len(n)== 1:
        # 4.        if group does not exist than create it with n as key
        # 5.        else add this into the existing group
        # 6.    else
        # 7.        make new variable thats str(n)
        # 8.        total = 0
        # 9.        for len(str(n))
        # 10.       total += int(str_n[i])
        # 11.       if group_dict
        group_dict = {}
        max_len = 0
        for i in range(1,n+1):
            str_n = str(i)
            total = 0
            for i in range(len(str_n)):
                total += int(str_n[i])
            if total in group_dict:
                group_dict[total].append(n)
            else:
                group_dict[total] = [n]
            if len(group_dict[total]) > max_len:
                max_len = len(group_dict[total])
        print(group_dict.values())
        res = 0
        new_list = list(group_dict.values())
        for l in new_list:
            if len(l) == max_len:
                res += 1
        return res
