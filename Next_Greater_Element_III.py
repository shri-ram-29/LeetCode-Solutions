class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n == 0:
            return -1
    
        nums = list(str(n))
        ln = len(nums)
        i = ln-1
        while i > 0:
            if nums[i-1] < nums[i]:
                break
            i -= 1
        i -= 1  
        if i < 0:
            return -1
        temp = ln-1
        while temp > i:
            if nums[i] < nums[temp]:
                break
            temp -= 1
        nums[i], nums[temp] = nums[temp], nums[i]
        nums[i+1:] = sorted(nums[i+1:]) 
        res = int("".join(nums))
        return  res if (res > n and res <= (2**31-1)) else -1