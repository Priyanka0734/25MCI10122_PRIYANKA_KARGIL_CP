from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:

        adj = [[] for i in range(numCourses)]
        indegree = [0] * numCourses

        for u, v in prerequisites:

            adj[v].append(u)
            indegree[u] += 1

        order = []

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:

            node = queue.popleft()
            order.append(node)

            for neigh in adj[node]:

                indegree[neigh] -= 1

                if indegree[neigh] == 0:

                    queue.append(neigh)

        return order if len(order) == numCourses else []