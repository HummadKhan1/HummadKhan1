from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        '''
        parameters: string s.
        returns: LENGTH of longest palindrome.
        Really asking: Use Counter. add if its an even number and add 1 mid.
        Variables: count, max_len, mid, mid_found.
        Constraints:
        '''
        count = Counter(s)
        unique = set(s)
        max_len = 0
        mid_found = False

        for u in unique:
            if count[u]%2 == 0:
                max_len += count[u]
            else:
                max_len += (count[u])-1
                if not mid_found:
                    mid_found = True
                    max_len += 1
        return max_len
