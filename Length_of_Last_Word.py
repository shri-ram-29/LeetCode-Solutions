class Solution:
    def lengthofLastWord(self, s:str) -> int:
        words = s.split()
        if len(words) == 0:
            return 0
        else:
            return len(words[-1])