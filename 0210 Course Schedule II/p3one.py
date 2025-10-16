class Solution:
    def dfs(self, node, visited, graph, my_list):
        if visited[node] == 2: return True
        if visited[node] == 1: return False

        visited[node] = 1
 
        for i in graph[node]:   
            if not self.dfs(i, visited, graph, my_list):
                return False

        visited[node] = 2
        my_list.append(node)
        return True
        

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        my_list = []
        graph  = defaultdict(list)
        visited = [0] * numCourses

        for value, key in prerequisites:
            graph[key].append(value)

        for i in range(numCourses):
            if not self.dfs(i, visited, graph, my_list):
                return []

        return my_list[::-1]