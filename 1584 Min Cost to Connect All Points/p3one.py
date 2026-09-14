class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 0:
            return 0

        heap = [(0, 0)]
        seen = set()
        cost = 0

        while heap:
            node_cost, node = heapq.heappop(heap)
            if node in seen:
                continue

            seen.add(node)
            cost += node_cost

            for nei in range(n):
                if nei not in seen:
                    nest_cost = (abs(points[node][0] - points[nei][0])+abs(points[node][1] - points[nei][1]))
                    heapq.heappush(heap, (nest_cost, nei))
        
        return cost
        