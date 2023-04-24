class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        n1, n2 = 0, 0
        for i in num1:
            n1 = n1 * 10 + ord(i) - ord('0')
        for i in num2:
            n2 = n2 * 10 + ord(i) - ord('0')
        result = n1 * n2
        if result == 0:
            return '0'
        s = ''
        while result > 0:
            digit = result % 10
            s = chr(digit + ord('0')) + s
            result //= 10
        return s
