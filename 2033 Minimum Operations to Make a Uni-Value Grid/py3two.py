class Solution:
    def flatten(self, grid):
        arr = []
        for g in grid:
            for val in g:
                arr.append(val)

        return arr


    def minOperations(self, grid: List[List[int]], x: int) -> int:

        arr = self.flatten(grid) 
        
        freq = [0]* 10001
        low = arr[0]
        high = arr[0]

        base = arr[0]
        for val in arr:
            if abs(val - base) % x != 0:
                return -1
            freq[val] += 1
            low = min(low, val)
            high = max(high, val)

        target = len(arr) // 2 + 1
        acc = 0
        mid = low

        for i in range(low, high + 1, x):
            acc += freq[i]
            if acc >= target:
                mid = i
                break

        res = 0
        for i in range(low, high + 1, x):
            res += abs(i - mid) // x * freq[i]

        return res
