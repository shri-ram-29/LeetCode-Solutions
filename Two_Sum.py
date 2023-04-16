from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}          #create an empty dict
        for i, num in enumerate(nums):
            if target - num in d:
                return [d[target - num],i]
            d[num] = i
        return []
    
    
s = Solution()
nums = [2, 7, 11, 15]
target = 9
result = s.twoSum(nums, target)
print(result)

    