class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        lengths = {}
        res = 0

        for num in nums:
            if num not in lengths:
                left = lengths.get(num - 1, 0)
                right = lengths.get(num + 1, 0)
                total = left + 1 + right

                lengths[num] = total
                lengths[num - left] = total
                lengths[num + right] = total

                res = max(res, total)

        return res