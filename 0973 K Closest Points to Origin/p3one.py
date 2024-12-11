class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, j in points:
            destance = i*i + j*j
            if len(heap) < k:
                heapq.heappush(heap, (-destance, i, j))
            else:
                heapq.heappushpop(heap, (-destance, i, j))

        return [(i, j) for _, i, j in heap]