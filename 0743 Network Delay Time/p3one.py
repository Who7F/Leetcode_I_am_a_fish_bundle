class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        
        for key, target, time in times:
            graph[key].append([target, time])
        
        seen = {}
        heap = [(0, k)]

        while heap:
            cost, node = heapq.heappop(heap)
            
            if node in seen: continue
            seen[node] = cost
            
            for g in graph[node]:
                if g[0] not in seen:
                    heapq.heappush(heap, (cost + g[1], g[0]))

        return max(seen.values()) if len(seen) == n else -1
        