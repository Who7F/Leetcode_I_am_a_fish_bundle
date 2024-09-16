class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lit = 0
        big = len(nums) -1
        while lit <= big:
            anc = lit + (big - lit)//2
            if target > nums[anc]: 
                lit = anc + 1
            elif target < nums[anc]:
                big = anc - 1
            else:
                return anc

        return -1
