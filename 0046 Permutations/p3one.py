# Mutating a shared 
# recursive
# Gets all the possible permutations

class Solution:
    def findPermuta(self, nums, res, temp):
        print(temp)
        if len(temp) == len(nums):
            # Adds base case (current subset to results)
            res.append(temp.copy())
        else:
            for n in nums:
                if n not in temp:
                    temp.append(n)
                    self.findPermuta(nums, res, temp)
                    temp.pop()

    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        # Start the recursive process
        self.findPermuta(nums, res, [])
        return res
