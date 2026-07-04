class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1:
            return False

        adjecancy = defaultdict(list)

        for node1, node2 in edges:
            adjecancy[node1].append(node2)
            adjecancy[node2].append(node1)

        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False

            visited.add(node)

            for neighbour in adjecancy[node]:
                if neighbour == prev:
                    continue

                if not dfs(neighbour, node):
                    return False

            return True
    
        return dfs(0, -1) and len(visited) == n
