class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency = defaultdict(list)

        for n1, n2 in edges:
            adjacency[n1].append(n2)
            adjacency[n2].append(n1)

        visited = [False for i in range(n)]
        count = 0

        def dfs(node):
            visited[node] = True
            
            for neighbour in adjacency[node]:
                if not visited[neighbour]:
                    dfs(neighbour)

        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count