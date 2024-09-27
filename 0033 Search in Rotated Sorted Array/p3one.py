class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        Split in to sorted and unsorted 
        '''
        lit = 0
        big = len(nums) - 1
        while lit <= big:
            mid = lit + (big - lit) // 2
            if nums[mid] == target:
                return mid
            elif nums[lit] <= nums[mid]:
                if nums[lit] <= target < nums[mid]:
                    big = mid - 1
                else:
                    lit = mid + 1
            else:
                if nums[mid] < target <= nums[big]:
                    lit = mid + 1
                else:
                    big = mid - 1
        return - 1
