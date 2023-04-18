class Solution:
    def palindrome(self, x: int) -> bool:
        original = x; reversed = 0
        while x > 0:
            rem = x % 10
            reversed = (reversed * 10) + rem
            x = x // 10
        return original == reversed
    
s = Solution()
result = s.palindrome(12321)
print(result)
