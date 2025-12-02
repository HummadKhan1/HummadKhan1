class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0]*(n+1)

        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end+1] -= 1
            else:
                diff[start] -= 1
                diff[end+1] += 1

        for i in range(1, n):
            diff[i] += diff[i-1]
        
        new_string = ''
        for i in range(len(s)):
            original = ord(s[i]) - ord('a')
            shift = (original+diff[i]) % 26
            new_letter = chr(shift + ord('a'))
            new_string += new_letter
        return new_string