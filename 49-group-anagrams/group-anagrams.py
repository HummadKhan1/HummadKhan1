class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        parameters: array of strings strs.
        return: array of the strings grouped together.
        Really asking: group anagrams problem.
        1. initialize hashmap.
        2. for loop
        3. 
        '''
        group_dict = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in group_dict:
                group_dict[sorted_word].append(word)
            else:
                group_dict[sorted_word] = [word]
        new_list = list(group_dict.values())
        return new_list