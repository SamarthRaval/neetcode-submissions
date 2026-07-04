class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacency = defaultdict(list)

        for node1, node2 in edges:
            adjacency[node1].append(node2)
            adjacency[node2].append(node1)

        visited = [False for i in range(n)]
        count = 0

        def dfs(node):
            if visited[node]:
                return 

            visited[node] = True

            for neighbour in adjacency[node]:
                if not visited[neighbour]:
                    dfs(neighbour)

            return

        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count