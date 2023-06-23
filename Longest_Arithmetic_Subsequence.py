class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        longest_length = 0
        
        for i in range(n):
            dp[i] = {}
            for j in range(i):
                diff = nums[i] - nums[j]
                if diff in dp[j]:
                    dp[i][diff] = dp[j][diff] + 1
                else:
                    dp[i][diff] = 2
                longest_length = max(longest_length, dp[i][diff])
        
        return longest_length
