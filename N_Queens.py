from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def solve(n, row, col, diag, anti_diag, queens, result):
            if row == n:
                result.append(queens)
                return
            for i in range(n):
                if (col >> i) & 1 or (diag >> (row+i)) & 1 or (anti_diag >> (row-i+n-1)) & 1:
                    continue
                solve(n, row+1, col | (1<<i), diag | (1<<(row+i)), anti_diag | (1<<(row-i+n-1)), queens + [i], result)
        
        result = []
        solve(n, 0, 0, 0, 0, [], result)
        return [['.'*i + 'Q' + '.'*(n-i-1) for i in sol] for sol in result]