class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dict = {}
        L = 0
        max_len = 0
        for R in range(len(s)):
            count_dict[s[R]] = count_dict.get(s[R], 0)+1
            while (R-L+1)-max(count_dict.values()) > k:
                count_dict[s[L]] -= 1
                if count_dict[s[L]] == 0:
                    del count_dict[s[L]]
                L += 1

            max_len = max(max_len, R-L+1)
        return max_len

