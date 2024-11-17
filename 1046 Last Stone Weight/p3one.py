class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        heapq._heapify_max(stones)
        while(len(stones) > 1):    
            x = heapq._heappop_max(stones)
            y = heapq._heappop_max(stones)
            if(x != y):
                heapq.heappush(stones, x-y)
                heapq._heapify_max(stones)
        if(len(stones) == 1):
            return heapq._heappop_max(stones)
        return 0
