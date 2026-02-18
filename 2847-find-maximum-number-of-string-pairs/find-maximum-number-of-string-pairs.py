class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        words_set = set()
        res = 0

        for s in words:
            if s[::-1] in words_set:
                res += 1
                words_set.remove(s[::-1])
            else:
                words_set.add(s)
        return res