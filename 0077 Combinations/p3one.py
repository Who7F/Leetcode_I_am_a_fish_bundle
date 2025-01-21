# Mutating a shared 
# recursive
# Finds base sebset

class Solution:
    def findNumbers(self, n, k, res, sol):        
        if len(sol) == k:
            # Adds base case (current subset to results)
            res.append(sol.copy())
        else:
            # Left branch (exclude current element)
            if n > k - len(sol):
                self.findNumbers(n - 1, k, res, sol)
            
            # Right branch (include current element)
            sol.append(n)
            self.findNumbers(n - 1, k, res, sol)
            sol.pop()


    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        sol = []
        # Start the recursive process
        self.findNumbers(n, k, res, sol)
        return res
