class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        anc = nums[0]
        for i in nums:
            if abs(i) < abs(anc):
                anc = i
            if abs(i) == abs(anc):
                anc = max(anc, i)

        return anc