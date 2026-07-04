class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacency = defaultdict(list)

        for n1, n2 in edges:
            adjacency[n1].append(n2)
            adjacency[n2].append(n1)
            
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)
            for neighbour in adjacency[node]:
                if neighbour == prev:
                    continue
                
                if not dfs(neighbour, node):
                    return False

            return True

        return dfs(0, -1) and len(visited) == n
        