from collections import Counter
class Solution:
    def largestPalindromic(self, num: str) -> str:
        '''
        parameters: str num.
        return: str largest palindromic integer.
        Really asking: count_dict, sorted_unique, mid_found.
        Constraints: NO LEADING ZEROES
        '''
        count_dict = Counter(num)
        unique = set(num)
        sorted_unique = sorted(unique, reverse=True)
        new_string = ""
        mid_found = False
        mid = ""
        for s in sorted_unique:
            if count_dict[s]%2 == 0:
                new_string += s*(count_dict[s]//2)
            else:
                if not mid_found:
                    mid = s
                    mid_found = True
                    new_string += s*(count_dict[s]//2)
                else:
                    new_string += s*(count_dict[s]//2)
        stripped_string = new_string.lstrip("0")
        if not stripped_string and not mid:
            return "0"
        return stripped_string + mid + stripped_string[::-1]