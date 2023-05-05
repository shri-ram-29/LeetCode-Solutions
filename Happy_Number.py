class Solution:
    def isHappy(self, n: int) -> bool:
        d = set()
        while n!=1:
            n =sum(int(i)**2 for i in str(n))
            if n in d:
                return False
            d.add(n)
        return True