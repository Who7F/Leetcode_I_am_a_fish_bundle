# Mutating a shared 
# recursive
# Gets all the possible permutations

class Solution:
    def findPermuta(self, nums, res, index):
        if index == len(nums):
            # Adds base case (current subset to results)
            res.append(nums.copy())
        else:
            for i in range(index, len(nums)):  
                nums[index], nums[i] = nums[i], nums[index]
                self.findPermuta(nums, res, index + 1)
                nums[index], nums[i] = nums[i], nums[index]


    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Start the recursive process
        self.findPermuta(nums, res, 0)
        return res
