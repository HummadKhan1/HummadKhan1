class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        for i in range(len(s)):
            if s[i] in s_dict:
                if t[i] in t_dict:
                   if s_dict[s[i]] != t[i] or t_dict[t[i]] != s[i]:
                    return False
                else:
                    return False
            else:
                if t[i] in t_dict:
                    return False
                else:
                    s_dict[s[i]] = t[i]
                    t_dict[t[i]] = s[i]
        return True