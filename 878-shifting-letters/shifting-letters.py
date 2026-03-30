class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        '''
        parameters: string s, int arr shifts. 
        returns: string.
        Really asking: Iterate backwards. chr() and ord().
        constraints:
        '''
        total_shifts = 0
        new_str = ""
        for i in range(len(s)-1,-1,-1):
            total_shifts += shifts[i]
            original = ord(s[i]) - ord('a')
            new_chr = (original + total_shifts) % 26
            new_chr = new_chr + ord('a')
            new_str += chr(new_chr)
        return new_str[::-1]
