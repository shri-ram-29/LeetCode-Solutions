class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for i in range(len(temperatures))]
        stack = []
        stack.append(0)
        i=1 
        while i<len(temperatures):
            while len(stack) and temperatures[i]>temperatures[stack[-1]]:
                index = stack[-1]
                ans[index] = i-index
                stack.pop()
            if not len(stack) or temperatures[i]<=temperatures[stack[-1]]:
                stack.append(i)
            i+=1
        return ans