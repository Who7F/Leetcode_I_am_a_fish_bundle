class Solution:
    def flatten(self, grid):
        arr = []
        for g in grid:
            for val in g:
                arr.append(val)

        return arr


    def minOperations(self, grid: List[List[int]], x: int) -> int:

        arr = self.flatten(grid) 
        
        base = arr[0]
        for val in arr:
            if abs(val - base) % x != 0:
                return -1

        arr.sort()

        center = arr[len(arr)//2]

        res = 0
        for val in arr:
            res += abs(val - center) // x

        return res
