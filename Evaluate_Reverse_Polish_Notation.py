from math import trunc
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in {"+","-","*","/"}:
                stack.append(int(t))
            else:
                a,b = stack.pop(),stack.pop()
                if t == '+': stack.append(b+a)
                elif t == '-': stack.append(b-a)
                elif t == '*': stack.append(b*a)
                else: stack.append(trunc(b/a))
        return stack[0]