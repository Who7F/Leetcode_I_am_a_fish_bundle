class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        heap = []
        delta = [0] * (len(nums) + 1)
        curr, j = 0, 0

        for i, val in  enumerate(nums):
            curr += delta[i]
            while j < len(queries) and queries[j][0] == i:
                heappush(heap, -queries[j][1])
                j += 1
            
            while curr < val and heap and -heap[0] >= i:
                curr += 1
                delta[-heappop(heap) + 1] -= 1

            if curr < val:
                return -1

        return len(heap)
