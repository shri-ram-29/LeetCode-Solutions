from typing import List
def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    n = len(nums)
    left = 0; right = 0
    min_len = float('inf'); window_sum = 0
    while right < n:
        window_sum += nums[right]
        right += 1
        while window_sum >=target:
            min_len = min(min_len, right-left)
            window_sum -= nums[left]
            left += 1
    return min_len if min_len != float('inf') else 0
