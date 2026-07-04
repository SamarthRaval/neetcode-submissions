class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = {i:0 for i in range(numCourses)}
        graph = defaultdict(list)

        # Populate indegree and graph
        for child, parent in prerequisites:
            indegree[child] += 1
            graph[parent].append(child)

        deque = collections.deque()
        order = []

        # First take all courses which are independent
        for key, value in indegree.items():
            if value == 0:
                deque.append(key)

        # Now iterate over all courses
        while deque:
            course = deque.popleft()
            order.append(course)

            for neighbour in graph[course]:
                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    deque.append(neighbour)

        return order if len(order) == numCourses else []