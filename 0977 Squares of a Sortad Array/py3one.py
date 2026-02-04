class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        num = list(map(lambda n: n*n, nums))
        left = 0
        right = len(num) - 1

        for i in range(len(nums), 0, -1):
            if num[right] > num[left]:
                nums[i - 1] = num[right]
                right -= 1
            else:
                nums[i - 1] = num[left]
                left += 1
        
        return nums