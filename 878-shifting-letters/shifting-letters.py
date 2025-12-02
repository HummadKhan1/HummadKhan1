class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        '''
        parameters: string s, int arr shifts.
        returns: final string afterall shifts are applied.
        Really asking: prefix sums
        constraints:
        '''
        new_str = ""
        total_shifts = 0
        for i in range(len(s)-1,-1,-1):
            total_shifts += shifts[i]
            original = ord(s[i])-ord('a')
            original = (original+total_shifts) % 26
            new_letter = chr(original+ord('a'))
            new_str += new_letter
        return new_str[::-1]
