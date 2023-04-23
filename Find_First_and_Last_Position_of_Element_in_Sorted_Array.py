from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1; end = -1
        #searching for first occurence of target
        left,right = 0,len(nums)-1
        while left<=right:
            mid = (left+right)//2
            if nums[mid]==target:
                start = mid
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid-1
        #searching for last occurence of target
        l,r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                end = mid
                l = mid+1
            elif nums[mid]<target:
                l = mid+1
            else:
                r = mid-1
        return [start, end]