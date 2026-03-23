class Solution:
    def countLargestGroup(self, n: int) -> int:
        sum_dict = {}
        max_num = 0
        res = 0
        for i in range(1, n+1):
            str_n = str(i)
            if len(str(n)) == 1:
                sum_dict[i] = [i]
                max_num = max(max_num, len(sum_dict[i]))
            else:
                sum = 0
                for c in str_n:
                    sum += int(c)
                if sum in sum_dict:
                    sum_dict[sum].append(i)
                    max_num = max(max_num, len(sum_dict[sum]))
                else:
                    sum_dict[sum] = [i]

        sum_list = list(sum_dict.values())
        print(sum_list)
        for group in sum_list:
            if max_num == len(group):
                res += 1
        
        return res