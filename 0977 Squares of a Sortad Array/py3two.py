class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        num = list(map(lambda n: n*n, nums))
        num.sort()
        return num