from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        l,r = 0, len(nums)-1
        while(l<r):
            nums[l], nums[r] = nums[r],nums[l]
            l = l+1; r = r-1          
        l,r = 0,k-1
        while(l<r):
            nums[l], nums[r] = nums[r],nums[l]
            l = l+1; r = r-1
        l,r = k, len(nums)-1
        while(l<r):
            nums[l], nums[r] = nums[r], nums[l]
            l = l+1; r = r-1
