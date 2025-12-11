class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        anc = [1] * l
        total = 1
        for i in range(l - 1):
            total = total * nums[i]
            anc[i+1] = anc[i+1] * total

        total = 1
        for i in range(l-1, 0, - 1):
            total = total * nums[i]
            anc[i-1] = anc[i-1] * total
            
        return anc