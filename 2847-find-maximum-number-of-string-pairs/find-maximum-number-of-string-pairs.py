class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        words_set = set()
        res = 0
        for s in words:
            sorted_s = ''.join(sorted(s))
            if sorted_s in words_set:
                words_set.remove(sorted_s)
                res += 1
            else:
                words_set.add(sorted_s)
        return res