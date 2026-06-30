class Solution:
    def centerHeap(self, nums, k):
        heap = []
        for val in nums:
            if len(heap) < k:
                heapq.heappush(heap, val)
            elif val > heap[0]:
                heapq.heappushpop(heap, val)

        return heap[0] if heap else None


    def flatten(self, grid):
        arr = []
        for g in grid:
            for val in g:
                arr.append(val)

        return arr


    def minOperations(self, grid: List[List[int]], x: int) -> int:

        arr = self.flatten(grid) 
        if len(arr) == 1:
            return 0
        
        base = arr[0]
        for val in arr:
            if abs(val - base) % x != 0:
                return -1

        center = self.centerHeap(arr, len(arr) // 2 + 1)

        res = 0
        for val in arr:
            res += abs(val - center) // x

        return res
