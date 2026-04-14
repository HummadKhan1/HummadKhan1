class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Parameters: array of str strs.
        returns: list in list.
        Really asking: group anagrams problem. 
        Variables: group_dict, group_list, sorted_word.
        Constraints: all lowercase, element could be "".
        '''
        group_dict = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in group_dict:
                group_dict[sorted_word].append(word)
            else:
                group_dict[sorted_word] = [word]
        group_list = list(group_dict.values())
        return group_list