#In this the arrays contains duplicate values
from typing import List
class Solution:
    def findMin(self,nums: List[list]) -> int:
        n = len(nums); left = 0; right = n-1
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]