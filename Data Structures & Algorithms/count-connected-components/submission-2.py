class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for n1,n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()
        count = 0

        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            
            for adj in graph[node]:
                if adj not in visited:
                    dfs(adj)

            return
        
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1

        return count