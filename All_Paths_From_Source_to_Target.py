class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            if node == n - 1:
                res.append(path)
                return
            for neighbor in graph[node]:
                dfs(neighbor, path + [neighbor])
        
        n = len(graph)
        res = []
        dfs(0, [0])
        return res