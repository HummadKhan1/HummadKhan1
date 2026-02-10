class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        '''
        parameters: arr words.
        return: maximum number fo pairs.
        Really asking: pair using hashmap.
        '''
        word_dict = {}
        res = 0
        for s in words:
            sorted_s = ''.join(sorted(s))
            if sorted_s in word_dict:
                res += 1
                del word_dict[sorted_s]
            else:
                word_dict[sorted_s] = s
        return res