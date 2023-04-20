class Solution:
    def isValid(self, s: str) -> bool:
        s1 = []; balanced = True; index = 0
        while index < len(s) and balanced:
            symbol = s[index]
            if symbol in "([{":
                s1.append(symbol)
            else:
                if not s1:
                    balanced = False
                else:
                    top = s1.pop()
                    if not self.matches(top, symbol):
                        balanced = False
            index += 1
        if balanced and not s1:
            return True
        else:
            return False

    @staticmethod
    def matches(open, close):
        opens = "([{"
        closes = ")]}"
        return opens.index(open) == closes.index(close)