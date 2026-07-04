class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = {i:0 for i in range(numCourses)}
        graph = defaultdict(list)

        for child, parent in prerequisites:
            indegree[child] += 1
            graph[parent].append(child)

        deque = collections.deque()
        seen = 0

        # Only courses to take care of which has no dependent
        for key, val in indegree.items():
            if val == 0:
                deque.append(key)

        print(graph)
        print(indegree)
        # BFS - to iterate to all neighbours
        while deque:
            course = deque.popleft()
            seen += 1

            for neighbour in graph[course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    deque.append(neighbour)

        return True if seen == numCourses else False