class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        pointer_one = 0; pointer_two = len(nums)-1
        index = len(nums)-1
        res = [0 for x in nums]
        while(pointer_one<=pointer_two):
            if abs(nums[pointer_one]) > abs(nums[pointer_two]):
                res[index] = nums[pointer_one]*nums[pointer_one]
                pointer_one = pointer_one+1
            else:
                res[index] = nums[pointer_two]*nums[pointer_two]
                pointer_two = pointer_two-1
            index = index-1
        return res

        