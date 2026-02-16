class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in group_dict:
                group_dict[sorted_word].append(word)
            else:
                group_dict[sorted_word] = [word]
        return list(group_dict.values())