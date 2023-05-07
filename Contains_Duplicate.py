from typing import List
class Solution:
    def containDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))