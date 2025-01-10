# Mutating a shared 
# recursive
# Finds base sebset

# Number of subsets is 2^n. 2 branches at each step.

class Solution:
    def getSub(self, nums: list[int], temp: list[int], anc: list[int], i: int) -> None:    
        if i == len(nums):
            # Adds base case (current subset to results)
            anc.append(temp.copy())

        else:
            # Left branch (exclude current element)
            self.getSub(nums, temp, anc, i + 1)

            # Right branch (include current element)
            temp.append(nums[i])
            self.getSub(nums, temp, anc, i + 1)
            temp.pop()

            
    def subsets(self, nums: List[int]) -> List[List[int]]:
        anc = []
        temp = []

        # Start the recursive process
        self.getSub(nums, temp, anc, 0)

        return anc