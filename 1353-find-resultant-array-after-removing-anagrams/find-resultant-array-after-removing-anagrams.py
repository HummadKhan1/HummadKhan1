class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        '''
        parameters: str arr.
        return: words arr.
        '''

        new_list = [words[0]]

        for i in range(1, len(words)):
            if sorted(words[i-1]) == sorted(words[i]):
                continue
            else:
                new_list.append(words[i])
        return new_list
