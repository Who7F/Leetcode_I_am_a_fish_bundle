class Solution:
    def findMin(self, nums: List[int]) -> int:
        lit = 0
        big = len(nums) - 1
        if nums[0] > nums[big]:
            while lit < big:
                mid = lit + (big - lit) // 2
                if nums[mid] > nums[big]:
                    lit = mid + 1
                else:
                    big = mid
            return nums[lit]

        else:
            return nums[0]
