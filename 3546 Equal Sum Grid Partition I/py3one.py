class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        hoziz = [0] * len(grid)
        verti = [0] * len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                hoziz[i] += grid[i][j]
                verti[j] += grid[i][j]

        left = 0
        right = len(hoziz) - 1

        totalLeft = 0
        totalRight = 0

        while left <= right:
            if totalLeft > totalRight:
                totalRight += hoziz[right]
                right -= 1
            else:
                totalLeft += hoziz[left]
                left += 1


        if totalLeft == totalRight:
            return True

        left = 0
        right = len(verti) - 1

        totalLeft = 0
        totalRight = 0

        while left <= right:
            if totalLeft > totalRight:
                totalRight += verti[right]
                right -= 1
            else:
                totalLeft += verti[left]
                left += 1

        if totalLeft == totalRight:
            return True

        return False
        
