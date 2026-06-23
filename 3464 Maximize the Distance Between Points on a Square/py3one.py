import bisect

class Solution:
    def flatten(self, point, side):
        x, y = point
        if y == 0: return x
        if x == side: return side + y
        if y == side: return 3 * side - x
        return 4 * side - y

    
    def isValid(self, arr, delta, side ,k):
        n = len(arr)
        for i, _ in enumerate(arr):
            ptr = i
            cnt = 1

            while cnt < k:
                target = arr[ptr] + delta

                j = bisect.bisect_left(arr, target)

                if j == n:
                    break

                ptr = j
                cnt += 1

                if delta + arr[ptr] > arr[i] + 4 * side:
                    cnt = 0
                    break
            
            if cnt == k:
                return True

        return False


    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        arr = sorted(self.flatten(point, side) for point in points)

        low, high = 0, side
        res = 0

        while low <= high:
            mid = (low + high) // 2
            if self.isValid(arr, mid, side, k):
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        
        return res
