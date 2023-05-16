from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]:
            return -1
        
        queue = deque([(0, 0, 1)])  
        visited = set([(0, 0)])    
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        while queue:
            row, col, depth = queue.popleft()
            if row == n-1 and col == n-1:
                return depth  
            for d in directions:
                r, c = row + d[0], col + d[1]
                if 0 <= r < n and 0 <= c < n and (r, c) not in visited and grid[r][c] == 0:
                    queue.append((r, c, depth+1))
                    visited.add((r, c))

        return -1
            