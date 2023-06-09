from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set(); nums.sort()
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i+1; r = len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s==0:
                    res.add((nums[i],nums[l],nums[r]))
                    l += 1; r -= 1
                    while l<r and nums[l] == nums[l-1]:
                        l += 1
                    while l<r and nums[r] == nums[r+1]:
                        r -= 1
                elif s<0:
                    l += 1
                else:
                    r -= 1
                    
        return list(res)
    
nums = [-1,0,1,2,-1,-4]
sol = Solution()
print(sol.threeSum(nums))