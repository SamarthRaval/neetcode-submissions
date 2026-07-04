class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {u:-1 for u in range(1, len(edges)+1)}

        def find(a):
            if parent[a] != -1:
                parent[a] = find(parent[a])
                return parent[a]

            return a

        def union(u, v):
            parent_of_u = find(u)
            parent_of_v = find(v)

            # We found the redundant link
            if parent_of_u == parent_of_v:
                return True

            parent[parent_of_u] = parent_of_v

            return False

        output = []
        for u, v in edges:
            if union(u,v):
                output = [u, v]
                break

        return output

        # This problem is a concept of Union-Find
