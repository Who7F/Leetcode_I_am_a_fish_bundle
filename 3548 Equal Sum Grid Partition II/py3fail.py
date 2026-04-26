class Solution:
    def matchPartition(self, diff, right, left, size_right, size_left, unbreke_left, unbrake_right):
        print(unbreke_left, unbrake_right, diff)
        if diff == 0:
            return True
        if diff > 0:
            return (size_right > 1 and right[diff] > 0) or diff in unbrake_right
        return (size_left > 1 and left[-diff] > 0) or -diff in unbreke_left

    def check(self, grid):
        m, n = len(grid), len(grid[0])
        total = sum(sum(row) for row in grid)

        right = Counter(val for row in grid for val in row)
        left = Counter()

        curr = 0

        for i in range(m - 1):
            for val in grid[i]:
                curr += val
                left[val] += 1
                right[val] -= 1
                if right[val] == 0:
                    del right[val]

            diff = total - 2 * curr

            if self.matchPartition(diff, right, left, m - i - 1, i + 1, [grid[0][0], grid[0][-1]], [grid[-1][0], grid[-1][-1]]):
                return True

        return False

    def canPartitionGrid(self, grid):
        if self.check(grid):
            return True

        grid = list(zip(*grid))

        return self.check(grid)
