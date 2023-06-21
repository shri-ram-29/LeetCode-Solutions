class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Find the maximum element in the given array
        max_num = max(nums)
        
        # Create a new array to store the sum of points for each number
        points = [0] * (max_num + 1)
        
        # Calculate the sum of points for each number
        for num in nums:
            points[num] += num
        
        # Apply dynamic programming to calculate the maximum points
        dp = [0] * (max_num + 1)
        dp[1] = points[1]
        
        for i in range(2, max_num + 1):
            dp[i] = max(dp[i-1], dp[i-2] + points[i])
        
        # Return the maximum points
        return dp[max_num]