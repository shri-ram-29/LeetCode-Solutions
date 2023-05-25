class Solution:
    def arraySign(self, nums: List[int]) -> int:
        result = 1
        for i in nums:
            result = result*i
        return self.signfunc(result)
    def signfunc(self,num):
        if num<0:
            return -1
        elif num>=1:
            return 1
        else:
            return 0
