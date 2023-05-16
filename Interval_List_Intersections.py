class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0; j = 0
        result = []
        while i < len(firstList) and j < len(secondList):
            starti,endi = firstList[i]
            startj,endj = secondList[j]

            if endi>=startj and endj>=starti:
                result.append([max(starti,startj), min(endi,endj)])
            
            if endi < endj:
                i+=1
            else:
                j+=1
        return result