class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        x,y = [],[]
        x.extend(nums),y.extend(nums)
        x.sort()
        y.sort(reverse=True)
        if(x==nums or y==nums):
            return True
        return False
