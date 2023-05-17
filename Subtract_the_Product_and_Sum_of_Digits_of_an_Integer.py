class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum, pro = 0,1
        while n>0:
            sum+=n%10
            pro = pro*(n%10)
            n = n//10
        return (pro-sum)