class Solution:
    def reverseWords(self, s: str) -> str:
        p1 = 0; p2 = 0
        s = list(s)
        while p1 < len(s):
            while p2 < len(s) and s[p2] != ' ':
                p2 += 1
            s[p1:p2] = s[p1:p2][::-1]
            p1 = p2 + 1
            p2 = p1
        return ''.join(s)
