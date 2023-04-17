class Solution:
    def reverse(self, x: int) -> int:
        neg = x<0
        x = abs(x)
        rev = 0
        while x:
            pop = x % 10
            x //= 10
            rev = rev * 10 + pop
        if neg:
            rev = -rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev