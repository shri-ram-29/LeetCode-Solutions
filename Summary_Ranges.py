class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        
        start = end = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == end + 1:
                end = nums[i]
            else:
                if start == end:
                    result.append(str(start))
                else:
                    result.append(str(start) + "->" + str(end))
                start = end = nums[i]
        
        if start == end:
            result.append(str(start))
        else:
            result.append(str(start) + "->" + str(end))
        
        return result