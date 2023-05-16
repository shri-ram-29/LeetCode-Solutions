class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        m = len(grid)
        n = len(grid[0])

        def bfs():
            q = deque()
            for x in range(m):
                for y in range(n):
                    if grid[x][y] == 2:
                        q.append((0,x,y))
            res = 0
            while q:
                level,x0,y0 = q.popleft()
                res = level
                for dx, dy in d:
                    x,y = x0+dx,y0+dy
                    if 0<=x<m and 0<=y<n and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((level+1,x,y))
            return res
        res = bfs()
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    return -1
        return res        