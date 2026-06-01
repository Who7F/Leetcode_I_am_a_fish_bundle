class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        res = []
        n = len(nums)
        pos = defaultdict(list)

        for i, num in enumerate(nums):
            pos[num].append(i)

        for q in queries:
            arr = pos[nums[q]]

            if len(arr) == 1:
                res.append(-1)
                continue

            idx = bisect_left(arr, q)

            prev_idx = arr[idx - 1]
            next_idx = arr[(idx + 1) % len(arr)]

            d1 = abs(q - prev_idx)
            d1 = min(d1, n - d1)

            d2 = abs(q - next_idx)
            d2 = min(d2, n - d2)

            res.append(min(d1, d2))

            
        return res
        
