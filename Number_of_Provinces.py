from typing import List
class Solution:
    def findCircleNum(self, matrix: List[List[int]]) -> int:
        def dfs(city):
            visited.add(city)
            for neighbor, connected in enumerate(matrix[city]):
                if connected == 1 and neighbor not in visited:
                    dfs(neighbor)
                    
        count = 0
        visited = set()
        for city in range(len(matrix)):
            if city not in visited:
                dfs(city)
                count += 1
        return count