class Solution:
    def safeCell(self, diff, m, n, grid, x, y):
        print(diff, m, n)
        if m > 1 and n > 1:
            return True

        if diff == grid[x][0] or diff == grid[x][-1] or diff == grid[y][0] or diff == grid[y][-1]:
            return True

        return False


    def check(self, grid, total):
        m, n = len(grid), len(grid[0])

        right = Counter(val for row in grid for val in row)
        left = Counter()

        curr = 0

        for i in range(m - 1):
            for val in grid[i]:
                curr += val
                left[val] += 1
                right[val] -= 1


            diff = total - 2 * curr

            if diff == 0:
                return True
            
            if right[diff] > 0:
                if self.safeCell(diff, m - (i+1), n, grid, i+1, m-1):
                    return True
            elif left[-diff] > 0:
                if self.safeCell(-diff, i + 1, n, grid, 0, i):
                    return True

        return False

    def canPartitionGrid(self, grid):
        total = sum(sum(row) for row in grid)

        if self.check(grid, total):
            return True

        grid = list(zip(*grid))

        return self.check(grid, total)
