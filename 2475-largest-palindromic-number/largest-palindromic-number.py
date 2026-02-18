from collections import Counter
class Solution:
    def largestPalindromic(self, num: str) -> str:
        '''
        parameters: string num.
        return: str largest palindromic integer.
        Really asking: count_dict, sorted_unique, mid_found, new_str.
        Constraints: no leading zeroes, return "0" if str and mid empty.
        '''
        count_dict = Counter(num)
        sorted_unique = sorted(set(num), reverse=True)
        mid_found = False
        mid = ''
        new_string = ''

        for u in sorted_unique:
            if count_dict[u]%2 == 0:
                new_string += u*(count_dict[u]//2)
            else:
                new_string += u*(count_dict[u]//2)
                if not mid_found:
                    mid_found = True
                    mid = u
        stripped_string = new_string.lstrip('0')
        if not stripped_string and not mid:
            return '0'
        return stripped_string + mid + stripped_string[::-1]