from collections import Counter
class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        new_str = ""
        mid = ""
        mid_found = False
        unique = set(num)
        u_list = list(unique)
        u_list.sort(reverse=True)

        for u in u_list:
            value = count[u]
            if count[u]%2 == 0:
                new_str += u*((value)//2)
            else:
                new_str += u*((value-1)//2)
                if not mid_found:
                    mid = u
                    mid_found = True
        new_str = new_str.lstrip("0")
        if not new_str and not mid:
            return '0'
        res = new_str + mid + new_str[::-1]
        return res