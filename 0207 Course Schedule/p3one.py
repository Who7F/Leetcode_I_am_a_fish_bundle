class Solution:
    def myDfs(self, node, states, g):
        state = states[node]
        if state == 2: return True
        elif state == 1: return False

        states[node] = 1

        for i in g[node]:
            if not self.myDfs(i, states, g):
                return False

        states[node] = 2
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[b].append(a)

        states = [0] * numCourses

        return all(self.myDfs(i, states, g) for i in range(numCourses))
