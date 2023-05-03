from typing import List
from collections import deque 
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        queue = deque()

        # Find all 'O's on the borders and add them to the queue
        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == 'O':
                    queue.append((r, c))
                    board[r][c] = 'B'  # Mark as visited
        
        # BFS to find all 'O's that are 4-directionally surrounded by 'X'
        while queue:
            r, c = queue.popleft()
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or board[nr][nc] != 'O':
                    continue
                queue.append((nr, nc))
                board[nr][nc] = 'B'  # Mark as visited
        
        # Mark all remaining 'O's as 'X' and revert 'B's back to 'O's
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'B':
                    board[r][c] = 'O'