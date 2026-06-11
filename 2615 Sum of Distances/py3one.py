class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        for i in range(n - 1):
            for j in range(i, n):
                if nums[i] == nums[j]:
                    res[i] += abs(i- j)


        for i in range(n - 1, 0, -1):
            for j in range(i, -1, -1):
                if nums[i] == nums[j]:
                    res[i] += abs(i- j)    
                     
        return res
