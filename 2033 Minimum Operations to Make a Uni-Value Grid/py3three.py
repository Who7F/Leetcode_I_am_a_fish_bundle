class Solution:
    def quickselect(self, nums, k):
        pivot = random.choice(nums)
        left  = [x for x in nums if x < pivot]
        mid   = [x for x in nums if x == pivot]
        right = [x for x in nums if x > pivot]

        if k < len(left):
            return self.quickselect(left, k)
        if k < len(left) + len(mid):
            return pivot
            
        return self.quickselect(right, k - len(left) - len(mid))


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

        center = self.quickselect(arr, len(arr) // 2)

        res = 0
        for val in arr:
            res += abs(val - center) // x

        return res
