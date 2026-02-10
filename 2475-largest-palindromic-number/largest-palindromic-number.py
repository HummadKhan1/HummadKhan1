from collections import Counter
class Solution:
    def largestPalindromic(self, num: str) -> str:
        '''
        parameters: string num (digits only).
        return: string using digits from num.
        '''
        num_dict = Counter(num)
        unique = set(num)
        new_string = ''
        sorted_unique = sorted(unique, reverse=True)
        mid_found = False
        mid = ''
        res = ''
        for u in sorted_unique:
            count = num_dict[u]
            if count%2 == 0:
                new_string += u * (num_dict[u]//2)
            else:
                new_string += u * ((count-1)//2)
                if not mid_found:
                    mid = u
                    mid_found = True
        new_string = new_string.lstrip('0')
        if not new_string and not mid:
            return '0'
        res += new_string
        if mid_found:
            res += mid
        res += new_string[::-1]
        return res
        
            

        