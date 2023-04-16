class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s
        start, end, n  = 0, 0, len(s)
        for i in range(n):
            left, right = i, i
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1; right += 1
            if right - left - 1 > end - start:
                start, end = left + 1, right - 1
            left, right = i, i + 1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if right - left - 1 > end - start:
                start, end = left + 1, right - 1
        return s[start:end+1]
    
sol = Solution()
print(sol.longestPalindrome("babad"))
